#!/usr/bin/ruby -W0

###################################################################
# This script is responsible for making the connection to the     #
# MySQL database					          #
#								  # #								  #
# Maximoz Sec <maximozsec@outlook.com.br>	       		  #
# 01/02/2015							  #
###################################################################

require 'mysql'
require 'colorize'

$server = "104.236.105.209"
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
				puts "[" + "!".red + "]" + " Error code: " + "#{e.errno}".yellow
				puts "[" + "!".red + "]" + " Error message: " + "#{e.error}".yellow
				puts "[" + "!".red + "]" + " Error SQLSTATE: " + "#{e.sqlstate}".yellow if e.respond_to?("sqlstate")	
				exit 1
		end
	end		

	def install(install_command) # Method to install tools
		begin
			# Requesting information from database as of a SQL command
			result = $db.query(install_command)
			result.each do |row|
				
				if row[0].include?("https://github.com/")   # Checking if the tool is 
					get = "git clone #{row[0]}"         # located on github or belongs 
				else				       	    # to another source
					get = "wget #{row[0]}"
				end
				puts " [" + "!".red + "] Downloading source\n #{get}"
				system get
				
				pkgconf = "wget http://104.236.105.209/organon/pkgconfig/#{row[2]}.conf"
				puts pkgconf
				system pkgconf

				if row[1].nil? == false	
					dep = "sudo apt-get install #{row[1]} -y"
					puts " [" + "!".red + "] Installing dependencies\n #{dep}"
					system dep
				else
					puts "[" + "~".blue + "] No necessary dependence"
				end
				
			end
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
		
	   	result.free
		end
	end
end # Ending class Resp
	
action = Resp.new
	
begin
	if 'install' == ARGV[0]
		action.connect
		action.install(ARGV[1])
	elsif 'list' == ARGV[0]
		action.connect
		action.list(ARGV[1])
	else
		exit 1
	end
end
