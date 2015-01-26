#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of 
#Nmap 6.47 on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"20/12/2014"

import os

comandos = [
	"tar xpvf nmap-6.47.tar.bz2",
	"cd nmap-6.47 && ./configure && make && sudo make install"]

for action in comandos:
	os.system(action)

print("\n\n")
print("-"*80)
print("\n All clear\n Enjoy!")
print("""
  write \"nmap\" without the quotes on your terminal
  and hit ENTER to run the application
""")
print("-"*80)
