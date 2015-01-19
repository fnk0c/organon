#!/usr/bin/python
#coding=utf-8

import sys
sys.path.append("src/")
import argparse
import os

parser = argparse.ArgumentParser(description = "Package manager that focus on Pentest")
parser.add_argument("-i", nargs = "+",
	help = "Install packages")
parser.add_argument("-r", nargs = "+",
	help = "Remove packages")
parser.add_argument("-s",
	help = "Search for package")
parser.add_argument("-l", action = "store_true",
	help = "List all packages available")

args = parser.parse_args()

if len(sys.argv) == 1:
	os.system("clear")
	parser.print_help()

else:
	if args.i:
		for package in install:
			os.system("src/%s.*" % package)

	elif args.r:
		print("remove")

	elif args.s:
		print args.s
		result = db_content.action("SELECT nome, versao, descricao FROM programas WHERE nome LIKE '%s'" % args.s)

	elif args.l:
		db_content.action("SELECT nome, versao, descricao FROM programas")
