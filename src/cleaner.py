#!/usr/bin/python
#coding: utf-8

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

from subprocess import check_call
from os import listdir

class uninstall(object):
	def __init__(self, conf, deps, ver3):
		self.conf = conf
		self.deps = deps
		self.ver3 = ver3

	def pkg(self, package, distro):
		print(" [+] Deleting %s source files..." % package)

		if package in listdir("/usr/bin"):
			check_call("sudo rm -rf /usr/bin/%s" % package, shell = True)
			check_call("sudo rm -rf /usr/share/%s" % package, shell = True)
		elif package in listdir("/usr/local/bin"):
			check_call("sudo rm -rf /usr/local/bin/%s" % package, shell = True)
			check_call("sudo rm -rf /usr/local/share/%s" % package, shell = True)
		else:
			print(" [!] %s not installed" % package)
			exit()
		
		if self.conf == True:
			check_call("sudo rm -rf /etc/%s" % package, shell = True)
		if self.deps == True:
			import database

			deps = database.connect(self.ver3).dependencies(package)

			if distro == "arch":
				command = "sudo pacman -Rsn %s" % deps
			elif distro == "debian":
				command = " sudo apt-get remove %s" % deps
			elif distro == "fedora":
				command = "sudo yum remove %s" % deps
			check_call(command, shell = True)