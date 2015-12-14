#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "Fnkoc"
__VERSION__	= "0.2.1"
__DATE__	= "30/10/2015"

"""
	Copyright (C) 2015  Franco Colombino

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

	(https://github.com/fnk0c/organon)
"""

from sys import version, argv
from os import path, getuid
from subprocess import check_call, CalledProcessError
from platform import machine

dependencies = {
"arch2":["python2", "python2-pip"],
"debian2":["python", "python-pip"],
"arch3":["python", "python-pip"],
"debian3":["python3", "python3-pip"]
}

py_version = {
3:[dependencies["arch3"], dependencies["debian3"]],
2:[dependencies["arch2"], dependencies["debian2"]],
}

distro = 0
arch = 0
debian = 1
ver2 = 2
ver3 = 3

def install():
	if path.isfile("/etc/apt/sources.list"):
		distro = "debian"
		manager = "sudo apt-get install "

		if "2" in version[0]:
			dep = str(py_version[ver2][debian]).replace("[", "")\
			.replace("]", "").replace(",", "")
		elif "3" in version[0]:
			dep = str(py_version[ver3][debian]).replace("[", "")\
			.replace("]", "").replace(",", "")

	elif path.isfile("/etc/pacman.conf"):
		distro = "arch"
		manager = "sudo pacman -S "

		# using wget cause urllib.request was not working 
		if "2" in version[0]:
			dep = str(py_version[ver2][arch]).replace("[", "").replace("]", "")\
			.replace(",", "")
		elif "3" in version[0]:
			dep = str(py_version[ver3][arch]).replace("[", "").replace("]", "")\
			.replace(",", "")

	#I could have used re.sub to replace the chars, but it doesn't seems to be a
	#great improve. Neither on layout nor in efficiency
	else:
		print("Installer not finished for this type os Linux.")
		print("Please, install the following dependencies:")
		for i in py_version[ver2][debian]:
			print("\t%s" % i)
		exit()
		
	try:
		command = manager + dep
		print(" [+] Installing dependencies")
		check_call(command, shell = True)
		check_call("sudo pip install -r requeriments.txt", shell = True)
		print(" [+] Installing MAN page")
		check_call("sudo install -Dm644 doc/organon.8 /usr/share/man/man8/", \
		shell = True)
		print(" [+] Creating organon\'s cache")
		check_call("sudo mkdir /var/cache/organon", shell = True)
		print(" [+] Moving organon to /usr/share")
		check_call("sudo mv ../organon /usr/share", shell = True)
		print(" [+] Creating symlink")

		with open("organon", "w") as symlink:
			symlink.write(\
"""
#!/bin/bash
			
cd /usr/share/organon
python organon.py $@""")

		check_call("sudo mv organon /usr/bin", shell = True)
		print(" [+] Changing permission")
		check_call("sudo chmod +x /usr/bin/organon", shell = True)
		print(" [+] Cleaning files")
	
	except (CalledProcessError, KeyboardInterrupt) as e:
		print(" [!] ainn. Something went wrong")
		print(e)
		exit()

	with open("organon.conf", "w") as conf:
		conf.write("distro = %s" % distro)
		conf.write("\narch = %s" % machine())
	
	check_call("sudo mkdir /etc/organon && sudo mv organon.conf /etc/organon", \
	shell = True)
	check_call("sudo cp etc/mirrors /etc/organon", shell = True)

def uninstall():
	check_call("sudo rm -rf /usr/share/organon /var/cache/organon /etc/organon\
	/usr/bin/organon", shell = True)

if __name__ == "__main__":
	if len(argv) == 1 or argv[1] == "help":
		print("Usage: python setup.py {install || uninstall}")
		exit()
	else:
		if getuid() == 0:
			print(getuid)
			print(" [!] Are you root? Please do NOT run this script as root")
			exit()
		else:
			if argv[1] == "install":
				if path.isfile("/usr/share/organon/organon.py"):
					print("Remove organon before continue")
					print("python setup.py uninstall")
				else:
					install()
			elif argv[1] == "uninstall":
				uninstall()
