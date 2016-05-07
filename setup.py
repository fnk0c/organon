#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "Fnkoc"

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

def install():
	if path.isfile("/etc/apt/sources.list"):
		distro = "debian"
		command = "sudo apt-get install unrar unzip wget"

	elif path.isfile("/etc/pacman.conf"):
		distro = "arch"
		command = "sudo pacman -S unrar unzip wget"

	elif path.isfile("/etc/yum.conf"):
		distro = "fedora"
		command = "sudo yum install unrar unzip wget"

	try:
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

		print(" [+] creating configuration file")
		with open("organon.conf", "w") as conf:
			conf.write("distro = %s" % distro)
			conf.write("\narch = %s" % machine())
	
		check_call("sudo mkdir /etc/organon && sudo mv organon.conf /etc/organon && sudo touch /etc/organon/installed.db", shell = True)
		check_call("sudo cp etc/mirrors /etc/organon", shell = True)

		print(" [+] Installing MAN page")
		check_call("sudo install -Dm644 doc/organon.8 /usr/share/man/man8/", \
		shell = True)
		print(" [+] Creating organon\'s cache")
		check_call("sudo mkdir /var/cache/organon", shell = True)
		print(" [+] Moving organon to /usr/share")
		check_call("sudo mv ../organon /usr/share", shell = True)
		print(" [+] Installing dependencies")
		check_call(command, shell = True)
	
	except (CalledProcessError, KeyboardInterrupt) as e:
		print(" [!] ainn. Something went wrong")
		print(e)
		exit()

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
