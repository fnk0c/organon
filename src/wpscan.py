#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of
#Wpscan on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"Germany/Brazil/15"     #2014 World Cup game result (7 x 1)
         
import os

comandos = [
	"cd wpscan && sudo gem install json -v '1.8.1'",
	"cd wpscan && sudo gem install nokogiri -v '1.6.5'",
	"cd wpscan && sudo gem install bundle",
	"cd wpscan && bundle install --without test --path vendor"]

for a in comandos:
	os.system(a)

os.chdir("src/")
os.system("sudo ./generator.py wpscan ruby wpscan.rb")

print("\n\n")
print("-"*80)
print("\n All clear\n Enjoy!")
print("""
 write \"wpscan\" without the quotes on your terminal
 and hit ENTER to run the application
 """)
print("-"*80)
