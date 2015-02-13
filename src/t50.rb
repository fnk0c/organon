#!/usr/bin/ruby

=begin
This script makes the download, compilation and installation of
T50 on linux distributions.
It only automates the things.
=end

# Maximoz Sec
# 01/01/2015

comandos = [
	"tar -xvf t50-5.4.1.tar.gz",
	"sudo chmod -R 555 t50-5.4.1",
	"cd t50-5.4.1 && sudo make -W Makefile"]

puts "[+] Installing t50....\n"

comandos.each { |x| system x }

puts "\n"
puts "-"*80
puts "[+] The tool is ready. Enjoy!"
puts "[+] Write \"t50\" without the quotes on your terminal to run the application."
puts "-"*80
