#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of 
#Scanner Inurl on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"28/12/2014"

import os

comandos = [
	"chmod -R 555 SCANNER-INURLBR",
	"cd SCANNER-INURLBR && chmod +x inurlbr.php",
	"sudo mv SCANNER-INURLBR /opt",
	"sudo sh -c 'echo \#\!/bin/bash >> /usr/bin/inurlbr'",
	"sudo sh -c 'echo exec php /opt/SCANNER-INURLBR/inurlbr.php \$@ >> /usr/bin/inurlbr'",
	"sudo chmod +x /usr/bin/inurlbr"]

for a in comandos:
	os.system(a)

print("\n\n")
print("-"*80)
print("\n All clear\n Enjoy!")
print("""
  write \"inurlbr\" without the quotes on your terminal
  and hit ENTER to run the application
  Scanner Inurlbr can be found at /opt
""")
print("-"*80)
