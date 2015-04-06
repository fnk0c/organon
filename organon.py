#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "Fnkoc"
__VERSION__	= "0.1.8"
__DATE__	= "12/03/2015"

import sys
import argparse
import os

white = "\33[1;37m"
default = "\33[1;00m"

banner = """%s
   
   ████▄ █▄▄▄▄   ▄▀  ██      ▄   ████▄    ▄   
   █   █ █  ▄▀ ▄▀    █ █      █  █   █     █  
   █   █ █▀▀▌  █ ▀▄  █▄▄█ ██   █ █   █ ██   █ 
   ▀████ █  █  █   █ █  █ █ █  █ ▀████ █ █  █ 
           █    ███     █ █  █ █       █  █ █ 
          ▀            █  █   ██       █   ██ 
                      ▀                       
%s""" % (white, default)

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
parser.add_argument("--clean", action = "store_true",
	help = "Clean Organon\'s cache")

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
			os.system("ruby src/DB/database_connector.rb install \"SELECT url, dependencias, nome FROM programas WHERE nome LIKE '%s'\"" % package)
			os.system("python src/installer.py %s" % package)
			try: os.system("mv %s* cache/" % package)
			except:	pass

	elif args.r:
		for package in args.r:
			os.system("src/uninstall_%s.*" % package)

	elif args.s:
		print(args.s)
		result = os.system("ruby src/DB/database_connector.rb list \"SELECT nome, versao, descricao FROM programas WHERE nome LIKE '%s'\"" % args.s)

	elif args.l:
		os.system("ruby src/DB/database_connector.rb list \"SELECT nome, versao, descricao FROM programas\"")

	elif args.version:
		print(__VERSION__)

	elif args.about:
		os.system("cat README.md | more")

	elif args.clean:
		os.system("rm -rf cache/*")
