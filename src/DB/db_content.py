#!/usr/bin/python
#coding=utf-8

import MySQLdb as mdb
import sys
import os

def listar(command):
	try:
		con = mdb.connect("186.222.226.68", "root", "organon", "organon")

		with con:
			cur = con.cursor()
			cur.execute(command)
		
			for i in range(cur.rowcount):
				row = cur.fetchone()

				print " [+] ", row[0], row[1]
				print " ", row[2]
				print ""


	except mdb.Error, e:
		print e

	finally:
		if con:
			con.close()

def install(command):
	try:
		con = mdb.connect("186.222.226.68", "root", "organon", "organon")

		with con:
			cur = con.cursor()
			cur.execute(command)
		
			for i in range(cur.rowcount):
				row = cur.fetchone()
				dep = "sudo apt-get install " + row[1] + "-y"
				print " [!] Installing dependencies\n %s" % dep
				os.system(dep)
				get = "wget " + row[0]
				print " [!] Downloading source\n %s" % get
				os.system(get)

	except mdb.Error, e:
		print e

	finally:
		if con:
			con.close()
