#!/usr/bin/ruby

###################################################################
# This script makes the download, compilation and installation of #
# pompem on linux distributions.				  #
# It only automates the things.				          #
#								  #
# Maximoz Sec <maximozsec@outlook.com.br>		          #
# 15/02/2015							  #
###################################################################	

Dir.chdir("src/")
system "sudo ./generator.py pompem python pompem.py"

require 'colorize'
load 'spinner.rb'

print "[" + " ~~ ".red + "] Installing Pompem..."
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
[ #{"ok".green} ] Write 'pompem' without the quotes on your terminal to run the tool.
-------------------------------------------------------------------------------
PNT
