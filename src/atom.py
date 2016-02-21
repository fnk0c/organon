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

import database		#Retrieve database data
import retrieve		#Retrieve source files and pkgconfig
from colors import *
from subprocess import check_call
from os import listdir

class actions(object):
	def __init__(self, ver3, distro, arch):
		self.ver3 = ver3
		self.distro = distro
		self.arch = arch

	# UPDATE ORGANON ###########################################################
	def update_organon(self):
		print(green + "[+] Updating Organon" + default)
		try:
			check_call("git reset --hard && git fetch && git pull")
			print(" [+] Organon was successfully updated")
		except Exception:
			print(" [-] Couldn\'t retrieve update. Please download the latest \
version from https://github.com/fnk0c/organon")
			exit()

	def update_packages(self):
		print("coming soon")

	def check_install(self):
		#CHECK IF PATH IS /USR/SHARE/ORGANON
		if self.ver3 == True:
			raw_input = input

		if os.getcwd() != "/usr/share/organon":
			from time import sleep
		
			os.system("clear")
			print(red + "\n\n\t >> OPS! <<\n\n")
			print(" [!] Did you run install.sh?\n Please run \'./install.sh\' \
to install dependencies and configure Organon" + default)
			sleep(3)

		if os.getuid() == 0:
			print("\n [WARNING] You're not supposed to run Organon as root")
			choice = raw_input(" [!] Continue? [y/N] ").lower()
			if choice == "y":
				pass
			else:
				exit()

	def install(self, pkgs, force_yes):
		#PYTHON 2 AND 3 SUPPORT
		if self.ver3 == True:
			raw_input = input

		if force_yes != True:
			# RESUME ACTIONS TO BE DONE
			try:
				print("\n Packages (" + str(len(pkgs)) + ") " + " ".join(pkgs))
				choice = raw_input("\n %s[+]%s Continue the installation? [Y/n] " % \
				(green, default)).lower()
			except KeyboardInterrupt:
				print(" [-] Aborted")
				exit()
		else:
			choice = "y"

		# CHECK IF USER WANT TO CONTINUE
		if choice != "y" and len(choice) != 0:
			print(" [-] Aborted")
			exit()
		elif choice == "y" or len(choice) == 0:
			for package in pkgs:
				# CHECK IF ALREADY INSTALLED
				if package in listdir("/usr/bin"):
					print(" [!] %s already installed" % package)
				elif package in listdir("/usr/local/bin"):
					print(" [!] %s already installed" % package)
				else:
					#call module responsable to download package
#					down = retrieve.download(package, self.distro, self.arch, self.ver3)
					#define server to be used
#					down.get_mirror()
					#download source em pkgconfig
#					server_pkgname = down.get_files()

					install = retrieve.install(package, self.ver3)
					install.read()
					install.install_deps(self.distro, force_yes)
#					install.make(server_pkgname)
					install.symlink()

	def uninstall(self, pkgs, config, dep, force_yes):
		if self.ver3 == True:
			raw_input = input

		if force_yes != True:
			try:
				print("\n Packages (" + str(len(pkgs)) + ") " + " ".join(pkgs))
				choice = raw_input("\n [+] Remove these packages? [Y/n] ").lower()
			except KeyboardInterrupt:
				print("\n [-] Aborted")
				exit()
		else:
			choice = "y"

		# CHECK IF USER WANT TO CONTINUE #######################################
		if choice != "y" and len(choice) != 0:
			print(" [-] Aborted")
			exit()

		elif choice == "y" or len(choice) == 0:
			# REMOVE PROCESS ###################################################
			for package in pkgs:
				print(" [+] Deleting %s source files...")

	def sync_db(self):
		sync = retrieve.download(None, self.distro, self.arch, self.ver3)
		sync.get_mirror()
		sync.sync()

	def enum_db(self):
		database.connect(self.ver3).listing()

	def search_db(self, keyword):
		print(green + " [+] " + default + "Searching for: " + keyword)
		database.connect(self.ver3).search(keyword)
