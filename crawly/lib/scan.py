# -*- coding: utf-8 -*-
# Part of crawly2

import sys
import re
import time
import urllib2
import dns.resolver
import threading
import Queue
import platform

# My modules
from ..core import tool as core
from ..core import http
from ..core import headers as head
from ..core import stdout

class Crawl:
	'''
	This class calls the web crawler
	It needs to be called like this :
	
	import scan
	scan.Crawl("www.whatever.com", True/False)
	[True or False represent the option 
	randomagent or not]

	I disabled the report
	option because it's not really
	useful.
	'''
	def __init__(self, URL, AGENT=True):
		self.c = head.Strings()
		#self.OUTPUT = "/usr/share/crawly/report.txt"
		self.tools = core.Tools()
		self.opener = urllib2.build_opener()
		self.URL = URL
		self.agent = AGENT
		self.run()

	def run(self):
		# Replacing the URL, [-http/-https/-'/']
		# and return a bool of the method
		# SSL or not.
		URL = http.URI(self.URL).prepare()
		
		if self.agent == True:
			print(self.c.INFO + "Request under random User-Agent.\n")
			self.opener.addheaders = [('User-Agent', self.tools.randomagent())]
		else:
			print(self.c.INFO + "Base User-Agent -- {'User-Agent': 'Helix/:)'}\n")
			self.opener.addheaders = [('User-Agent', 'Helix/:)')]

		out = self.opener.open(URL)

		# Reading html code to find URLs.
		# And remove duplicates links.

		read = str(out.read())
		extln = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', read)
		out = list(set(extln))
		num = len(out)
		num = str(num)

		for i in out:
			print(self.c.PASS + "Found URL : "+i)

		## Searching .css or .js files and images ##
		css = re.findall('href="?\'?([^"\'>]*)', read)
		out2 = list(set(css))

		for i in out2:
			if str('.css') in i:
				print(self.c.PASS + "Found CSS code : "+i)

		js_img = re.findall('src="?\'?([^"\'>]*)', read)
		out3 = list(set(js_img))

		for i in out3:
			if str('.js') in i:
				if "https://" in i:
					print(self.c.PASS + "Found external JS link : "+i)
				elif "http://" in i:
					print(self.c.PASS + "Found external JS link : "+i)
				else:
					print(self.c.PASS + "Found internal JS code : "+i)

		for i in out3:
			if str('.gif') in i:
				print(self.c.PASS + "Found image : "+i)
			elif str('.jpg') in i:
				print(self.c.PASS + "Found image : "+i)
			elif str('.jpeg') in i:
				print(self.c.PASS + "Found image : "+i)
			elif str('.png') in i:
				print(self.c.PASS + "Found image : "+i)

		print(self.c.MED + "Found %s true URLs." %(num))
		print(self.c.INFO + "Scan finished at "+time.strftime("%H:%M:%S"))

