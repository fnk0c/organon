#!/usr/bin/python
#coding=utf-8

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"03/02/2015"

#This script generates a shell script used to create symbolic links
#move directories and others things

import sys
import os

lang = sys.argv[1]
pkgname = sys.argv[2]
prog = sys.argv[3]

def generator(prog):
	installer = open("installer.sh", "w")

	with open("installer_base.txt", "r") as log:
		log = log.readlines()
		for l in log:
			l = l.replace("organon.py", prog).replace("organon", pkgname).replace("python", lang)
			installer.write(l)

		installer.close()

	installer.close()
	os.system("sudo sh installer.sh")

generator(prog)

os.system("rm installer.sh")
