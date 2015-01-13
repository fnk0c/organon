#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of 
#Reaver-1.4 on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"18/12/14"

import os

comandos = [
	"sudo apt-get install libpcap*-dev libsqlite3-dev -y",
	"wget https://reaver-wps.googlecode.com/files/reaver-1.4.tar.gz",
	"tar xpvf reaver-1.4.tar.gz",
	"cd reaver-1.4/src && ./configure && make && sudo make install"]

try:
   input = raw_input
except NameError:
   pass

print("\n Install Reaver and its dependencies?\n [Y]es [N]o [V]iew dependencies")
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
  write \"reaver\" without the quotes on your terminal
  and hit ENTER to run the application
""")
print("-"*80)
