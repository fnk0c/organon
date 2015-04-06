#!/usr/bin/python

__AUTHOR__ 	= "Fnkoc"
__DATE__	= "Mimi\'s day 2015"		#12/03/2015

import sys
import os
import re

package_name = sys.argv[1]

pkg = open(package_name + ".conf", "r")				#Open config file

for a in pkg:
	if re.match("(.*)(T|t)ype(.*)", a):
		a = a.replace("type =", "").lower()
pkg.close()

pkg = open(package_name + ".conf", "r")				#Open config file

#Get install instructions
pkg_read = pkg.read()
start = pkg_read.index("{")	+ 1			#Get string location
end = pkg_read.index("}")
config = pkg_read[start:end]			#Use only range deffined on "start" and "end"
config = config.replace("\"", "").replace("\n", "").replace("\t", "")

commands = config.split(",")			#Split using comma as reference

bash = []								#Keep pkg data

for b in commands:
	bash.append(b)						#Write pkg data to bash list
#end

#Check if program needs a install script
if "True" in pkg_read:
	install = True
else:
	install = False

pkg.close()
#end

#Generate shell script to install
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
		lang = "python"
		exe = ".py"
	elif "perl" in a:
		lang = "perl"
		exe = ".pl"
	elif "ruby" in a:
		lang = "ruby"
		exe = ".rb"
	elif "exec" in a:
		os.system("sudo ln -s /opt/%s/%s /usr/bin" % (package_name, package_name))
		exit()
	elif "php" in a:
		lang = "php"
		exe = ".php"

	os.system("cd src/ && python generator.py %s %s %s" % (lang, package_name, package_name + exe))
	os.system("rm pkgconfig.sh %s.conf" % package_name)
