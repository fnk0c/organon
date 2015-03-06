#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "Fnkoc"
__VERSION__	= "0.1.7"
__DATE__	= "06/03/2015"

import sys
import argparse
import os

banner = """
   
   ████▄ █▄▄▄▄   ▄▀  ██      ▄   ████▄    ▄   
   █   █ █  ▄▀ ▄▀    █ █      █  █   █     █  
   █   █ █▀▀▌  █ ▀▄  █▄▄█ ██   █ █   █ ██   █ 
   ▀████ █  █  █   █ █  █ █ █  █ ▀████ █ █  █ 
           █    ███     █ █  █ █       █  █ █ 
          ▀            █  █   ██       █   ██ 
                      ▀                       
"""

parser = argparse.ArgumentParser(description = "Package manager that focus on Pentest tools")
parser.add_argument("-a", "--about", action = "store_true",
	help = "About this tool")
parser.add_argument("-v", "--version", action = "store_true",
	help = "Show version and exit")
parser.add_argument("-i", nargs = "+",
	help = "Install packages")
parser.add_argument("-r", nargs = "+",
	help = "Remove packages")
parser.add_argument("-u", action = "store_true",
	help = "Update Organon")
parser.add_argument("-s",
	help = "Search for package")
parser.add_argument("-l", action = "store_true",
	help = "List all packages available")

args = parser.parse_args()

if len(sys.argv) == 1:
	os.system("clear")
	print(banner)
	parser.print_help()

else:
	if args.u:
		os.system("git fetch && git pull")

	elif args.i:
		for package in args.i:
			os.system("ruby src/DB/database_connector.rb install \"SELECT url, dependencias FROM programas WHERE nome LIKE '%s'\"" % package)

			for a in args.i:		
				os.system("src/%s.*" % a)

	elif args.r:
		for package in args.r:
			os.system("src/%s.*" % package)

	elif args.s:
		print(args.s)
		result = os.system("ruby src/DB/database_connector.rb list \"SELECT nome, versao, descricao FROM programas WHERE nome LIKE '%s'\"" % args.s)

	elif args.l:
		os.system("ruby src/DB/database_connector.rb list \"SELECT nome, versao, descricao FROM programas\"")

	elif args.version:
		print(__VERSION__)

	elif args.about:
		os.system("cat README.md | more")
