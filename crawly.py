#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
TODO: 
	- create docs folder /!\


All rights reserved.
--------------------
This program mustn't be used as illegal purposes. ;)
Crawly is a web scanner coded for the DGSquad.

:: Performances:
:: -------------
::
:: After an estimation, this program
:: Makes [100/150]requests/sec with 35
:: threads

The entire developement of this program
rotates around modules, So you can import one
Of my modules in your programs if you want.

Example:
--------

from crawly.lib import scan as s
s.Dirbrute("www.host.com", [True/False], [True/False], 20)

And the module will print all the directorys of 
the host.

Needs of the classes (scan.py):
------------------------------
Crawl()
--> (URL, USER-AGENT)
| URL = str()
| USER-AGENT = True/False

Dirbrute()
--> (URL, USER-AGENT, COMMON, THREADS)
| URL = str()
| USER-AGENT = True/False
| COMMON = True/False
| THREADS = int(*)

DNSBrute()
--> (DOMAIN, THREADS, WORDLIST)
| DOMAIN = str()
| THREADS = int(*)
| WORDLIST = None/"A/Path/to" 
| (If None, a wordlist will be used in db/)
'''
__author__	= "helix"
__copyright__ 	= "Copyright (c) 2018, Helix." 
__credits__ 	= ["MorpheusTor"]
# __version__ 	= Defined in crawly/core/version.py

# Modules:
from crawly import Runner

class Crawly:
	def __init__(self):
		'''
		Running Init() to lunch
		the program.
		'''
		self.run = Runner.Init()

if __name__ == '__main__':
	Crawly()