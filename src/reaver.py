#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of 
#Reaver-1.4 on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"18/12/14"

import os

comandos = [
	"tar xpvf reaver-1.4.tar.gz",
	"cd reaver-1.4/src && ./configure && make && sudo make install"]

for a in comandos:
	os.system(a)

print("\n\n")
print("-"*80)
print("\n All clear\n Enjoy!")
print("""
  write \"reaver\" without the quotes on your terminal
  and hit ENTER to run the application
""")
print("-"*80)
