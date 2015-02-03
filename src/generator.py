#!/usr/bin/python
#coding=utf-8

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"03/02/2015"

#This script generates a shell script used to create executables
#move directories and others things

import sys
import os

prog = sys.argv[1]
tipo = sys.argv[2]
nome = sys.argv[3]

def generator(prog):
	installer = open("installer.sh", "w")

	with open("installer_base.txt", "r") as log:
		log = log.readlines()
		for l in log:
			l = l.replace("organon.py", nome).replace("organon", prog).replace("python", tipo)
			installer.write(l)

		installer.close()

	os.system("sudo ./installer.sh")

generator(prog)

os.system("rm installer.sh")
