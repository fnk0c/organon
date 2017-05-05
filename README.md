![Image of organon](https://i.imgur.com/VvoUkMP.jpg)

This program focuses on automating the download, installation and compilation of pentest tools from source

Tool developed for Linux systems (APT and Pacman)

Authors:
--------
* [Franco Colombino (Fnkoc)](https://github.com/fnk0c)  
***Special thanks to [Ygor Máximo (Maximoz)](https://github.com/maximozsec) for support on the beginning***

Requirements
-------------
1. Python >=2.7 or >=3.4    
2. GNU/Linux system based on Debian and Arch

Install
-------
	git clone https://github.com/fnk0c/organon.git
	cd organon
	python setup.py install

[With screenshot](https://projetos.cienciahacker.ch/organon/install/install.html)

Tested on:
----------
* Arch Linux
* Apricity OS 1.4
* Debian 7.8 Wheezy
* Debian 8 Jessie
* Elementary OS Luna
* Linux Mint 17.1
* Manjaro 0.8.13
* Ubuntu 14.04 x86_64
* Ubuntu 14.10 x86_64

Screenshot
----------
![Screenshot](http://i.imgur.com/xjBVGMG.png)

Help
----
```
usage: organon [-h] [-a] [-v] [-i I [I ...]] [-r R [R ...]] [--deps] [--conf]
               [-U] [-u] [-S] [-s S] [-L] [--clean] [--yes]

Package manager that focus on Pentest tools

optional arguments:
  -h, --help     show this help message and exit
  -a, --about    About this tool
  -v, --version  Show version and exit
  -i I [I ...]   Install packages
  -r R [R ...]   Remove packages
  --deps         Remove dependencies (use with -r)
  --conf         Remove configuration files (use with -r)
  -U             Update Organon
  -u             Update packages
  -S             Synchronize database
  -s S           Search for packages
  -L             List all packages available
  --clean        Clean Organon's cache
  --yes          Assume yes to all questions


organon -h
	Shows help

organon -a
	Shows MAN file

organon -v 
	Shows version

organon -i [PACKAGE]
	Install an specific package

organon -r [PACKAGE]
  Remove an specific package
  --dependencies
  	Remove package dependencies
	--config
		Remove package configuration files

organon -U
	Search and download updates for Organon

organon -u
	Search and download updates for installed packages

organon -S [PACKAGE]
	Synchronizes database between server and client

organon -s [PACKAGE]
	Search for an specific package

organon -L
	Lists all the availables tools to install

organon -Li
	List all tools already installed

organon --clean
	Clean /var/cache/organon directory
```

BUGS
----
Since it's still on development phase bugs are expected. Please, **report to us!** or open an **Issue**
* fb.com/franco.colombino
* fb.com/cienciahacker

Be Part of development
----------------------
Send us a message on facebook
