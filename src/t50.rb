=begin
This script makes the download, compilation and installation of
T50 on linux distributions.
It only automates the things.
=end

# Maximoz Sec
# 01/01/2015

comandos = [
	"wget https://downloads.sourceforge.net/project/t50/t50-5.4.1/t50-5.4.1.tar.gz",
	"tar -xvf t50-5.4.1.tar.gz",
	"sudo chmod -R 555 t50-5.4.1",
	"cd t50-5.4.1 && sudo make -W Makefile",
	"sudo mv t50-5.4.1 /opt",
	"sudo sh -c 'echo \\#\!/bin/bash >> /usr/bin/t50'",
	"sudo sh -c 'echo exec /opt/t50-5.4.1/t50 \"\\$@\" >> /usr/bin/t50'",
	"sudo chmod +x /usr/bin/t50"]

puts "[+] Installing t50....\n"

comandos.each { |x| system x }

puts "\n"
puts "-"*80
puts "[+] The tool is ready. Enjoy!"
puts "[+] Write \"t50\" without the quotes on your terminal to run the application."
puts "-"*80
