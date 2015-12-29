#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "Fnkoc"
__VERSION__	= "0.2.2"
__DATE__	= "28/12/2015"

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

import csv
from colors import *

class connect(object):
	def __init__(self, ver3):
		self.ver3 = ver3

	def listing(self):
		if self.ver3 == True:
			exception = FileNotFoundError
		else:
			exception = IOError

		try:
			with open("/etc/organon/tools.db", "r") as csvfile:
				csvcontent = csv.reader(csvfile, delimiter=";")

				for row in csvcontent:
					print(green + " [+] " + row[0] + yellow + " v" + row[1] + default)
					print(row[4] + "\n")

		except exception:
			print(red + " [!] " + default + "No database found! Use \"organon\
 -S\" to sync with our servers")

	def search(self, keyword):
		if self.ver3 == True:
			exception = FileNotFoundError
		else:
			exception = IOError
		try:
			with open("/etc/organon/tools.db", "r") as csvfile:
				csvcontent = csv.reader(csvfile, delimiter=";")

				for row in csvcontent:
					#The following convert to lower case
					#reference link: http://stackoverflow.com/questions/8265648/using-the-lowercase-function-with-csv-rows
					row = ([r.lower() for r in row])
					if keyword in row[0]:
						print(green + " [+] " + row[0] + yellow + " v" + row[1]\
						 + default)
						print(row[4] + "\n")
					elif keyword in row[1]:
						print(green + " [+] " + row[0] + yellow + " v" + row[1]\
						 + default)
						print(row[4] + "\n")
					elif keyword in row[2]:
						print(green + " [+] " + row[0] + yellow + " v" + row[1]\
						 + default)
						print(row[4] + "\n")
					elif keyword in row[3]:
						print(green + " [+] " + row[0] + yellow + " v" + row[1]\
						 + default)
						print(row[4] + "\n")
					elif keyword in row[4]:
						print(green + " [+] " + row[0] + yellow + " v" + row[1]\
						 + default)
						print(row[4] + "\n")
		except exception:
			print(red + " [!] " + default + "No database found! Use \"organon\
 -S\" to sync with our servers")
