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

#Checking ruby version
rubyversion=`ruby --version | cut -f1 -d. | grep -i "$ruby 2"`

if [ ! -n "$rubyversion" ]
then
	echo -e "\033[31m [!]\033[00m Installing Ruby 2"
	sudo apt-get install libffi-dev libssl-dev libreadline-dev make g++ build-essential zlib1g-dev libyaml-dev
	wget http://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.0.tar.gz
	tar xpvf ruby-2.2.0.tar.gz
	cd ruby-2.2.0 && ./configure && make && sudo make install
	cd ..	#Exits ruby-2.2.0 directory
else
	echo -e "\033[31m [!]\033[00m ruby 2 installed"
fi
#End Ruby check

sudo apt-get install python libmysqlclient-dev bundler

echo -e "\033[32m [+]\033[00m Bundling ruby gems"
bundle install

cd .. 	#Exits organon directory

#Move organon to opt
echo -e "\033[32m [+]\033[00m Moving organon to /opt"
sudo mv organon /opt/

echo -e "\033[32m [+]\033[00m Creating symbolic link"
sudo sh -c "echo \#\!/bin/bash >> /usr/bin/organon"
sudo sh -c "echo cd /opt/organon >> /usr/bin/organon"
sudo sh -c "echo exec python organon.py \$\@\ >> /usr/bin/organon"

echo -e "\033[32m [+]\033[00m Creating MAN page"
if [ ! -e /usr/local/share/man/man8 ]
then
	sudo mkdir /usr/local/share/man/man8
fi
sudo mv organon.8 /usr/local/share/man/man8/

echo -e "\033[32m [+]\033[00m Changing permissions"
sudo chmod +x /usr/bin/organon
sudo chmod +x /opt/organon/src/*
sudo chmod 644 /usr/local/share/man/man8/organon.8

echo -e "\033[32m [+]\033[00m Cleaning directory"
sudo rm -rf /opt/organon/ruby-2.2.0*

echo -e '\033[32m [+]\033[00m Complete!'
echo 'Type "organon" in order to use it'
