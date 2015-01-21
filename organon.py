#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "Fnkoc"
__VERSION__	= "0.1.3"
__DATE__	= "21/01/2015"

import sys
sys.path.append("src/DB")
import db_content
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
		for package in args.i:
			db_content.install("SELECT url, dependencias FROM programas WHERE nome LIKE '%s'" % package)
		
		args.i = "".join(args.i)
		print("src/%s" % args.i)		
		os.system("src/%s.*" % args.i)

	elif args.r:
		print("remove")

	elif args.s:
		print args.s
		result = db_content.listar("SELECT nome, versao, descricao FROM programas WHERE nome LIKE '%s'" % args.s)

	elif args.l:
		db_content.listar("SELECT nome, versao, descricao FROM programas")
