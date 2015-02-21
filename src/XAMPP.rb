#!/usr/bin/ruby

###################################################################
# This script makes the download, compilation and installation of #
# XAMPP on linux distributions.			          	  #
# It only automates the things.			                  #
#							          #
# Maximoz Sec <maximozsec@outlook.com.br>	                  #
# 20/02/2015					                  #
###################################################################

system "chmod +x xampp-linux-x64-5.6.3-0-installer.run; sudo ./xampp-linux-x64-5.6.3-0-installer.run"

Dir.chdir("/opt/lampp/")
system "sudo ./generator.py xampp sh xampp"

require 'colorize'
load 'lib/spinner.rb'

system "clear"
print "[" + " ~~ ".red + "] Installing XAMPP..."
show_wait_spinner{
  sleep rand(4)+2 # Simulate a task taking an unknown amount of time
}
load 'lib/banner.rb'
prog("xampp")