class Dirbrute:
	'''
	This class can dirbrute
	an host.
	With multi-threads.
	'''
	def __init__(self, URL, AGENT=True, COMMON=False, WORDLIST=None, 
		THREADS=35, CODES=["200"], REPORT=False, OUTPUT=None):
		self.tools = core.Tools()
		self.c = head.Strings()
		self.URL = URL
		self.AGENT = AGENT
		self.COMMON = COMMON
		self.WORDLIST = WORDLIST
		self.THREADS = THREADS
		self.CODES = CODES
		self.REPORT = REPORT
		self.OUTPUT = OUTPUT

		# Grrrrrr windows...
		if self.WORDLIST is None:
			if self.COMMON == True:
				if platform.system() != "Windows":
					self.WORDLIST = "/usr/share/crawly/db/common"
				else:
					self.WORDLIST = "C:/Program Files/Crawly/db/common"
			else:
				if platform.system() != "Windows":
					self.WORDLIST = "/usr/share/crawly/db/wordlist"
				else:
					self.WORDLIST = "C:/Program Files/Crawly/db/wordlist"

		self.multic = False
		if len(self.CODES) > 1:
			self.multic = True

		self.run()

	def brute(self, i, q):
		# http://site.com/path/
		URL = http.URI(self.URL).prepare()

		while True:
			i = q.get()

			link = URL + i

			if self.AGENT == True:
				req = urllib2.Request(link, headers={'User-Agent': self.tools.randomagent()})
			else:
				req = urllib2.Request(link, headers={'User-Agent': 'Helix/:)'})

			try:

				out = urllib2.urlopen(req)
				
				if len(out.read()):
					if ".pl" in link:
						stdout.CLI(self.c.PASS, "[shellshock?]: %s"%(link), self.REPORT, self.OUTPUT).write()
					elif ".cgi" in link:
						stdout.CLI(self.c.PASS, "[shellshock?]: %s"%(link), self.REPORT, self.OUTPUT).write()
					elif ".sh" in link:
						stdout.CLI(self.c.PASS, "[shellshock?]: %s"%(link), self.REPORT, self.OUTPUT).write()

					else:
						stdout.CLI(self.c.PASS, "Found [%d]: %s" %(out.code, link), self.REPORT, self.OUTPUT).write()

			except urllib2.HTTPError as e:
				if self.multic == True:
					for code in self.CODES:
						if int(code) == e.code:
							stdout.CLI(self.c.SEMI, "Found [%d]: %s" %(out.code, link), self.REPORT, self.OUTPUT).write()
				else:
					self.CODES = str(self.CODES).strip('[]')
					self.CODES = str(self.CODES).strip("'")
					if int(self.CODES) == e.code:
						stdout.CLI(self.c.SEMI, "Found [%d]: %s" %(out.code, link), self.REPORT, self.OUTPUT).write()
				
				pass

			except urllib2.URLError:
				pass

			finally:
				q.task_done()

			if platform.system() != "Windows":
				# There's some print fails here on windows.
				sys.stdout.write(self.c.INFO + "Directories to test: %d\r" % q.qsize())
				sys.stdout.flush()

	def run(self):
		q = Queue.Queue()

		if self.AGENT == True:
			print(self.c.INFO + "Using random-agent for requests.")
		else:
			print(self.c.INFO + "Using base User-Agent for requests : 'Helix/:)'")

		print(self.c.MED + "Starting : "+ str(self.THREADS) + " threads...")
		
		if self.multic == True:
			print(self.c.MED + "Searching with HTTP codes %s\n" %(str(self.CODES).strip('[]')))
		else:
			print(self.c.MED + "Searching with HTTP code %s\n" %(str(self.CODES).strip('[]')))


		with open(self.WORDLIST, "r") as l:
			for line in l:
				q.put(line.rstrip('\n\r'))

		start = time.time()
		for i in range(int(self.THREADS)):
			worker = threading.Thread(target=self.brute, args=(i, q))
			worker.setDaemon(True)
			worker.start()
			worker.join(1)

		q.join()

		elapsed = time.time() - start
		elapsed = round(elapsed)
		convert = time.strftime("%M:%S", time.gmtime(elapsed))
		print(self.c.INFO + "Elapsed time: %s" %str(convert))

