#!/bin/bash

#This script belongs to organons project
#Author = Fnkoc
#Project = https://github.com/maximozsec/organon

#Check if is already installed
if [ -e /opt/organon ]
then
	sudo rm -rf /opt/organon
fi

if [ -e /usr/bin/organon ]
then
	sudo rm /usr/bin/organon
fi

#end check

#Checking if ruby is installed
ruby=`ruby --version`

if [ ! -n "$ruby" ]
then
	echo -e "\033[1m [!]\033[00m sudo apt-get install ruby"
	sudo apt-get install ruby
else
	echo -e "\033[31m [!]\033[00m ruby installed"
fi
#End Ruby check

#Check Distro
distro=`cat /etc/issue | cut -d ' ' -f1`

if [ "$distro" = "Debian" ]
then
	echo -e "033[1m [!]\033[00m sudo apt-get install python libmysqlclient-dev bundler"
	sudo apt-get install python libmysqlclient-dev bundler

elif [ "$distro" = "Ubuntu" ]
then
	#Check Ubuntu Version
	version=`lsb_release -r | cut -d: -f2`
	if [ "$version" = "	14.10" ]
	then
		echo -e "033[1m [!]\033[00m sudo apt-get install python libmysqlclient-dev bundler"
		sudo apt-get install python libmysqlclient-dev bundler
	else
		echo -e "033[31m [!]\033[00m sudo apt-get install python libmysqlclient-dev ruby-bundler"
		sudo apt-get install python libmysqlclient-dev ruby-bundler
	fi
	#end Version check
else
	echo -e "\033[31m [!]\033[00m sudo apt-get install python libmysqlclient-dev ruby-bundler"
	sudo apt-get install python libmysqlclient-dev ruby-bundler
fi
#End Distro check

echo -e "\033[32m [+]\033[00m Bundling ruby gems"
bundle install

cd .. 	#Exits organon directory

#Move organon to opt
echo -e "\033[32m [+]\033[00m Moving organon to /opt"
if [ -e "organon-master" ]
then
	mv organon-master organon
fi

#Move organon to opt
echo -e "\033[32m [+]\033[00m Moving organon to /opt"
sudo mv organon /opt/

#Create Symbolic Links
echo -e "\033[32m [+]\033[00m Creating symbolic link"
sudo sh -c "echo \#\!/bin/bash >> /usr/bin/organon"
sudo sh -c "echo cd /opt/organon >> /usr/bin/organon"
sudo sh -c "echo exec python organon.py \$\@\ >> /usr/bin/organon"

#Move Man Page
echo -e "\033[32m [+]\033[00m Creating MAN page"
if [ ! -e /usr/local/share/man/man8 ]
then
	sudo mkdir /usr/local/share/man/man8
fi
sudo mv /opt/organon/organon.8 /usr/local/share/man/man8/

#Change permission
echo -e "\033[32m [+]\033[00m Changing permissions"
sudo chmod +x /usr/bin/organon
sudo chmod 644 /usr/local/share/man/man8/organon.8

#Delete ruby file
echo -e "\033[32m [+]\033[00m Creating .cache directory"
mkdir /opt/organon/.cache

echo -e '\033[32m [+]\033[00m Complete!'
echo 'Type "organon" in order to use it'
