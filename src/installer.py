#!/usr/bin/python

#This script makes part of Organon Project
#https://github.com/maximozsec/organon
#LAST UPDATE = 03/06/15


__AUTHOR__ 	= "Fnkoc"
__DATE__	= "Mimi\'s day 2015"		#12/03/2015

import sys
import os
import re

#Get argument
package_name = sys.argv[1]

#The following function generates the shell script responsable of tool instalation
#It uses installer_base.txt as template.
def generator(lang, package_name, prog):
	installer = open("src/installer.sh", "w")
	
	#Read txt template
	with open("src/installer_base.txt", "r") as base:
		base = base.readlines()
		for l in base:
			#Replace key words
			l = l.replace("organon.py", prog).replace("organon", package_name).replace("python", lang)
			installer.write(l)

	installer.close()
	os.system("sudo sh src/installer.sh")
	os.system("rm src/installer.sh")


################################################################################
#Generate Shell Script to compile

#Open config file
pkg = open(package_name + ".conf", "r")

for a in pkg:
	#Searchs for "type"
	if re.match("(.*)(T|t)ype(.*)", a):
		a = a.replace("type =", "").lower()
pkg.close()

#Open config file
pkg = open(package_name + ".conf", "r")

#Get install instructions
pkg_read = pkg.read()
start = pkg_read.index("{")	+ 1		#Get string location
end = pkg_read.index("}")
config = pkg_read[start:end]		#Use only range defined on "start" and "end"
config = config.replace("\"", "").replace("\n", "").replace("\t", "")

commands = config.split(",")		#Split using comma as reference

bash = []							#Keep pkg data

for b in commands:
	bash.append(b)					#Write pkg data to bash list
#end

#Check if program needs a install script
if "True" in pkg_read:
	install = True
else:
	install = False

pkg.close()
#end

#Generate shell script to compile
with open("pkgconfig.sh", "w") as l:
	l.write("#!/bin/bash\n\n")
	l.write("#This file is generated automatically by installer.py\n\n")
	for c in bash:
		l.write(str(c) + "\n")
	l.write("\n#End")
#End

#Exec shell script
os.system("sh pkgconfig.sh")

if install == True:
	if "python3" in a:
		lang = "python3"
		exe = ".py"
	elif "python" in a:
		lang = "python2"
		exe = ".py"
	elif "perl" in a:
		lang = "perl"
		exe = ".pl"
	elif "ruby" in a:
		lang = "ruby"
		exe = ".rb"
	elif "php" in a:
		lang = "php"
		exe = ".php"

	prog = package_name + exe
	generator(lang, package_name, prog)
os.system("rm pkgconfig.sh %s.conf" % package_name)
