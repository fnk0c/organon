#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of 
#Aircrack-ng on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"26/12/2014"

import os

comandos = [
	"cd cangibrina && sh linux_install.sh"]

for a in comandos:
	os.system(a)

print("\n\n")
print("-"*80)
print("\n All clear\n Enjoy!")
print("""
  write \"cangibrina\" without the quotes on your terminal
  and hit ENTER to run the application
""")
print("-"*80)
