#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "Fnkoc"
__VERSION__	= "0.2.6"
__DATE__	= "04/07/2016"

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

from sys import path, argv, version
from os import system
import argparse

path.append("src/")
import atom
from colors import *

# BANNER #######################################################################
banner = """%s
   
   ████▄ █▄▄▄▄   ▄▀  ██      ▄   ████▄    ▄   
   █   █ █  ▄▀ ▄▀    █ █      █  █   █     █  
   █   █ █▀▀▌  █ ▀▄  █▄▄█ ██   █ █   █ ██   █ 
   ▀████ █  █  █   █ █  █ █ █  █ ▀████ █ █  █ 
           █    ███     █ █  █ █       █  █ █ 
          ▀            █  █   ██       █   ██ 
                      ▀                       
%s""" % (white, default)

# ARGUMENTOS ###################################################################

parser = argparse.ArgumentParser(prog = "organon", description = "Package \
manager that focus on Pentest tools")
parser.add_argument("-a", "--about", action = "store_true",
	help = "About this tool")
parser.add_argument("-v", "--version", action = "store_true",
	help = "Show version and exit")
parser.add_argument("-i", nargs = "+",
	help = "Install packages")
parser.add_argument("-r", nargs = "+",
	help = "Remove packages")
parser.add_argument("--deps", action = "store_true",
	help = "Remove dependencies (use with -r)")
parser.add_argument("--conf", action = "store_true",
	help = "Remove configuration files (use with -r)")
parser.add_argument("-U", action = "store_true",
	help = "Update Organon")
parser.add_argument("-u", action = "store_true",
	help = "Update packages")
parser.add_argument("-S", action = "store_true",
	help = "Synchronize database")
parser.add_argument("-s",
	help = "Search for packages")
parser.add_argument("-L", action = "store_true",
	help = "List all packages available")
parser.add_argument("--clean", action = "store_true",
	help = "Clean Organon\'s cache")
parser.add_argument("--yes", action = "store_true",
	help = "Assume yes to all questions")
parser.add_argument("-Li", action = "store_true",
	help = argparse.SUPPRESS)

args = parser.parse_args()

# DETECTS PYTHON VERSION #######################################################

def py_version():
	global ver3

	if "2" in version[0]:
		ver3 = False
	elif "3" in version[0]:
		ver3 = True
	else:
		print("WTF Dude! Are you using Python?")
		exit()

def main():
	core = atom.actions(ver3, distro, arch)

	#Check if organon is correctly installed
	core.check_install()
	
	### - OPEN MAN PAGE - ###
	if args.about:
		system("man organon")
	
	### - RETURN VERSION - ###
	if args.version:
		print("Version: ", __VERSION__)
		print("Last revision", __DATE__)

	### - CLEAN ORGANON CACHE - ###
	if args.clean:
		print(" [!] Cleaning cache")
		system("sudo rm -rf /var/cache/organon/*")

	### - UPDATE ORGANON - ###
	if args.U:
		core.update_organon()

	### - UPDATE PACKAGES - ###
	if args.u:
		core.update_packages()

	### - INSTALL PROGRAM - ###
	elif args.i:
		core.install(args.i, args.yes)

	### - REMOVE PROGRAM - ###
	elif args.r:
		conf = False
		deps = False
		if args.conf == True and args.deps == True:
			conf = True
			deps = True

		elif args.conf == True and args.deps == False:
			conf = True
			deps = False

		elif args.conf == False and args.deps == True:
			conf = False
			deps = True

		core.uninstall(args.r, conf, deps, args.yes)

	### - SYNCHRONIZE DATABASE - ###
	elif args.S:
		core.sync_db()

	### - SEARCH IN DATABASE - ###
	elif args.s:
		core.search_db(args.s)

	### - LIST DATABASE - ###
	elif args.L:
		core.enum_db()
	
	### - LIST INSTALLED TOOLS - ###
	elif args.Li:
		core.installed()

if __name__ == "__main__":
	if len(argv) == 1:
		system("clear")
		print(banner)
		parser.print_help()
	else:
		try:
			with open("/etc/organon/organon.conf", "r") as conf:
				conf = conf.readlines()
				distro = conf[0].split("=")[1].replace("\n", "").replace(" ", "")
				arch = conf[1].split("=")[1].replace("\n", "").replace(" ", "")
		except FileNotFoundError:
			print(" [!] No configuration file found (/etc/organon/organon.conf")
			print("Did you installed organon?")
			print("python setup.py install")
			exit()
		py_version()
		
		try:
			main()
		except KeyboardInterrupt:
			print(red + "\n\n [!] User aborted" + default)
			exit()
		except Exception as e:
			print(red + str(e) + default)
			raise(e)
