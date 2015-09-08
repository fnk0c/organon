#!/bin/bash

#This script belongs to organons project
#Author = Fnkoc
#Project = https://github.com/maximozsec/organon
#last update 04/06/2015

#	 Copyright (C) 2015  Franco Colombino & Ygor Máximo
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#Colors
red="\033[31m"
green="\033[32m"
default="\033[00m"
white="\033[1m"

#Check user id
id=`id -u`

if [ $id == 0 ]
then
	echo -e "$red[!]$default$white You're not supposed to run this script as root$default"
	read -p "[!] Continue? [y/N] " choice
	
	if [ $choice != "y" ]
	then
		echo -e "$green [-] User aborted$default"
		exit
	fi
fi
#end check user id

#Check if is already installed
if [ -e /usr/share/organon ]
then
	sudo rm -rf /usr/share/organon
fi

if [ -e /usr/bin/organon ]
then
	sudo rm /usr/bin/organon
fi

if [ -e /usr/local/share/man/man8/organon.8 ]
then
	sudo rm /usr/local/share/man/man8/organon.8
fi
#end check

#Check Distro
if [ -e /etc/apt ]
then
	distro=`cat /etc/issue | cut -d ' ' -f1`

	if [ "$distro" = "Ubuntu" ]
	then
		#Check Ubuntu Version
		version=`cat /etc/*release | grep -i version_id | cut -d '"' -f 2`
		if [ "$version" = "	12.04" ] || [ "$version" = " 14.04" ]
		then
			echo -e "$white [!]$default sudo apt-get install python libmysqlclient-dev ruby-bundler"
			sudo apt-get install python ruby libmysqlclient-dev ruby-bundler
		else
			echo -e "$white [!]$default sudo apt-get install python libmysqlclient-dev bundler"
			sudo apt-get install python ruby libmysqlclient-dev bundler
		fi
		#end Ubuntu check
	
	elif [ "$distro" = "Debian" ]
	then
		echo -e "$white [!]$default sudo apt-get install python libmysqlclient-dev bundler"
		sudo apt-get install python ruby libmysqlclient-dev bundler

	else
		echo -e "$white [!]$default Try to install manually:"
		echo " [+] Packages:"
		echo "	python"
		echo "	libmysqlclient-dev"
		echo "	ruby-bundler"
		echo " [+] gems:"
		echo "	colorize"
		echo " 	nokogiri"
		echo " 	mysql"
		exit
	fi

elif [ -e /etc/pacman.d ]
then
	sudo pacman -S python ruby libmariadbclient --needed


else
	echo -e "$red [-]$default Your system doesn't seem to be supported"
	echo " Please, read the documentation"
	exit
fi

#End Distro check

echo -e "$green [+]$default Bundling ruby gems"
if [ -e /etc/pacman.d ]
then
	if [ 'pacman -Q | grep ruby-bundler' = 1 ]
	then
		wget https://aur.archlinux.org/packages/ru/ruby-bundler/PKGBUILD
		makepkg PKGBUILD
		sudo pacman -U ruby-bundler-*.pkg.tar.xz
		rm -rf pkg PKGBUILD ruby-bundler-*.pkg.tar.xz bundler-*.gem
		echo -e "$green [+]$default Bundler installed"
	else
		echo -e "$green [+]$default Bundler installed"
	fi
fi

bundle install

cd .. 	#Exits organon directory

if [ -e "organon-master" ]
then
	echo -e "$red [!]$default Aparently you haven't clone the repository."
	echo -e "This way you will not be able to retrive updates to Organon"
	echo -e "use$green git clone https://github.com/fnk0c/organon$default to clone"
	sleep 5
	mv organon-master organon
fi

#Move organon to /usr/share
echo -e "$green [+]$default Moving organon to /usr/share"
sudo mv organon /usr/share/

#Create Symbolic Links
echo -e "$green [+]$default Creating symbolic link"
sudo sh -c "echo \#\!/bin/bash >> /usr/bin/organon"
sudo sh -c "echo cd /usr/share/organon >> /usr/bin/organon"
sudo sh -c "echo exec python organon.py \$\@\ >> /usr/bin/organon"

#Move Man Page
echo -e "$green [+]$default Creating MAN page"
if [ ! -e /usr/local/share/man/man8 ]
then
	sudo mkdir /usr/local/share/man/man8
fi
sudo mv /usr/share/organon/doc/organon.8 /usr/local/share/man/man8/

#Change permission
echo -e "$green [+]$default Changing permissions"
sudo chmod +x /usr/bin/organon
sudo chmod 644 /usr/local/share/man/man8/organon.8

#Create .cache
echo -e "$green [+]$default Creating .cache directory"
mkdir /usr/share/organon/.cache

#Configuring organon based on your distro
echo -e "$green [+]$default Configuring organon to your system"
if [ -e /etc/apt ]
then
	echo -e "$white [+] Debian based system$default"
elif [ -e /etc/pacman.d ]
then
	echo -e "$white [+] Arch based system$default"
	sed -i "s/debian/arch/g" /usr/share/organon/organon.py
	sed -i "s/debian/arch/g" /usr/share/organon/src/DB/database_connector.rb
	sed -i "s/apt-get install/pacman -S/g" /usr/share/organon/src/DB/database_connector.rb
	sed -i "s/apt-get remove/pacman -R/g" /usr/share/organon/src/DB/database_connector.rb
fi

echo -e "$green [+]$white Complete!"
echo -e "Type "organon" in order to use it $default"
