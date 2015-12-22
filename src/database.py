#!/usr/bin/python
#coding=utf-8

import csv
from colors import *

class connect(object):
	def listing(self):
		with open("/etc/organon/tools.db", "r") as csvfile:
			csvcontent = csv.reader(csvfile, delimiter=";")

			for row in csvcontent:
				print(green + " [+] " + row[0] + yellow + " v" + row[1] + default)
				print(row[4] + "\n")
	
	def search(self, keyword):
		with open("/etc/organon/tools.db", "r") as csvfile:
			csvcontent = csv.reader(csvfile, delimiter=";")

			for row in csvcontent:
				if keyword in row[0]:
					print(green + " [+] " + row[0] + yellow + " v" + row[1] + default)
					print(row[4] + "\n")
				elif keyword in row[1]:
					print(green + " [+] " + row[0] + yellow + " v" + row[1] + default)
					print(row[4] + "\n")
				elif keyword in row[2]:
					print(green + " [+] " + row[0] + yellow + " v" + row[1] + default)
					print(row[4] + "\n")
				elif keyword in row[3]:
					print(green + " [+] " + row[0] + yellow + " v" + row[1] + default)
					print(row[4] + "\n")
				elif keyword in row[4]:
					print(green + " [+] " + row[0] + yellow + " v" + row[1] + default)
					print(row[4] + "\n")
