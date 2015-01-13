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
	install = args.i
	remove = args.r
	search = args.s
	listar = args.l

	if install:
		for package in install:
			os.system("src/%s.*" % package)
	elif remove:
		print("remove")
	elif search:
		print("search")
	elif listar:
		print("list")
