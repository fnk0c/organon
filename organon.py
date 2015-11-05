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
parser.add_argument("--dependencies", action = "store_true",
	help = "Remove dependencies (use with -r)")
parser.add_argument("--config", action = "store_true",
	help = "Remove configuration files (use with -r)")
parser.add_argument("-u", action = "store_true",
	help = "Update Organon")
parser.add_argument("-s",
	help = "Search for package")
parser.add_argument("-l", action = "store_true",
	help = "List all packages available")
parser.add_argument("--clean", action = "store_true",
	help = "Clean Organon\'s cache")

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
#	core.check_install()
	
	### - OPEN MAN PAGE - ###
	if args.about:
		system("man organon")
	
	### - RETURN VERSION - ###
	if args.version:
		print("Version: ", __VERSION__)
		print("Last revision", __DATE__)

	### - UPDATE ORGANON - ###
	if args.u:
		core.update()

	### - INSTALL PROGRAM - ###
	elif args.i:
		core.install(args.i)

	### - REMOVE PROGRAM - ###
	elif args.r:
		config = False
		deps = False
		if args.config == True and args.dependencies == True:
			config = True
			deps = True

		elif args.config == True and args.dependencies == False:
			config = True
			deps = False

		elif args.config == False and args.dependencies == True:
			config = False
			deps = True

		core.uninstall(args.r, config, deps)

	### - LISTA DATABASE - ###
	elif args.l:
		core.enum_db()

	### - SEARCH IN DATABASE - ###
	elif args.s:
		core.search_db(args.s)

if __name__ == "__main__":
	if len(argv) == 1:
		system("clear")
		print(banner)
		parser.print_help()
	else:
		with open("/etc/organon/organon.conf", "r") as conf:
			conf = conf.readlines()
			distro = conf[0].split("=")[1].replace("\n", "").replace(" ", "")
			arch = conf[1].split("=")[1].replace("\n", "").replace(" ", "")
		py_version()
		main()
