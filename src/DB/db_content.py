#!/usr/bin/python
#coding=utf-8

import MySQLdb as mdb
import sys

def action(command):
	try:
		con = mdb.connect("localhost", "root", "organon", "organon")

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
