#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
TODO: 
	- lot of things...

All rights reserved.
--------------------
This program mustn't be used as illegal purposes. ;)

:: Performances:
:: -------------
::
:: After an estimation, this program
:: Makes [100/150]requests/sec with 35
:: threads

The entire developement of this program
rotates around modules, So you can import one
Of my modules in your programs if you want.

Each method had his help string.

Ex.
----

import crawly
help(crawly)
'''

# Avoiding *.pyc files.
import sys
sys.dont_write_bytecode = True
# Modules:
from crawly import Runner

class Crawly:
	def __init__(self):
		'''
		Running run() function to lunch
		the program.
		'''
		self.run = Runner.run()

if __name__ == '__main__':
	# Let's go ;)
	Crawly()