class DNSBrute:
	'''
	This class brute some
	subdomains of an host
	'''
	def __init__(self, URL, THREADS=35, WORDLIST=None, REPORT=False, OUTPUT=None):
		self.tools = core.Tools()
		self.c = head.Strings()
		self.domain = http.URI(URL).host()
		self.THREADS = THREADS
		self.WORDLIST = WORDLIST
		self.REPORT = REPORT
		self.OUTPUT = OUTPUT

		if self.WORDLIST is None:
			if platform.system() != "Windows":
				self.WORDLIST = "/usr/share/crawly/db/subdomains"
			else:
				self.WORDLIST = "C:/Program Files/Crawly/db/subdomains"

		self.run()

	def GetNS(self):
		ns = dns.resolver.query(self.domain, "NS")
		for i in ns:
			print(self.c.SEMI + "Found NS records : "+str(i))

	def DNS(self, i, q):

		while True:
			i = q.get()

			try:
				subdomain = i + "." + self.domain
				dns.resolver.query(subdomain, 'a')

				stdout.CLI(self.c.PASS, "Found : %s" % subdomain, self.REPORT, self.OUTPUT).write()

			except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
				pass
			except TypeError:
				pass
			
			finally:
				q.task_done()

			if platform.system() != "Windows":
				# There's some print fails here on windows.
				sys.stdout.write(self.c.INFO + "Subdomains: [%d]\r" % q.qsize())
				sys.stdout.flush()

	def run(self):
		q = Queue.Queue()

		with open(self.WORDLIST, "r") as l:
			for line in l:
				q.put(line.rstrip('\n\r'))

		self.GetNS()

		for i in range(int(self.THREADS)):
			worker = threading.Thread(target=self.DNS, args=(i, q))
			worker.setDaemon(True)
			worker.start()
			worker.join(2)

		q.join()

		print(self.c.INFO + "Scan finished at: "+time.strftime('%H:%M:%S'))


class LFIBrute:
        """
        LFIBrute can scan for LFI vuln
        on a URL, you need to give me
        the full path...
        ex: "http://test.com/index.php?vuln=1"
        
        Contributor: @Seepcko
        """
	def __init__(self, URL, WORDLIST=None, THREADS=15, REPORT=False, OUTPUT=None, AGENT=True):
                self.c = head.Strings()
                self.URL = URL
                self.WORDLIST = WORDLIST
                self.THREADS = THREADS
		self.REPORT = REPORT
		self.OUTPUT = OUTPUT
		self.AGENT = AGENT

		if(self.WORDLIST is None):
			if(platform.system() != "Windows"):
				self.WORDLIST = "/usr/share/crawly/db/lfi"
			else:
				self.WORDLIST = "C:/Program Files/Crawly/db/lfi"

		if(http.URI(self.URL).isPath() == False):
			print(self.c.ERROR + "You need to enter a path for example http://localhost/index.php?id=index")
			sys.exit(0)

		self.run()

	def brute(self, i, q):

		URL = http.URI(self.URL).prepare()
		URL = self.URL.split("=")[0]
		URL = URL + "="

		while True:
			i = q.get()
			so = URL + i

			if self.AGENT == True:
				req = urllib2.Request(so, headers={'User-Agent': self.tools.randomagent()})
			else:
				req = urllib2.Request(so, headers={'User-Agent': 'Helix/:)'})

			try:
				out = urllib2.urlopen(req).read()

				if("root:" in out):
					stdout.CLI(self.c.PASS, "[lfi?]: %s"%(so), self.REPORT, self.OUTPUT).write()

			except urllib2.HTTPError as e:
				pass
			except urllib2.URLError:
				pass
			finally:
                                q.task_done()
                                
                        if platform.system() != "Windows":
                            # There's some print fails here on windows.
                            sys.stdout.write(self.c.INFO + "Remaining tests: %d\r" % q.qsize())
                            sys.stdout.flush()
                        
                        if q.qsize() == 0:
                            sys.stdout.write("\033[F") # Back to previous line
                            sys.stdout.write("\033[K") # Clear line
                            print("\n" + self.c.INFO + "Waiting for threads to exit...")
                            sys.stdout.flush()


	def run(self):
		q = Queue.Queue()

		with open(self.WORDLIST, "r") as l:
			for line in l:
				q.put(line.rstrip('\n\r'))

		for i in range(int(self.THREADS)):
			worker = threading.Thread(target=self.brute, args=(i, q))
			worker.setDaemon(True)
			worker.start()
			worker.join(2)

		q.join()

                print(self.c.INFO + "Scan finished at: "+time.strftime('%H:%M:%S'))

