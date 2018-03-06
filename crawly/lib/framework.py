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
				print """Framework options:
help -- Print help of this program.
quit, exit -- Killing the program.
show modules
use <module>"""


	def ParseOptions(self):
		params = raw_input(self.ps1).lower()
		try:

			if "help" in params:
				self.PrintOptions()
				self.run()

			elif "quit" in params:
				sys.exit(0)
			elif "exit" in params:
				sys.exit(0)

			elif "show modules" in params:
				pass

			elif "use Dirbruter" in params:
				print "test"
			else:
				self.run()

		except KeyboardInterrupt:
			print "\nCTRL + C pressed, killing the framework..."
			sys.exit(0)

	def run(self):
		self.ParseOptions()