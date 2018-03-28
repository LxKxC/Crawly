# -*- coding: utf-8 -*-
# Part of crawly2

import sys
# Modules:
from ..core import headers as heads
from ..core import tool

class Framework:
	'''
	This is a very simple framework
	desc...
	'''
	def __init__(self):
		self.c = heads.Strings()
		self.tool = tool.Tools()
		self.ps1 = self.c.G + self.c.BOLD + "[Lix]" + self.c.O + self.c.BOLD + " >>> "

	def PrintOptions(self):
		print("""Framework options:
help -- Print help of this program.
quit, exit -- Killing the program.
show modules -- Show different modules.
use <module> -- Use a specific module.""")

	def PrintModules(self):
		print("""Different modules:

Scan		Attack
----		------

Crawler		Shellshock
Dirbrute	Bashdoor
DNSBrute	HTMLBrute
...		HTTPBrute
...		SSHBrute
""")

	def ParseOptions(self):
		while True:
			params = raw_input(self.ps1).lower()

			if "exit" in params or "quit" in params:
				break

			elif "help" in params:
				self.PrintOptions()

			elif "show modules" in params:
				self.PrintModules()

			elif params == "use":
				print(self.c.INFO + "Not enough options.")

			elif "use crawler" in params:
				print("test")
			
			else:
				if params == '':
					continue
				else:
					print(self.c.ERROR + "Seems to be an unknown command.")

	def run(self):
		self.ParseOptions()