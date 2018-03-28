# -*- coding: utf-8 -*-
# Part of Crawly2

class CLI:
	def __init__(self, COLOR="", MSG="", REPORT=False, PATH=None):
		self.COLOR = COLOR
		self.MSG = MSG
		self.REPORT = REPORT
		self.PATH = PATH

	def write(self):
		# Making a safe multi-threaded print
		print "%s%s\n" % (self.COLOR, self.MSG),

		if self.REPORT != False:
			self.report()

	def report(self):
		with open(self.PATH, "a") as output:
			output.write(self.MSG+"\n")

	def InitReport(self):
		head = """
*********************************
         Crawly report
*********************************

"""

		with open(self.PATH, "a") as output:
			output = output.readlines()

		if not len(output):
			output.write(head+"\n")

		