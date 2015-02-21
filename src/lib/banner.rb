#!/usr/bin/ruby

# Maximoz Sec <maximozsec@outlook.com.br>
# 20/02/2015

require 'colorize'

def prog(name)

banner = """


,~~
|'|#{">".yellow}		Penso,
|U|		logo
| |		programo.
..>>

[ #{"ok".green} ] Done!
-------------------------------------------------------------------------------
[ #{"ok".green} ] The tool is ready. Enjoy!
[ #{"ok".green} ] Write '#{name}' without the quotes on your terminal to run the tool.
-------------------------------------------------------------------------------
"""
puts banner
end
