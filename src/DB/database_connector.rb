#!/usr/bin/ruby

=begin
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 This script is responsible for making the connection to the
 MySQL database

 Maximoz Sec <maximozsec@outlook.com.br>
 01/02/2015
 
	Copyright (C) 2015  Franco Colombino & Ygor Máximo

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
=end

begin
	require 'mysql'
	require 'colorize'
	require 'nokogiri'
	require 'open-uri'
	require 'net/http'
rescue Interrupt
	warn "You have interrupted the application."
	exit 1
end

doc = Nokogiri::HTML(open("http://organon.ddns.net"))

$server = doc.css('link')[0]['href'].gsub!("http://", "").gsub!(":1000/favicon.ico", "")
$user = "organonuser"
$pass = "organon"
$database = "organon"


class Resp
		
	def connect
		begin				
			# Connect to the MySQL server
			$db = Mysql.real_connect($server, $user, $pass, $database)
				
		# If eventually occur some error
		rescue Mysql::Error => e
			sgn = "[" + "!".red + "]"
			puts sgn + " Error code: " + "#{e.errno}".yellow
			puts sgn + " Error message: " + "#{e.error}".yellow
			puts sgn + " Error SQLSTATE: " + "#{e.sqlstate}".yellow if e.respond_to?("sqlstate")	
			puts sgn + " If you get this error, please let us an issue as soon! github.com/maximozsec/organon/issues"
			exit 1
		end
	end		

	def install(install_command) # Method to install tools
		begin
			# Requesting information from database as of a SQL command
			result = $db.query(install_command)
			result.each do |row|
			
				# Checking if the tool is located on github or belongs to another source
				if row[0].include?("https://github.com/")
						get = "cd .cache && git clone --depth 1 #{row[0]}" # Update the github tool
						puts " [" + "!".red + "] Downloading source\n #{get}"
						system get
				else				       	    			
						get = "cd .cache && wget -c #{row[0]}" # Continue the download from the last download stage
						puts " [" + "!".red + "] Downloading source\n #{get}"
						system get
				end
				
				# Downloading the tool configuration file
				pkgconf = Net::HTTP.get(URI "http://#{$server}:1000/organon/pkgconfig/debian/#{row[2]}.conf")

				File.open("#{row[2]}.conf", "w+") do |file|
					file.write(pkgconf)
				end

				if row[1] != 'NULL' # Checking if the row of the dependencies of the given tool is not empty
					puts "The following dependencies are necessary for this tool."
					puts "(#{row[1].split.length}) #{row[1]}\n"
					puts " [" + "!".red + "] Installing dependencies........"
					system "sudo apt-get install #{row[1]} -y"      
				else
					puts "[" + "~".blue + "] No necessary dependence"
				end
			end
		rescue Interrupt
			warn "You have interrupted the labeling."
			exit 1
		end
		result.free
			# Invoking .free to release the result set. 
			# After that point, the result set is invalid 
			# and you should not invoke any of the object's methods.
	end
	
	def list(list_command) # Method to list tools
		begin
			result = $db.query(list_command)
	   		result.each do |row| # Listing each row
	     		puts <<TOOLS

 #{"[" + " + ".green + "]"} #{row[0]} #{"v#{row[1]}".yellow}
 #{row[2]}

TOOLS
	  		end
		rescue Interrupt
			warn "You have interrupted the instalation."
			exit 1
		end
		result.free
	end

	def remove(remove_command)
		begin
			result = $db.query(remove_command)
			result.each do |row|
				system "sudo apt-get remove #{row[0]}"
			end
		rescue Interrupt
			warn "Interrupted."
			exit 1
		end
	end
end # Ending Resp class
	
action = Resp.new

begin
	case ARGV[0]
	when "install" 
		action.connect
		action.install(ARGV[1])
	when "list" 
		action.connect
		action.list(ARGV[1])
	when "remove"
		action.connect
		action.remove(ARGV[1])
	else
		exit 1
	end
rescue StandardError => e
	warn "ERROR: #{e.message}"
end
