# -*- coding: utf-8 -*-
# Part of crawly2

import sys
import re
import time
import urllib2
import dns.resolver
import threading
import Queue

# My modules
from ..core import tool as core
from ..core import headers as head

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
	usefull.
	'''
	def __init__(self, URL, AGENT):
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
		HOST, https = self.tools.ReplacingURL(self.URL)
		
		if self.agent == True:
			print self.c.INFO + "Request under random User-Agent.\n"
			self.opener.addheaders = [('User-agent', self.tools.randomagent())]
		else:
			print self.c.INFO + "Base User-Agent -- {'User-Agent': 'Helix/:)'}\n"
			self.opener.addheaders = [('User-agent', 'Helix/:)')]

		link = "http://" + HOST
		if https == True:
			link = "https://" + HOST ## Simple security.

		out = self.opener.open(link)

		# Reading html code to find URLs.
		# And remove duplicates links.

		read = str(out.read())
		extln = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', read)
		out = list(set(extln))
		num = len(out)
		num = str(num)

		for i in out:
			print self.c.PASS + "Found URL : "+i

		## Searching .css or .js files and images ##
		css = re.findall('href="?\'?([^"\'>]*)', read)
		out2 = list(set(css))

		for i in out2:
			if str('.css') in i:
				print self.c.PASS + "Found CSS code : "+i

		js_img = re.findall('src="?\'?([^"\'>]*)', read)
		out3 = list(set(js_img))

		for i in out3:
			if str('.js') in i:
				if "https://" in i:
					print self.c.PASS + "Found external JS link : "+i
				elif "http://" in i:
					print self.c.PASS + "Found external JS link : "+i
				else:
					print self.c.PASS + "Found internal JS code : "+i

		for i in out3:
			if str('.gif') in i:
				print self.c.PASS + "Found image : "+i
			elif str('.jpg') in i:
				print self.c.PASS + "Found image : "+i
			elif str('.jpeg') in i:
				print self.c.PASS + "Found image : "+i
			elif str('.png') in i:
				print self.c.PASS + "Found image : "+i

		print self.c.MED + "Found %s true URLs." %(num)
		print self.c.INFO + "Scan finished at "+time.strftime("%H:%M:%S")

class Dirbrute:
	'''
	This class can dirbrute
	an host.
	With multi-threads.
	'''
	def __init__(self, URL, AGENT, COMMON, WORDLIST, THREADS, CODES):
		self.tools = core.Tools()
		self.c = head.Strings()
		self.URL = URL
		self.AGENT = AGENT
		self.COMMON = COMMON
		self.THREADS = THREADS
		self.CODES = CODES
		self.WORDLIST = WORDLIST

		if self.WORDLIST is None:
			if self.COMMON == True:
				self.WORDLIST = "/usr/share/crawly/db/common"
			else:
				self.WORDLIST = "/usr/share/crawly/db/wordlist"

		self.multic = False
		if len(self.CODES) > 1:
			self.multic = True

		self.run()

	def brute(self, i, q):
		URL, https = self.tools.ReplacingURL(self.URL)

		while True:
			i = q.get()

			link = "http://" + URL + "/" + i
			
			if https == True:
				link = "https://" + URL + "/" + i

			if self.AGENT == True:
				req = urllib2.Request(link, headers={'User-Agent': self.tools.randomagent()})
			else:
				req = urllib2.Request(link, headers={'User-Agent': 'Helix/:)'})

			try:

				out = urllib2.urlopen(req)
				
				if len(out.read()):
					if ".pl" in str(link):
						print self.c.PASS + "[shellshock?]: %s\n"%(link),
					elif ".cgi" in str(link):
						print self.c.PASS + "[shellshock?]: %s\n"%(link),
					elif ".sh" in str(link):
						print self.c.PASS + "[shellshock?]: %s\n"%(link),

					else:
						print self.c.PASS + "Found [%d]: %s\n" %(out.code, link),
					
			except urllib2.HTTPError as e:
				if self.multic == True:
					for code in self.CODES:
						if int(code) == e.code:
							print self.c.SEMI + "Found [%d]: %s\n"%(e.code, link),
				else:
					self.CODES = str(self.CODES).strip('[]')
					self.CODES = str(self.CODES).strip("'")
					if int(self.CODES) == e.code:
						print self.c.SEMI + "Found [%d]: %s\n"%(e.code, link),
				
				pass

			except urllib2.BadStatusLine:
				pass
			
			finally:
				q.task_done()

			sys.stdout.write(self.c.INFO + "Directorys to test: %d\r" % q.qsize())
			sys.stdout.flush()

	def run(self):
		q = Queue.Queue()

		if self.AGENT == True:
			print self.c.INFO + "Using random-agent for requests."
		else:
			print self.c.INFO + "Using base User-Agent for requests : 'Helix/:)'"

		print self.c.MED + "Starting : "+ str(self.THREADS) + " threads..."
		
		if self.multic == True:
			print self.c.MED + "Searching with HTTP codes %s\n" %(str(self.CODES).strip('[]'))
		else:
			print self.c.MED + "Searching with HTTP code %s\n" %(str(self.CODES).strip('[]'))


		with open(self.WORDLIST, "r") as l:
			for line in l:
				q.put(line.rstrip('\n\r'))

		start = time.time()
		for i in range(int(self.THREADS)):
			worker = threading.Thread(target=self.brute, args=(i, q))
			worker.setDaemon(True)
			worker.start()

		q.join()

		elapsed = time.time() - start
		elapsed = round(elapsed)
		convert = time.strftime("%M:%S", time.gmtime(elapsed))
		print self.c.INFO + "Elapsed time: %s" %str(convert)

class DNSBrute:
	'''
	This class brute some
	subdomains of an host
	'''
	def __init__(self, URL, THREADS, WORDLIST):
		self.tools = core.Tools()
		self.c = head.Strings()
		self.domain = URL
		self.THREADS = THREADS
		self.WORDLIST = WORDLIST

		if self.WORDLIST is None:
			self.WORDLIST = "/usr/share/crawly/db/subdomains"

		self.run()

	def GetNS(self):
		ns = dns.resolver.query(self.domain, "NS")
		for i in ns:
			print self.c.SEMI + "Found NS records : "+str(i)

	def DNS(self, i, q):
		domain, var = self.tools.ReplacingURL(self.domain)

		while True:
			i = q.get()

			try:
				subdomain = i + "." + domain
				dns.resolver.query(subdomain, 'a')

				print self.c.PASS + "Found : "+subdomain + "\n",

			except dns.resolver.NXDOMAIN, dns.resolver.NoAnswer:
				pass
			except TypeError:
				pass
			
			finally:
				q.task_done()

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

		q.join()

		print self.c.INFO + "Scan finished at: "+time.strftime('%H:%M:%S')

