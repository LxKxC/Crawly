# -*- coding: utf-8 -*-
# Part of Crawly2

class CLI:
	def __init__(self, MSG="", REPORT=False, PATH=None):
		self.MSG = MSG
		self.REPORT = REPORT
		self.PATH = PATH

	def write(self):
		# Making a safe multi-threaded print
		print "{0}\n".format(self.MSG),

		if self.report != False:
			with open(self.PATH, "a") as output:
				output.write(self.PATH+"\n")


