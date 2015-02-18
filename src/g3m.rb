#!/usr/bin/ruby

###################################################################
# This script makes the download, compilation and installation of #
# g3m on linux distributions.							      #
# It only automates the things.									  #
#																  #
# Maximoz Sec <maximozsec@outlook.com.br>						  #
# 02/01/2015													  #
###################################################################	

comandos = [
	"wget https://sites.google.com/site/roxzinx/g3m/g3m.c https://sites.google.com/site/roxzinx/g3m/c4 https://sites.google.com/site/roxzinx/g3m/check.c https://sites.google.com/site/roxzinx/g3m/freak.c https://sites.google.com/site/roxzinx/g3m/juno.c",
	"sudo mkdir /opt/g3m",	
	"gcc g3m.c -o g3m",
	"sudo mv g3m g3m.c check.c freak.c juno.c c4 /opt/g3m",
	"sudo sh -c 'echo \\#\!/bin/bash >> /usr/bin/g3m'",
	"sudo sh -c 'echo exec /opt/g3m/g3m \"\\$@\" >> /usr/bin/g3m'",
	"sudo chmod +x /usr/bin/g3m"]

comandos.each { |x| system x }

require 'colorize'
load 'spinner.rb'

print "[" + " ~~ ".red + "] Installing g3m..."
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
[ #{"ok".green} ] Write 'g3m' without the quotes on your terminal to run the tool.
-------------------------------------------------------------------------------
PNT
