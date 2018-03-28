# -*- coding: utf-8 -*-
# Part of crawly2

class WindowsError(Exception):
	'''
	This error is raised when
	A class can't be runned
	On windows host.
	'''
	pass
	
class BadURLError(Exception):
	'''
	Error raised when
	the user forgot to
	enter an url with
	'http' or 'https'
	'''
	def __init__(self, URL):
		self.URL = URL

	def __str__(self):
		return "Unable to find 'http' or 'https' in %s" %(self.URL)