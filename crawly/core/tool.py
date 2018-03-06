# -*- coding: utf-8 -*-
# Part of crawly2

import sys
import os
import platform
import socket
import random
import requests
from bs4 import BeautifulSoup
# Modules
from . import headers as h
from . import version

class Tools:
	def __init__(self):
		self.c = h.Strings()
		self.v = float(version.__version__)

	def GetHostInfos(self, HOST):
		'''
		This function returns strings of
		host informations
		ex. : "URL", "IP", "PORT", "SERVER_TYPE"
		'''
		# Constant variable
		URL, https = self.ReplacingURL(HOST)
		URLb = URL
		is_port = False
		port = None

		if ":" in URL:
			is_port = True
			# Splitting port to avoid socket error
			URL, port = URL.split(":")

		# Resolving URL.
		try:
			IP = socket.gethostbyname(URL)
		except socket.gaierror:
			print self.c.ERROR + "It's not a valid URL..."
			sys.exit(1)

		if is_port == True:
			PORT = port
		else:
			PORT = "80/443"

		if https == True:
			r = requests.get("https://" + URLb)
		else:
			r = requests.get("http://" + URLb)

		try:
			typeserv = r.headers['Server']
			SERVER = typeserv
		except KeyError:
			SERVER = "Not Resolved"

		if SERVER is None:
			SERVER = "NoneType"

		return [URL, IP, PORT, SERVER]

	def PrintHostInfos(self, HOST):
		c = h.Strings()
		URL, IP, PORT, SERVER = self.GetHostInfos(HOST)
		print self.c.INFO + "URL to scan : " + URL
		print self.c.INFO + "Server IP : " + IP
		print self.c.INFO + "Port : "+PORT
		print self.c.INFO + "Server : "+SERVER + "\n"

	def ReplacingURL(self, URL):
		'''
		This function returns a string of the
		URL replaced, and a booleen.
		url, bool = "test.com", [True/False]
		'''
	    ## URL settings // Your http or https url is not compatible with urllib2
		## As soon as the request is complete, I will solve that for you :)
		https = False

		if "http://" in URL:
			URL = URL.replace("http://", "")
		
		elif "https://" in URL:
			https = True
			URL = URL.replace("https://", "")
		
		## www.test.com/ -- '/' is not compatible either so I'll solve that for you :)
		if "/" in URL:
			URL = URL.replace("/", "")

		return URL, https

	def randomagent(self):
		'''
		This function need to be called
		When the --random-agent option
		is set.
		'''
		usera = []
		usera.append("Opera/8.51 (Windows NT 5.0; U; en)")
		usera.append("Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0")
		usera.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27")
		usera.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8) Gecko/20060118 Firefox/1.5")
		usera.append("Opera/9.63 (Macintosh; Intel Mac OS X; U; en) Presto/2.1.1")
		usera.append("Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
		return random.choice(usera)

	def CheckUpdate(self):
		'''
		This function check if a new commit
		has been efectued on github.
		To download the latest version :)
		'''
		current_version = self.GetVersion()

		if current_version > self.v:
			print self.c.INFO + "Github crawly version : %s" %(str(current_version))
			print self.c.INFO + "Your crawly version : %s" %(str(self.v))
			print self.c.OH + "New version available. Type 'crawly --upgrade' to get the latest version."
		
		elif current_version == self.v:
			print self.c.INFO + "Crawly is up to date."
			print self.c.INFO + "Version: %s" %(str(current_version))

	def GetVersion(self):

		URL = "https://github.com/ZenixIs/Crawly/blob/master/core/version.py"
		out = requests.get(URL).text

		soup = BeautifulSoup(out, 'lxml')
		for i in soup.find_all("span", class_="pl-s"):
			curr = i.text

		if "'" in curr:
			curr = curr.replace("'", "")

		return float(curr)

	def Upgrade(self):
		'''
		This function upgrade crawly
		via git :)
		'''
		script = """
		sudo rm -rf /usr/share/crawly/
		sudo rm /usr/bin/crawly

		git clone https://github.com/ZenixIs/Crawly.git /tmp/crawly
		cd /tmp/crawly
		chmod +x setup.sh
		./setup.sh install
		cd ~
		rm -rf /tmp/crawly/
		"""

		current_version = self.GetVersion()

		if current_version > self.v:
			print self.c.INFO + "Let's upgrade Crawly..."
			os.system("bash -c '%s'" % (script))
			print self.c.OH + "Crawly is up-to-date :)"

		else:
			print self.c.ERROR + "Can't upgrade crawly... Latest version installed [%s]" %(str(current_version))





