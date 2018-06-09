# Crawly

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

**Crawly is an open source multi-threaded web scanner and simple penetration testing tool.**

Crawly is developed in [Python](https://www.python.org/) by **Helix/@Jean-Mi**, with help of MorpheusTor (Langage correction)

**(Warning) Crawly at this time, works only on Py2.7**

Platforms
----

	Windows
	Linux
	MacOs

Tested on ArchLinux(4.15.3-1-ARCH), Ubuntu(4.13), Debian, BackBox, Kali Linux(4.12.0-kali1-amd64), Windows 10.

Installation
----


	git clone https://github.com/ZenixIs/Crawly.git

Go to directory:
	
	cd Crawly/

	python2.7 setup.py install

The windows setup can fail, you can fix the errors by installing the requirements with pip.
	
	pip install -r requirements.txt

Then
	
	crawly

An executable will be created with the setup.

Usage
----

List of options:

	crawly [-h/--help]

Show usage:

	crawly --usage

How to use the functions (example):
```python
	>>> from crawly import Crawl
	>>> Crawl("http://www.google.com")
	[!] Request under random User-Agent.
	[+] Found URL : http://www.google.ch/
	...
	>>> 
	>>> from crawly import Dirbrute
	>>> help(Dirbrute) # To see __init__ needed variables
```

See the complete documentation to **doc/**

ZenixIs, 2018.
