#!/bin/bash

#This script belongs to organons project
#Author = Fnkoc
#Project = https://github.com/maximozsec/organon

#Check user permition
if [ "$(id -u)" != "0" ]; then
	clear
	echo -e " \033[31m [!]\033[00m This script must be run as root " 1>&2
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

#Checking ruby version
rubyversion=`ruby --version | cut -f1 -d. | grep -i "$ruby 2"`

if [ ! -n "$rubyversion" ]
then
	echo -e "\033[31m [!]\033[00m Installing Ruby 2"
	apt-get install libffi-dev libssl-dev libreadline-dev make g++ build-essential zlib1g-dev libyaml-dev
	wget http://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.0.tar.gz
	tar xpvf ruby-2.2.0.tar.gz
	cd ruby-2.2.0 && ./configure && make && make install
	cd ..	#Exits ruby-2.2.0 directory
else
	echo -e "\033[31m [!]\033[00m ruby 2 installed"
fi
#End Ruby check

#Install Dependencies
#sys=`cat /etc/issue | grep -i ubuntu`

#if [ ! -n "$sys" ]
#then
#	apt-get install python libmysqlclient-dev rubygems
#else
#	echo -e "\033[32m [+]\033[00m UBUNTU OS"
#	apt-get install python libmysqlclient-dev rubygems-integration
#fi
apt-get install python libmysqlclient-dev

cd .. 	#Exits organon directory

gem install mysql colorize

#Move organon to opt
echo -e "\033[32m [+]\033[00m Moving organon to /opt"
mv organon /opt/

echo -e "\033[32m [+]\033[00m Creating symbolic link"
echo \#\!/bin/bash >> /usr/bin/organon
echo cd /opt/organon >> /usr/bin/organon
echo exec python organon.py \"\$\@\" >> /usr/bin/organon

echo -e "\033[32m [+]\033[00m Changing permitions"
chmod +x /usr/bin/organon
chmod +x /opt/organon/src/*

echo -e "\033[32m [+]\033[00m Cleaning directory"
rm -rf /opt/organon/ruby-2.2.0*

echo -e '\033[32m [+]\033[00m Complete!'
echo 'Type "organon" in order to use it'
