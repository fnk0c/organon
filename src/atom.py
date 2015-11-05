#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "Fnkoc"
__VERSION__	= "0.2.1"
__DATE__	= "13/10/2015"

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

import os
import database		#Retrieve database data
import retrieve		#Retrieve source files and pkgconfig
from colors import *

class actions(object):
	def __init__(self, ver3, distro, arch):
		self.ver3 = ver3
		self.distro = distro
		self.arch = arch

	# UPDATE ORGANON ###########################################################
	def update(self):
		print(colors.green + "[+] Updating Organon" + colors.default)
		up = os.system("git fetch && git pull")

		if up != 0:
			print(" [-] Couldn\'t retrieve update. Please download the latest \
version from https://github.com/fnk0c/organon")
		else:
			print(" [+] Organon was successfully updated")

	#CHECK IF PATH IS /USR/SHARE/ORGANON
	#THIS CHECK HAPPENS BECAUSE WHEN YOU RUN ./INSTALL.SH THE SCRIPT IS MOVED 
	#TO /USR/SHARE/. INSTALL.SH ALSO INSTALL ALL DEPENDENCIES NEEDED, CREATE 
	#THE SYMBOLICS LINKS AND .cache DIRECTORY
	def check_install(self):
#		if self.ver3 == True:
		try: raw_input
		except: raw_input = input

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

	def install(self, pkgs):
		#PYTHON 2 AND 3 SUPPORT
		if self.ver3 == False:
			pass
		elif self.ver3 == True:
			raw_input = input

		#RESUME ACTIONS TO BE DONE
		print("\n Packages (" + str(len(pkgs)) + ") " + " ".join(pkgs))
		choice = raw_input("\n %s[+]%s Continue the installation? [Y/n] " % \
		(green, default)).lower()

		# CHECK IF USER WANT TO CONTINUE
		if choice != "y" and len(choice) != 0:
			print(" [-] Aborted")
			exit()
		elif choice == "y" or len(choice) == 0:
			for package in pkgs:
				# CHECK IF ALREADY INSTALLED
				if package in os.listdir("/usr/bin"):
					print(" [!] %s already installed" % package)
				elif package in os.listdir("/usr/local/bin"):
					print(" [!] %s already installed" % package)
				else:
					#call module responsable to download package
					down = retrieve.download(package, self.distro, self.arch)
					#define server to be used
					down.get_mirror()
					#download source em pkgconfig
					down.get_files()
						

	def uninstall(self, pkgs, config, dep):
		if self.ver3 == True:
			raw_input = input

		print("\n Packages (" + str(len(pkgs)) + ") " + " ".join(pkgs))
		choice = raw_input("\n [+] Remove these packages? [Y/n] ").lower()

		# CHECK IF USER WANT TO CONTINUE #######################################
		if choice != "y" and len(choice) != 0:
			print(" [-] Aborted")
			exit()

		else:
			# REMOVE PROCESS ###################################################
			for package in pkgs:
				print(" [+] Deleting %s source files..." \
% package)
				try:
					if package in os.listdir("/usr/share"):
						os.system("sudo rm -rf /usr/share/%s" % package)
					elif package in os.listdir("/usr/local/share"):
						os.system("sudo rm -rf /usr/local/share/%s" % package)
					elif package in os.listdir("/opt"):
						os.system("sudo rm -rf /opt/%s" % package)
					elif package in os.listdir("/usr/bin"):
						os.system("sudo rm -rf /usr/bin/%s" % package)
					else:
						print(" [-] %s doesn\'t seem to be installed" % package)
				except Exception as e:
					print(e)

				print(" [+] Deleting symlink...")
				try:
					if package in os.listdir("/usr/bin"):
						os.system("sudo rm -rf /usr/bin/%s" % package)
					elif package in os.listdir("/usr/local/bin"):
						os.system("sudo rm -rf /usr/local/bin/%s" % package)
				except Exception as e:
					print(e)

				if config == True:
					if package in os.listdir("/etc/"):
						print(" [+] Removing configuration files...")
						os.system("sudo rm -rf /etc/%s" % package)
					else:
						print(" [!] No configuration file found")

				if dep == True:
					print(" [+] Removing dependencies...")

	def enum_db(self):
		#Since organon is hosted on a Dynamic IP server. We need to get its
		#IP address everytime we run it
		db = database.connect("http://organon.ddns.net", self.ver3)
		db.ip_retriever()
		db.MySQL("SELECT nome, versao, descricao FROM %s" % self.distro)

	def search_db(self, keyword):
		query = ("\
SELECT * FROM table WHERE \
(CONVERT( nome USING utf8 ) \
LIKE '%create%' OR \
CONVERT( versao USING utf8 ) \
LIKE '%create%' OR \
CONVERT( descricao USING utf8) \
LIKE '%create%' OR \
CONVERT( url USING utf8 ) \
LIKE '%create%' OR \
CONVERT( dependencias  USING utf8 ) \
LIKE '%create%') LIMIT 0, 30").replace("create", keyword).replace("table", self.distro)

		print(" [+] Searching for: " + keyword)
		db = database.connect("http://organon.ddns.net", self.ver3)
		db.ip_retriever()
		db.MySQL(query)
