#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of 
#Aircrack-ng on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"26/12/2014"

import os

comandos = [
	"sudo apt-get install git python-mechanize -y",
	"git clone https://github.com/fnk0c/cangibrina.git",
	"cd cangibrina && sh linux_install.sh"]

try:
   input = raw_input
except NameError:
   pass

print("\n Install Cangibrina and its dependencies?\n [Y]es [N]o [V]iew dependencies")
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
  write \"cangibrina\" without the quotes on your terminal
  and hit ENTER to run the application
""")
print("-"*80)
