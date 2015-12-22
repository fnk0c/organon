![Image of organon](https://i.imgur.com/VvoUkMP.jpg)

This program focuses on automating the download, installation and compilation of pentest tools from source

# ATTENTION!

## ** This tool is no longer working! Server is down ** .

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

[With screenshot](http://organon.ddns.net/install)

Tested on:
----------
* Arch Linux
* Manjaro
* Debian 8

Screenshot
----------
![Screenshot](https://i.imgur.com/mAKhkRC.png)

Help
----
```
usage: organon [-h] [-a] [-v] [-i I [I ...]] [-r R [R ...]] [--dependencies]
               [--config] [-U] [-u] [-S] [-s S] [-L] [--clean]

Package manager that focus on Pentest tools

optional arguments:
  -h, --help      show this help message and exit
  -a, --about     About this tool
  -v, --version   Show version and exit
  -i I [I ...]    Install packages
  -r R [R ...]    Remove packages
  --dependencies  Remove dependencies (use with -r)
  --config        Remove configuration files (use with -r)
  -U              Update Organon
  -u              Update packages
  -S              Synchronize database
  -s S            Search for packages
  -L              List all packages available
  --clean         Clean Organon's cache

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

About current version
---------------------
#### `v0.2.2`
- All features from previous versions + review of the code  
 - Using rsync to do package tracking
 - Download application according to platform (x86 ou x86_64)
 - MySQL database replaced by CSV file

About previous version
---------------------
#### `v0.2.1`
- All features from previous versions + review of the code  
 - Installation script re-wrote and optimized  
 - Remove ruby  
 - All scripts are made in python  

