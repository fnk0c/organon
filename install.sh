#!/bin/bash

#This script belongs to organons project
#Author = Fnkoc
#Project = https://github.com/maximozsec/organon

#Check user permition
if [ "$(id -u)" != "0" ]; then
	clear
	echo "This script must be run as root" 1>&2
	exit
fi

#Check if already installed
if [ -e /opt/organon ]
then
	rm -rf /opt/organon
fi

if [ -e /usr/bin/organon ]
then
	rm /usr/bin/organon
fi

#end check

#Install Dependencies
sys=`cat /etc/issue | grep -i ubuntu`

if [ ! -n "$sys" ]
then
	apt-get install ruby python libmysqlclient-dev rubygems
else
	echo "UBUNTU OS"
	apt-get install ruby python libmysqlclient-dev rubygems-integration
fi

rubyversion=`ruby --version | cut -f1 -d. | grep -i "$ruby 2"`

#Checking ruby version
if [ ! -n "$rubyversion" ]
then
	echo " [!] Installing Ruby 2"
	apt-get install libffi-dev
	wget http://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.0.tar.gz
	tar xpvf ruby-2.2.0.tar.gz
	cd ruby-2.2.0 && ./configure && make && make install
	cd ..	#Exits ruby-2.2.0 directory
else
	echo " [!] ruby 2 installed"
fi

#End Ruby check

cd .. 	#Exits organon directory

gem install mysql colorize

#Move organon to opt
mv organon /opt/

echo \#\!/bin/bash >> /usr/bin/organon
echo cd /opt/organon >> /usr/bin/organon
echo exec python organon.py \"\$\@\" >> /usr/bin/organon

chmod +x /usr/bin/organon
chmod +x /opt/organon/src/*

echo '[+] Complete!'
echo 'Type "organon" in order to use it'
