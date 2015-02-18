#!/usr/bin/ruby

###################################################################
# This script makes the download, compilation and installation of #
# T50 on linux distributions.								      #
# It only automates the things.									  #
#																  #
# Maximoz Sec <maximozsec@outlook.com.br>						  #
# 01/01/2015													  #
###################################################################	

comandos = [
	"wget https://downloads.sourceforge.net/project/t50/t50-5.4.1/t50-5.4.1.tar.gz",
	"tar -xvf t50-5.4.1.tar.gz && rm t50-5.4.1.tar.gz",
	"sudo chmod -R 555 t50-5.4.1",
	"cd t50-5.4.1 && sudo make -W Makefile",
	"sudo mv t50-5.4.1 /opt",
	"sudo sh -c 'echo \\#\!/bin/bash >> /usr/bin/t50'",
	"sudo sh -c 'echo exec /opt/t50-5.4.1/t50 \"\\$@\" >> /usr/bin/t50'",
	"sudo chmod +x /usr/bin/t50"]

comandos.each { |x| system x }

require 'colorize'
load 'lib/spinner.rb'

print "[" + " ~~ ".red + "] Installing T50..."
show_wait_spinner{
  sleep rand(4)+2 # Simulate a task taking an unknown amount of time
}

puts <<PNT


,~~
|'|#{">".yellow}		Penso,
|U|		logo
| |		programo.
..>>

[ #{"ok".green} ] Done!
-------------------------------------------------------------------------------
[ #{"ok".green} ] The tool is ready. Enjoy!
[ #{"ok".green} ] Write 't50' without the quotes on your terminal to run the tool.
-------------------------------------------------------------------------------
PNT
