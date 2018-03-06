# Crawly

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

**Crawly is an open source multi-threaded web scanner and simple penetration testing tool.**

Crawly is developed in [Python](https://www.python.org/) by **Helix**, for the **DGSquad** with help of MorpheusTor (Langage correction)

**(Warning) Crawly works only on Py2.7**

Platforms
---

	Linux
	MacOs

Tested on ArchLinux(4.15.3-1-ARCH), Ubuntu(4.13), Debian, BackBox(), Kali Linux(4.12.0-kali1-amd64)

Installation
----

	git clone https://github.com/ZenixIs/Crawly.git

Go to directory:
	
	cd crawly2/

	sudo python2.7 setup.py install
	

Then
	
	crawly

crawly.py will be moved to **/usr/bin/crawly** after running the setup.

Usage
----

List of options:

	crawly [-h/--help]

Show usage:

	crawly --usage

Simple Documentation
---

Crawly has 3 scan modules :

	'import scan'
	Crawl()
	Dirbrute()
	DNSBrute() 

and at this time 5 simple attack scripts:

	'import attack'
	Shellshock()
	Bashdoor()
	HTMLBrute()
	HTTPBrute()
	SSHBrute()

And some little tools:

	'import tool'
	GetHostInfos()
	ReplacingURL()
	PrintHostInfos()
	randomagent()

How to use the functions (example):

	>>> from crawly.lib import scan as s
	>>> s.Crawl("www.google.com", True) # True is for a random-agent or not.
	[!] Request under random User-Agent.
	[+] Found URL : http://www.google.ch/setprefs?sig=0_87XNjV5P2-tqXi8BJEEeNKAQVg8%3D&amp;hl=en&amp;source=homepage&amp;sa=X&amp
	...
	>>>
	>>> help(s.Dirbrute) # To see the methods in the __init__

### TODO

- [x] Add options file to brute many URLs.
- [x] Add some error messages.
- [x] Dev SSH and HTML bruteforcer.
- [x] Add best functions to the setup.
- [x] Adding safe print with threads.
- [ ] Proxy pivoting option (requesting mode)
