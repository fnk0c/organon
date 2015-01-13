#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of 
#Hydra on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"27/12/2014"

import os

comandos = [
	"sudo apt-get install libssl-dev libssh-dev libidn11-dev libpcre3-dev libgtk2.0-dev libmysqlclient-dev libpq-dev libsvn-dev firebird2.1-dev libncp-dev libncurses5-dev -y",
	"git clone https://github.com/vanhauser-thc/thc-hydra.git",
	"cd thc-hydra && ./configure && make && sudo make install"]

try:
   input = raw_input
except NameError:
   pass

print("\n Install Hydra and its dependencies?\n [Y]es [N]o [V]iew dependencies")
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
  write \"hydra\" without the quotes on your terminal
  and hit ENTER to run the application
""")
print("-"*80)
