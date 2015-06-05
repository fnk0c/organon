#!/bin/bash

#This script belongs to organons project
#Author = Fnkoc
#Project = https://github.com/maximozsec/organon
#last update 04/06/2015

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

#Checking if ruby is installed
ruby=`ruby --version`

#Check Distro
if [ -e /etc/apt ]
then
	distro=`cat /etc/issue | cut -d ' ' -f1`

	if [ "$distro" = "Debian" ]
	then
		echo -e "$white [!]$default sudo apt-get install python libmysqlclient-dev bundler"
		sudo apt-get install python ruby libmysqlclient-dev bundler

	elif [ "$distro" = "Ubuntu" ]
	then
		#Check Ubuntu Version
		version=`lsb_release -r | cut -d: -f2`
		if [ "$version" = "	14.10" ]
		then
			echo -e "$white [!]$default sudo apt-get install python libmysqlclient-dev bundler"
			sudo apt-get install python ruby libmysqlclient-dev bundler
		else
			echo -e "$white [!]$default sudo apt-get install python libmysqlclient-dev ruby-bundler"
			sudo apt-get install python ruby libmysqlclient-dev ruby-bundler
		fi
		#end Version check
	else
		echo -e "$white [!]$default sudo apt-get install python libmysqlclient-dev ruby-bundler"
		sudo apt-get install python ruby libmysqlclient-dev ruby-bundler
	fi

elif [ -e /etc/pacman.d ]
then
	sudo pacman -S python ruby libmariadbclient
fi

#End Distro check

echo -e "$green [+]$default Bundling ruby gems"
if [ -e /etc/pacman.d ]
then
	wget https://aur.archlinux.org/packages/ru/ruby-bundler/PKGBUILD
	makepkg PKGBUILD
fi

bundle install

cd .. 	#Exits organon directory

if [ -e "organon-master" ]
then
	mv organon-master organon
fi

#Move organon to opt
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
sudo mv /usr/share/organon/organon.8 /usr/local/share/man/man8/

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
