#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of 
#Hydra on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"27/12/2014"

import os

comandos = [
	"cd thc-hydra && ./configure && make && sudo make install"]

for a in comandos:
	os.system(a)

print("\n\n")
print("-"*80)
print("\n All clear\n Enjoy!")
print("""
  write \"hydra\" without the quotes on your terminal
  and hit ENTER to run the application
""")
print("-"*80)
