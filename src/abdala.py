#!/usr/bin/python
#coding=utf-8

import csv

class local(object):
	def __init__(self, ver3):
		self.ver3 = ver3

	def listing(self):
		if self.ver3 == True:
			exception = FileNotFoundError
		else:
			exception = IOError

		try:
			pkgs = []
			with open("/etc/organon/installed.db", "r") as csvfile:
				csvcontent = csv.reader(csvfile, delimiter=";")

				for row in csvcontent:
					pkgs.append(row)

		except exception:
			print(" [!] No tool installed. Use organon -i <tool> to install")
		return(pkgs)

	def add(self, pkg, pkg_ver, itens):
		with open("/etc/organon/installed.db", "w") as csvfile:
			csvcontent = csv.writer(csvfile, delimiter = ";")
			for i in itens:
				csvcontent.writerow(i)
			csvcontent.writerow([pkg, pkg_ver])