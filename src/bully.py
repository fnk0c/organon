#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of 
#BUlly on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"06/02/2015"

import os

comandos = [
   "tar xpvf bully-1.0.22-1-x86_64.pkg.tar.xz",
   "sudo mkdir /opt/bully",
   "sudo mv bully-1.0.22-1-x86_64.pkg/usr/bin/bully /opt/bully",
   "./generator.py bully sh bully"]

for a in comandos:
	os.system(a)

print("\n\n")
print("-"*80)
print("\n All clear\n Enjoy!")
print("""
  write \"bully\" without the quotes on your terminal
  and hit ENTER to run the application
  bully can be found at /opt
""")
print("-"*80)
