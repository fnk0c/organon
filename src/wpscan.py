#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of
#Wpscan on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"Germany/Brazil/15"     #2014 World Cup game result (7 x 1)
         
import os

comandos = [
	"sudo apt-get install ruby ruby-dev libcurl4-gnutls-dev make git bundler -y",
	"git clone https://github.com/wpscanteam/wpscan.git",
	"sudo gem install json -v '1.8.1' ",
	"sudo gem install nokogiri -v '1.6.5' ",
	"sudo gem install typhoeus",
	"sudo gem install --user-install terminal-table",
	"sudo gem install --user-install ruby-progressbar"
	"sudo mv wpscan /opt",
	"cd /opt/wpscan && bundle install --without test --path vendor",
	"sudo sh -c 'echo \#\!/bin/bash >> /usr/bin/wpscan'",
	"sudo sh -c 'echo cd /opt/wpscan >> /usr/bin/wpscan'",
	"sudo sh -c 'echo exec ruby wpscan.rb \$\@ >> /usr/bin/wpscan'",
	"sudo chmod +x /usr/bin/wpscan"]

try:
   input = raw_input
except NameError:
   pass
       
print("\n Install WPScan and its dependencies?\n [Y]es [N]o [V]iew dependencies")
answer = input("\n>> ").lower()

if answer == "y":
	for action in comandos:
		os.system(action)

elif answer == "n":
	exit()

elif answer == "v":
	print(comandos[0].replace("sudo apt-get install", "").replace("-y", ""))
	exit()

else:
	print("Invalid option")
	exit()

print("\n\n")
print("-"*80)
print("\n All clear\n Enjoy!")
print("""
 write \"wpscan\" without the quotes on your terminal
 and hit ENTER to run the application
 """)
print("-"*80)
