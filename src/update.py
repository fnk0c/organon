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

import abdala
import atom
from database import connect
from colors import *
from subprocess import check_call

class xereca(object):
	def __init__(self, ver3):
		self.ver3 = ver3

	def tools(self):
		pkgs = abdala.local(self.ver3).listing()
		for i in pkgs:
			print(green + " [+]" + default + " Attemping to update %s" % i[0])
			if i[1] == "git":
				path = "/usr/share/%s" % i[0]
				check_call("cd %s && sudo git pull" % path, shell = True)
			else:
				ver = connect(self.ver3).dependencies(i[0], True)
				if ver == i[1]:
					print("Already up to date")
				else:
					atom.actions(self.ver3).uninstall(i, False, False, True)
					atom.actions(self.ver3).install(i, True)

	def organon(self):
		print(green + "[+] Updating Organon" + default)
		try:
			check_call("git reset --hard && git pull", shell = True)
			print(" [+] Organon was successfully updated")
		except Exception:
			print(" [-] Couldn\'t retrieve update. Please download the latest \
version from https://github.com/fnk0c/organon")
			exit()
