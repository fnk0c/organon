#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "Fnkoc"
__VERSION__	= "0.1.4"
__DATE__	= "21/01/2015"

try:
	import MySQLdb as mdb
except:
	print(" [!] MySQLdb is required")
	print(" sudo apt-get install python-mysqldb")
import sys
import os

def listar(command):
	try:
		con = mdb.connect("104.236.105.209", "organonuser", "organon", "organon")

		with con:
			cur = con.cursor()
			cur.execute(command)
		
			for i in range(cur.rowcount):
				row = cur.fetchone()

				print" [+] ", row[0], row[1]
				print" ", row[2]
				print""


	except mdb.Error, e:
		print(e)

	finally:
		if con:
			con.close()

def install(command):
	try:
		con = mdb.connect("104.236.105.209", "organonuser", "organon", "organon")

		with con:
			cur = con.cursor()
			cur.execute(command)
		
			for i in range(cur.rowcount):
				row = cur.fetchone()
				
				if (row[1] is None) or (len(row[0]) == 0):
					pass

				else:
					dep = "sudo apt-get install " + row[1] + " -y"
					print(" [!] Installing dependencies\n %s" % dep)
					os.system(dep)

				if "https://github.com/" in row[0]:		#Caso a URL seja referente ao github
					get = "git clone " + row[0]			#Deve ser utilizado o comando git
				else:									#Ao invés de
					get = "wget " + row[0]				#Wget

				print(" [!] Downloading source\n %s" % get)
				os.system(get)

	except mdb.Error, e:
		print e

	finally:
		if con:
			con.close()
