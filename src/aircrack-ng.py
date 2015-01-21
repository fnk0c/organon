#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of 
#Aircrack-ng on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"13/12/2014"

import os

comandos = [
	"tar xpvf aircrack-ng-1.2-rc1.tar.gz",
	"cd aircrack-ng-1.2-rc1/ && make && sudo make install && sudo airodump-ng-oui-update"]

for a in comandos:
	os.system(a)

print("\n\n")
print("-"*80)
print("\n All clear\n Enjoy!")
print("""
  write \"sudo air\" without the quotes on your terminal
  and hit TAB twice to see all the applications installed
""")
print("-"*80)
