# -*- coding: utf-8 -*-
# Part of crawly2

import sys
import os
import datetime
import platform
import socket
import random
import requests
from bs4 import BeautifulSoup
# Modules
from . import headers as h
from . import version
from . import http

class Tools:
	def __init__(self):
		self.DIR = os.path.expanduser("~/.crawly/")
		self.FILE = "run.check"
		self.MONTH_FILE = "month.check"
		self.c = h.Strings()
		self.v = float(version.__version__)

	def GetHostInfos(self, HOST):
		'''
		This function returns strings of
		host informations
		ex. : "URL", "IP", "PORT", "SERVER_TYPE"
		'''
		# Constant variable
		URI = http.URI(HOST)
		URL = URI.prepare()

		# Resolving URL.
		try:
			IP = socket.gethostbyname(URI.host())
		except socket.gaierror:
			print(self.c.ERROR + "It's not a valid URL or the URL is not reachable...")
			sys.exit(1)

		PORT = str(URI.port())
		
		try:
			r = requests.get(URL)
		except requests.exceptions.SSLError:
			print(self.c.ERROR + "SSLError, please retry with an http connection.")
			sys.exit(1)
			
		try:
			SERVER = r.headers['Server']
		except KeyError:
			SERVER = "Not Resolved"

		if SERVER is None:
			SERVER = "NoneType"

		return [URL, IP, PORT, SERVER]

	def PrintHostInfos(self, HOST):
		c = h.Strings()
		URL, IP, PORT, SERVER = self.GetHostInfos(HOST)
		print(self.c.INFO + "URL to scan : " + URL)
		print(self.c.INFO + "Server IP : " + IP)
		print(self.c.INFO + "Port : "+PORT)
		print(self.c.INFO + "Server : "+SERVER + "\n")

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
			print(self.c.INFO + "Github crawly version : %s" %(str(current_version)))
			print(self.c.INFO + "Your crawly version : %s" %(str(self.v)))
			print(self.c.OH + "New version available. Type 'crawly --upgrade' to get the latest version.")
		
		elif current_version == self.v:
			print(self.c.INFO + "Crawly is up to date.")
			print(self.c.INFO + "Version: %s" %(str(current_version)))
        
        def NeedMonthUpdate(self):
            month = self.InitMonthUpdate()
            if month != datetime.datetime.now().month:
                return True
            else:
                return False

        def InitMonthUpdate(self):
            '''
            This function checks if
            crawly needs an update
            every months.
            Works like InitFirstRun()
            '''
            result = datetime.datetime.now().month
            if platform.system() != "Windows":
                if os.path.isfile(self.DIR + self.MONTH_FILE) == False:
                    f = open(self.DIR + self.MONTH_FILE, 'w')
                    f.write("Month=%d" %(datetime.datetime.now().month))
                    f.close()

                with open(self.DIR + self.MONTH_FILE, 'r') as check:
                    result = int(check.read().split("Month=")[1])

            return result

        def RunMonthUpdate(self):
            if self.InitMonthUpdate() < datetime.datetime.now().month:
                response = raw_input(self.c.PLUS + "Do you want to check if crawly is up-to-date and upgrade it ? [Y/N] > ").upper()
                if response == "Y":
                    print("")
                    self.Upgrade(False)
                else:
                    print(self.c.INFO + "Exiting...")

                with open(self.DIR + self.MONTH_FILE, 'w') as file:
                    file.write("Month=%d" %(datetime.datetime.now().month))

        def InitFirstRun(self):
            '''
            This function checks if crawly
            is runned for the first time.
            If yes a file will be created
            Otherwise the program will run
            as usual.
            '''
            result = 1
            if platform.system() != "Windows":
                if os.path.exists(self.DIR) == False:
                    # Let's create the files.
                    os.makedirs(self.DIR)
                
                    f = open(self.DIR + self.FILE, 'w')
                    f.write("isRun=0")
                    f.close()

                with open(self.DIR + self.FILE, 'r') as check:
                    result = int(check.read().split("isRun=")[1])

            return result
        
        def isFirstRun(self):
            if self.InitFirstRun() == 0:
                return False
            else:
                return True

        def UpFirstRun(self):
            with open(self.DIR + self.FILE, "w") as file:
                file.write("isRun=1")

	def GetVersion(self):
		URL = "https://github.com/ZenixIs/Crawly/blob/master/crawly/core/version.py"
		out = requests.get(URL).text

		soup = BeautifulSoup(out, 'lxml')
		for i in soup.find_all("span", class_="pl-s"):
			i = i.text

		if "'" in i:
			curr = i.replace("'", "")

		return float(curr)

	def Upgrade(self, refresh):
		'''
		This function upgrade crawly
		via git :)
		'''
		script = """
		git clone https://github.com/ZenixIs/Crawly.git /tmp/crawly
		cd /tmp/crawly
		sudo python2.7 setup.py install
		cd ~
		sudo rm -rf /tmp/crawly/
		"""
		#win_script = """ """

		if platform.system() == "Windows":
			raise WindowsError("Can't upgrade crawly at this time on windows host. --> https://github.com/ZenixIs/Crawly")

		current_version = self.GetVersion()

		if refresh == False:
			if current_version > self.v:
				print(self.c.INFO + "Let's upgrade Crawly...")
				os.system("bash -c '%s'" % (script))
				print(self.c.OH + "Crawly is up-to-date :)")
			else:
				print(self.c.ERROR + "Can't upgrade crawly... Latest version installed [%s]" %(str(current_version)))
				print(self.c.INFO + "Try to use [--refresh] option, to refreshing files from github.")
	
		else:
			if current_version > self.v:
				print(self.c.INFO + "Let's upgrade Crawly...")
				os.system("bash -c '%s'" % (script))
				print(self.c.OH + "Crawly is up-to-date :)")
			else:
				print(self.c.INFO + "Refreshing files...")
				os.system("bash -c '%s'" %(script))
				print(self.c.INFO + "Crawly files are refreshed")
