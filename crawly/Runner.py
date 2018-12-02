# -*- coding: utf-8 -*-
# Part of crawly2

import sys
from optparse import *
import random
import platform
# Modules:
from core import headers as heads
from core import tool
from core import errors
from core import version
from lib import scan as s
from lib import attack as a
from lib import framework as f

class Init:
	def __init__(self):
		self.c = heads.Strings()
		self.help = heads.Strings().help()
		self.version = version.__version__
		self.usage = heads.Strings().usage()
		self.headers = heads.Strings().randheaders()
		self.tool = tool.Tools()
		self.f = f.Framework()
		# Running the other classes and starting the program.
		self.main()

	def main(self):
		parser = OptionParser(add_help_option=False)
		parser.add_option("-h", "--help", dest="help", action="store_true")
		parser.add_option("--usage", action="store_true")
		parser.add_option("--version", "-v", action="store_true")
		parser.add_option("--check-update", dest="update", action="store_true")
		parser.add_option("--upgrade", action="store_true")
		parser.add_option("--refresh", action="store_true")
		parser.add_option("-u", "--url")
		parser.add_option("-f", "--file", help="url file")
		parser.add_option("-o", "--output")
		parser.add_option("--crawl", action="store_true")
		parser.add_option("--dir", action="store_true")
                parser.add_option("--lfi", action="store_true")
		parser.add_option("--random-agent", dest="useragent", action="store_true")
		parser.add_option("--common", dest="common", action="store_true")
		parser.add_option("--dns", action="store_true")
		parser.add_option("-c", dest="code", type="string")
		parser.add_option("-t", "--threads", default=35)
		parser.add_option("-w", "--wordlist")
		# Attacks options:
		parser.add_option("-A", dest="attack")
		parser.add_option("-U", dest="userfield")
		parser.add_option("-P", dest="passfield")
		parser.add_option("-m", "--method")
		parser.add_option("--lhost")
		parser.add_option("--lport")
		parser.add_option("--user")
		parser.add_option("--err", dest="errmsg")
		parser.add_option("--shellshock", action="store_true")
		parser.add_option("--bashdoor", action="store_true")
		# Other options
		parser.add_option("--quiet", action="store_true")
		# Hidden option :p
		parser.add_option("--framework", action="store_true")

		(options, args) = parser.parse_args()

		URL = options.url
		URL_FILE = options.file
		WORDLIST = options.wordlist
		HTTP_CODE = options.code
		THREADS = options.threads
		RHOST = options.attack
		LHOST = options.lhost
		LPORT = options.lport
		OUTPUT = options.output

		USER = options.user
		USERFIELD = options.userfield
		PASSFIELD = options.passfield
		ERRORMSG = options.errmsg
		refresh = False

		# Printing headers
		if not options.quiet:
			if platform.system() == "Windows":
				print(self.headers[1])
			else:
				print(random.choice(self.headers))
		# Windows can't read some headers... :(
		
                if self.tool.isFirstRun() == False:
                    print(heads.Strings().FirstRun())
                    self.tool.UpFirstRun()
                    sys.exit(0)

                # Check every months for a new update.
                if self.tool.NeedMonthUpdate() == True:
                    self.tool.RunMonthUpdate()
                    sys.exit(0)

		if HTTP_CODE is not None:
			if " " in HTTP_CODE:
				print(self.c.ERROR + "Option -c must be declared like that : -c 403,302.")
				print(self.c.ERROR + "Please remove the spaces.")
				sys.exit(1)
			
			elif "," in HTTP_CODE:
				HTTP_CODE = HTTP_CODE.split(",")

			else:
				HTTP_CODE = [HTTP_CODE]
		else:
			HTTP_CODE = ["200"]

		REPORT = False
		if OUTPUT:
			REPORT = True

		if not (options.help or options.url or options.attack \
                        or options.usage or options.file or options.update \
                        or options.upgrade or options.framework \
                        or options.version or options.refresh):
			print(self.c.ERROR + "Not enough options.")
			print(self.c.ERROR + "Type 'crawly -[h/--help]' to see available options.")

		elif options.help:
                    print(self.help)

		elif options.usage:
			print(self.usage)

		elif options.version:
			print(self.c.INFO + "Crawly version: %s" %(self.version))

		elif options.url:
			if (options.dir and options.common):
				print(self.c.ERROR + "Conflicting options. Use only [--dir] or [--common], not both.")
				sys.exit(1)

			## Common is set to false while you don't use --common option.
			common = False
			## same for agent but for option --random-agent.
			agent = False
			wordlist = None

			try:
				self.tool.PrintHostInfos(URL)
			except errors.BadURLError:
				print(self.c.ERROR + "BadURLError, I cannot find http:// or https:// in this url.")
				sys.exit(1)

			if options.crawl:
				if options.useragent:
					agent = True

				s.Crawl(URL, agent)
				sys.exit(0)

			elif options.dir:
				if options.useragent:
					agent = True
				
				elif options.wordlist:
					wordlist = options.wordlist

				s.Dirbrute(URL, agent, common, wordlist, THREADS, HTTP_CODE, REPORT, OUTPUT)
				sys.exit(0)

			elif options.common:
				common = True
				if options.useragent:
					agent = True

				s.Dirbrute(URL, agent, common, wordlist, THREADS, HTTP_CODE, REPORT, OUTPUT)
				sys.exit(0)

			elif options.dns:
				wordlist = None
				if options.wordlist:
					wordlist = options.wordlist

				s.DNSBrute(URL, THREADS, wordlist, REPORT, OUTPUT)
				sys.exit(0)

                        elif options.lfi:
                            wordlist = None
                            if options.wordlist:
                                wordlist = options.wordlist

                            s.LFIBrute(URL, wordlist, THREADS, REPORT, OUTPUT, agent)
                            sys.exit(0)

			print(self.c.OOPS + "Humm, i don't have enough options to work, mate :)")

		elif options.attack:
			if options.shellshock:
				a.Shellshock(RHOST)
				sys.exit(0)

			elif options.bashdoor:
				a.Bashdoor(RHOST, LHOST, LPORT)
				sys.exit(0)

			elif options.method:
				if options.method.lower() == "http":
					a.HTTPBrute(RHOST, USER, WORDLIST, THREADS)
					sys.exit(0)

				elif options.method.lower() == "ssh":
					print(self.c.OOPS + "I'm working on it....")
					sys.exit(1)

				elif options.method.lower() == "html":
					#def __init__(self, URL, USERFIELD, PASSFIELD, ERRORMSG, USER, WORDLIST, THREADS):
					a.HTMLBrute(RHOST, USERFIELD, PASSFIELD, ERRORMSG, USER, WORDLIST, THREADS)
					sys.exit(0)

			print(self.c.OOPS + "I like to eat some servers, but... There's not enough options.")
				
		elif options.file:
			'''
			Option file act like url option
			but can read multiples URLs

			TODO: Change the work process
			of this option...
			'''
			if (options.dir and options.common):
				print(self.c.ERROR + "Theses options are in conflict. Use only [--dir] or [--common], not both.")
				sys.exit(1)

			## Common is set to false while you don't use --common option.
			common = False
			## same for agent but for option --random-agent.
			agent = False
			wordlist = None

			with open(URL_FILE, "r") as file:
				file = file.readlines()

			for i in file:
				i = i.strip("\n")
				URL2 = i

				print("\n")
				self.tool.PrintHostInfos(URL2)

				if options.crawl:
					if options.useragent:
						agent = True

					s.Crawl(URL2, agent)

				elif options.dir:
					if options.useragent:
						agent = True
				
					if options.wordlist:
						wordlist = options.wordlist

					s.Dirbrute(URL2, agent, common, wordlist, THREADS, HTTP_CODE, REPORT, OUTPUT)

				elif options.common:
					common = True
					if options.useragent:
						agent = True

					s.Dirbrute(URL2, agent, common, wordlist, THREADS, HTTP_CODE, REPORT, OUTPUT)

				elif options.dns:
					wordlist = None
					if options.wordlist:
						wordlist = options.wordlist

					s.DNSBrute(URL2, THREADS, wordlist, REPORT, OUTPUT)

		elif options.framework:
			#print self.c.OH + "It's an hidden feature well done..."
			#print self.c.INFO + "I'm working on it."
			#sys.exit(1)
			print(self.c.OH + "Welcome to the Crawly framework...")
			self.f.run()

		elif options.update:
			self.tool.CheckUpdate()
			sys.exit(0)
		
		elif options.refresh:
			refresh = True
			self.tool.Upgrade(refresh)

		elif options.upgrade:
			self.tool.Upgrade(refresh)
			sys.exit(0)

def run():
    '''
    Crawly needs this function,
    To run the program with 
    console scripts.
    '''
    colors = heads.Strings()
    try:
    	Init()
    except KeyboardInterrupt:
    	print("\n" + colors.INFO + "CTRL + C signal found! Exiting...")
    	sys.exit(1)
