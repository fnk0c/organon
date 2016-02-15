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
from os import chdir

class download(object):
	def __init__(self, pkg_name, distro, arch, ver3):
		self.pkg_name = pkg_name
		self.distro = distro
		self.arch = arch
		self.ver3 = ver3

	def get_mirror(self):
		#Opens /etc/organon/mirrors to get mirror address
		with open("/etc/organon/mirrors", "r") as mirror:
			mirror = mirror.readline()
			mirror = mirror.replace("\n", "")

		self.mirror = mirror
		self.src_mirror = mirror + "mirror/source/" + self.arch + "/"
		self.pkg_mirror = mirror + "mirror/" + self.distro + "/pkgconfig/"

	def get_files(self):
		#Download source files of programs
		
		import database
		
		db = database.connect(self.ver3)
		server_pkgname = db.server_pkgname(self.pkg_name)
		
		src = self.src_mirror + server_pkgname
		pkg = self.pkg_mirror + self.pkg_name + ".conf"

		try:
			command = "sudo wget -c -P /var/cache/organon %s" % src
			check_call(command, shell = True)
		except (Exception, CalledProcessError, FileNotFoundError):
			command = command.replace("x86_64", "any").replace("x86", "any")
			print(command)
			check_call(command, shell = True)

		check_call("sudo wget -N -c -P /var/cache/organon %s" % pkg, shell = True)

	def sync(self):
		#Sync local database with server's database
		command = "sudo wget -N -P /etc/organon/ %smirror/%s/tools.db" % (self.mirror, self.distro)
		check_call(command, shell = True)


class install(object):
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
		Type = pkgconfig.index("type")
		self.Type = pkgconfig[installer + 2]

		#retrieve compile/extraction process
		process_b = self.pkg_content.find("{")
		process_e = self.pkg_content.find("}")
		process = self.pkg_content[process_b + 1:process_e]
		self.process = process.split("\n")
		
	def install_deps(self, distro, force_yes):
		import database
		
		db = database.connect(self.ver3)
		deps = db.dependencies(self.pkg_name)

		if distro == "arch":
			if force_yes == True:
				manager = "sudo pacman --noconfirm -S "
			else:
				manager = "sudo pacman -S "
		elif distro == "debian":
			if force_yes == True:
				manager = "sudo apt-get -f install "
			else:
				manager = "sudo apt-get install "
		elif distro == "fedora":
			if force_yes == True:
				manager = "sudo yum -f install "
			else:
				manager = "sudo yum install "

		check_call(manager + deps, shell = True)

	def make(self):
		check_call("tar -xzvf /var/cache/organon/*%s*.tar.gz -C /tmp" % self.pkg_name, shell = True)

		with open("/tmp/%s.sh" % self.pkg_name, "w") as shell:
			shell.write("#!/bin/bash\n\n")
			shell.write("cd /tmp/%s*\n" % self.pkg_name)
			for command in self.process:
				if command == "":
					pass
				else:
					shell.write(command)
		check_call("sh /tmp/%s.sh" % self.pkg_name, shell = True)

	def symlink(self):
		if self.installer == "none":
			pass
		elif self.installer == "script":
			#Template used to do the install
			script_template = \
"""#!/bin/bash

#Copy organon to /usr/share
cp -R /tmp/pkgname /usr/share/

echo \#\!/bin/bash >> /usr/bin/pkgname
echo cd /usr/share/pkgname >> /usr/bin/pkgname
echo exec python pkgname.py \"\$\@\" >> /usr/bin/pkgname

chmod +x /usr/bin/pkgname
chmod 777 /usr/share/pkgname
"""

			ext = {
"python":"py",
"ruby":"rb",
"shell":"sh",
"php":"php",
"perl":"pl"}
			with open("/tmp/%s.sh" % self.pkg_name, "w") as symlink:
				symlink.write(script_template.replace("pkgname", self.pkg_name)\
				.replace("python", self.Type).replace(".py", ".%s"\
				 % ext[self.Type]))

		elif self.install == "symlink":
			link_template = \
"""#!/bin/bash

#Copy organon to /usr/share
cp -R /tmp/pkgname /usr/share

ln -s /usr/share/pkgname/pkgname* /usr/bin/pkgname
"""

			with open("/tmp/%s.sh" % self.pkg_name, "w") as symlink:
				symlink.write(link_template)
		
		try:
			check_call("sh /tmp/%s.sh" % self.pkg_name, shell = True)
		except Exception:
			pass
