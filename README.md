# Crawly

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

**Crawly is an open source multi-threaded web scanner and simple penetration testing tool.**

Crawly is developed in [Python](https://www.python.org/) by **Helix/@Jean-Mi**, with help of MorpheusTor (Langage correction)

**(Warning) Crawly at this time, works only on Py2.7**

![screenshot](https://github.com/ZenixIs/Crawly/blob/master/screens/crawly_front.png)

You can visit the [screenshots](https://github.com/Crawly/blob/master/screens/)

Platforms
----

	Windows
	Linux
	MacOs

Tested on ArchLinux, Ubuntu, Debian, BackBox, Kali Linux, Windows 10.

Installation
----


	git clone https://github.com/ZenixIs/Crawly.git
	
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


See the complete documentation to **doc/**, to use crawly in your own program.

ZenixIs, 2018.
