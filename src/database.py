#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "Fnkoc"
__VERSION__	= "0.2.1"
__DATE__	= "14/12/15"

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

"""
This script is responsible to connect with the database and retrieve all the
needed informations
"""

from colors import *

class connect(object):
	def __init__(self, host, ver3):
		self.host = host
		self.ver3 = ver3

	def ip_retriever(self):
		def __init__(self):
			self.ip = ip
		#lib to parse html
		from bs4 import BeautifulSoup
		
		#Python 3 support
		if self.ver3 == True:
			import urllib.request as u
		#Python 2 support
		elif self.ver3 == False:
			import urllib as u

		#Download HTML
		con = u.urlopen(self.host)
		html = con.read()

		### - Parse HTML - ###
		soup = BeautifulSoup(html, "html5lib")
		for l in soup.findAll("link"):
			ip = l.get("href")

		ip = ip.split(":")
		self.ip = (ip[1].replace("/", ""))

	def MySQL(self, query):
		import pymysql as sql

		#Database credentials
		userdb 	= "organonuser"
		passwd 	= "organon"
		db		= "organon"

		try:
			con = sql.connect(self.ip, userdb, passwd, db)
			cur = con.cursor()
			cur.execute(query)

			for row in cur:
				for i in row[::5]:
					package = str(i)
				for i in row[1::5]:
					version = str(i)
				for i in row[3::5]:
					description = str(i)
			
				print(" %s%s%s | v%s%s%s\n\n    %s\n" % (green, package, default, \
				yellow, version, default, description))
		except sql.Error as e:
			print(e)
			exit()
		finally:
			if con:
				con.close()
