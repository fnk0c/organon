#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of 
#Aircrack-ng on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"13/12/2014"

import os

comandos = [
	"sudo apt-get install build-essential libssl-dev pkg-config libpcre3-dev libnl-3-dev libnl-genl-3-dev -y",
	"wget http://download.aircrack-ng.org/aircrack-ng-1.2-rc1.tar.gz",
	"tar xpvf aircrack-ng-1.2-rc1.tar.gz",
	"cd aircrack-ng-1.2-rc1/ && make && sudo make install && sudo airodump-ng-oui-update"]

try:
   input = raw_input
except NameError:
   pass

print("\n Install Aircrack-ng and its dependencies?\n [Y]es [N]o [V]iew dependencies")
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
  write \"sudo air\" without the quotes on your terminal
  and hit TAB twice to see all the applications installed
""")
print("-"*80)
