#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of 
#Scanner Inurl on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"28/12/2014"

import os

comandos = [
	"sudo apt-get install php5 php5-curl php5-cli -y",
	"git clone https://github.com/googleinurl/SCANNER-INURLBR.git",
	"chmod -R 555 SCANNER-INURLBR",
	"cd SCANNER-INURLBR && chmod +x inurlbr.php",
	"sudo mv SCANNER-INURLBR /opt",
	"sudo sh -c 'echo \#\!/bin/bash >> /usr/bin/inurlbr'",
	"sudo sh -c 'echo exec php /opt/SCANNER-INURLBR/inurlbr.php \$@ >> /usr/bin/inurlbr'",
	"sudo chmod +x /usr/bin/inurlbr"]

try:
   input = raw_input
except NameError:
   pass

print("\n Install Scanner Inurlbr and its dependencies?\n [Y]es [N]o [V]iew dependencies")
answer = input("\n>> ").lower()

if answer == "y":
	for action in comandos:
		os.system(action)

elif answer == "n":
	exit()

elif answer == "v":
	print(comandos[0].replace("sudo apt-get install", "").replace("-y", ""))
	exit()

else:
	print("Invalid option")
	exit()

print("\n\n")
print("-"*80)
print("\n All clear\n Enjoy!")
print("""
  write \"inurlbr\" without the quotes on your terminal
  and hit ENTER to run the application
  Scanner Inurlbr can be found at /opt
""")
print("-"*80)
