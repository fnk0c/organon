#!/usr/bin/python
#coding=utf-8

#This script makes part of Organon Project
#https://github.com/fnk0c/organon

__AUTHOR__ 	= "Fnkoc"

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

from os import chdir
from re import findall
from subprocess import check_call, CalledProcessError

from colors import *

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
		self.pkg_mirror = mirror + "mirror/" + self.distro + "/" + self.arch + "/pkgconfig/"

	def pkgconfig(self):
		#Download source files of programs
		
		import database
		
		db = database.connect(self.ver3)
		server_pkgname = db.server_pkgname(self.pkg_name)
		
		pkg = self.pkg_mirror + self.pkg_name + ".conf"

		check_call("sudo wget -N -c -P /var/cache/organon %s" % pkg, shell = True)
		return(server_pkgname)

	def source(self, url):
		if "github" in url:
			command = "cd /var/cache/organon/ ; sudo git clone %s" % url
		else:
			command = "sudo wget -N -c -P /var/cache/organon %s" % url
		try:
			check_call(command, shell = True)
		except Exception as e:
			pass

	def sync(self):
		#Sync local database with server's database
		command = "sudo wget -N -P /etc/organon/ %smirror/%s/%s/tools.db" % (self.mirror, self.distro, self.arch)
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
		arch = pkgconfig.index("arch")
		self.arch = pkgconfig[arch + 2]
		source = pkgconfig.index("source")
		self.source = pkgconfig[source + 2]

		try:
			Type = pkgconfig.index("type")
			self.Type = pkgconfig[Type + 2]
		except ValueError:
			pass

		#retrieve compile/extraction process
		process_b = self.pkg_content.find("{")
		process_e = self.pkg_content.find("}")
		process = self.pkg_content[process_b + 1:process_e]
		process = process.split("\n")
		return(self.source, process, self.version)		
	def install_deps(self, distro, force_yes):
		import database
		
		db = database.connect(self.ver3)
		deps = db.dependencies(self.pkg_name)
		
		if deps != "NULL":
			if distro == "arch":
				if force_yes == True:
					manager = "sudo pacman --needed --noconfirm -S "
				else:
					manager = "sudo pacman --needed -S "
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
		else:
			pass

	def make(self, server_pkgname, process):
		if self.version == "git":
			check_call("cp -Rf /var/cache/organon/%s /tmp" % \
			server_pkgname, shell = True)

		elif server_pkgname[-3:] == "rar":
			check_call("unrar e /var/cache/organon/%s /tmp" % \
			server_pkgname, shell = True)

		elif server_pkgname[-3:] == "zip":
			check_call("unzip /var/cache/organon/%s -d /tmp/%s" % \
			(server_pkgname, self.pkg_name), shell = True)

		elif server_pkgname[-3:] == "run":
			check_call("sudo chmod +x /var/cache/organon/%s" % \
			server_pkgname, shell = True)
			check_call("sudo /var/cache/organon/%s" % server_pkgname, \
			shell = True)
			exit()

		else:
			check_call("tar -xvf /var/cache/organon/%s -C /tmp" % \
			server_pkgname, shell = True)

		with open("/tmp/%s.sh" % self.pkg_name, "w") as shell:
			shell.write("#!/bin/bash\n\n")
			shell.write("if [ \"%s\" != \"%s\" ]\n" % (server_pkgname, self.pkg_name))
			shell.write("then\n")
			shell.write("\tmv /tmp/%s /tmp/%s\n" % (server_pkgname.\
			replace(".tar.gz", "").\
			replace(".tar.bz2", "").\
			replace(".rar", "").\
			replace(".zip", ""), self.pkg_name))
			shell.write("else\n\tcontinue\nfi\n")
			

			shell.write("cd /tmp/%s\n" % self.pkg_name)
			for command in process:
				if command == "":
					pass
				else:
					shell.write(str(command) + "\n")
		check_call("sh /tmp/%s.sh" % self.pkg_name, shell = True)

	def symlink(self):
		if self.installer == "none":
			pass
		elif self.installer == "script":
			#Template used to do the install
			script_template = \
"""#!/bin/bash

#Copy organon to /usr/share
rm /tmp/pkgname.sh
sudo cp -R /tmp/pkgname /usr/share/

echo '#!/bin/bash' | sudo tee --append /usr/bin/pkgname
echo 'cd /usr/share/pkgname' | sudo tee --append /usr/bin/pkgname
echo 'exec python pkgname.py $@' | sudo tee --append /usr/bin/pkgname

sudo chmod +x /usr/bin/pkgname
sudo chmod 777 /usr/share/pkgname
"""

			ext = {
"python3":"py",
"python2":"py",
"python":"py",
"ruby":"rb",
"bash":"sh",
"php":"php",
"perl":"pl"}

			with open("/tmp/install_%s.sh" % self.pkg_name, "w") as symlink:
				symlink.write(script_template.replace("pkgname", self.pkg_name)\
				.replace("python", self.Type).replace(".py", ".%s" % ext[self.Type]))

		elif self.install == "symlink":
			link_template = \
"""#!/bin/bash

#Copy organon to /usr/share
cp -R /tmp/pkgname /usr/share

ln -s /usr/share/pkgname/pkgname* /usr/bin/pkgname
"""

			with open("/tmp/install_%s.sh" % self.pkg_name, "w") as symlink:
				symlink.write(link_template)
		
		try:
			check_call("sh /tmp/install_%s.sh" % self.pkg_name, shell = True)
		except Exception:
			pass
