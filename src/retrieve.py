#!/usr/bin/python
#coding=utf-8

#This script makes part of Organon Project
#https://github.com/fnk0c/organon

__AUTHOR__ 	= "Fnkoc"
__DATE__ = "28/12/2015"

"""
	Copyright (C) 2015  Franco Colombino & Ygor Máximo

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""

from re import findall
from subprocess import check_call, CalledProcessError
from colors import *

class download(object):
	def __init__(self, pkg_name, distro, arch):
		self.pkg_name = pkg_name
		self.distro = distro
		self.arch = arch

	def get_mirror(self):
		with open("/etc/organon/mirrors", "r") as mirror:
			mirror = mirror.readline()
			mirror = mirror.replace("\n", "")

		self.mirror = mirror
		self.src_mirror = mirror + "mirror/source/" + self.arch + "/"
		self.pkg_mirror = mirror + "mirror/" + self.distro + "/pkgconfig/"

	def get_files(self):
		src = self.src_mirror + self.pkg_name + ".tar.gz"
		pkg = self.pkg_mirror + self.pkg_name + ".conf"
		print(src)

		try:
			command = "sudo wget -c -P /var/cache/organon %s" % src
			check_call(command, shell = True)
		except (Exception, CalledProcessError, FileNotFoundError):
			command = command.replace("x86_64", "any").replace("x86", "any")
			print(command)
			check_call(command, shell = True)

		check_call("sudo wget -N -c -P /var/cache/organon %s" % pkg, shell = True)

	def sync(self):
#		command = "sudo rsync -Cravzp %sdb/tools.db /etc/organon/" % self.src_mirror
		command = "sudo wget -N -P /etc/organon/ %smirror/%s/tools.db" % (self.mirror, self.distro)
		check_call(command, shell = True)

#class install(download):
class install(object):
	#Template used to do the install
	script_template = \
"""#!/bin/bash

#Copy organon to /usr/share
cp -R /var/cache/organon/pkgname /usr/share/

echo \#\!/bin/bash >> /usr/bin/pkgname
echo cd /usr/share/pkgname >> /usr/bin/pkgname
echo exec python pkgname.py \"\$\@\" >> /usr/bin/pkgname

chmod +x /usr/bin/pkgname
chmod 777 /usr/share/pkgname
"""
	link_template = \
"""#!/bin/bash

#Copy organon to /usr/share
cp -R /var/cache/organon/pkgname /usr/share

ln -s /usr/share/pkgname/pkgname /usr/bin/pkgname
"""
	#Store extension
	EXT = {
	"python":"py",
	"ruby":"rb",
	"sh":"sh",
	"php":"php",
	"perl":"pl",
	}

	def __init__(self, pkg_name, ver3):
		self.pkg_name = pkg_name
		self.ver3 = ver3

	def read(self):
		with open("/var/cache/organon/%s.conf" % self.pkg_name, "r") as pkg_content:
			self.pkg_content = pkg_content.read()
		
		#convert string to list
		pkgconfig = self.pkg_content.split()
		
		#Find variables and its values
		version = pkgconfig.index("version")
		self.version = pkgconfig[version + 2]
		installer = pkgconfig.index("installer")
		self.installer = pkgconfig[installer + 2]


		#retrieve compile/extraction process
		process_b = self.pkg_content.find("{")
		process_e = self.pkg_content.find("}")
		process = self.pkg_content[process_b + 1:process_e]
		self.process = process.split("\n")
		
		
		self.deps = findall("dependencies = (.*)", self.pkg_content)
		
	def install_deps(self, distro):
		import database
		
		db = database.connect(self.ver3)
		deps = db.dependencies(self.pkg_name)

		if distro == "arch":
			manager = "sudo pacman -S "
		elif distro == "debian":
			manager = "sudo apt-get install "
		
		check_call(manager + deps)
