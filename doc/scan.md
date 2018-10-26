# Scan

# File

- [x] scan.py

This file contains scanning classes of crawly. Each class instancied is auto runned with the given paremeters.

# Crawler
```
# CLI command
crawly -u https://www.google.com/ --crawl 
crawly -u https://www.google.com/ --crawl --random-agent
```
```python
  class Crawl:
    __init__(self, URL, AGENT=True)
    
>>> from crawly import Crawl
>>> Crawl("https://www.google.com")
>>> Crawl("https://www.google.com", True/False) # True is for a random user-agent.
```

# Dirbruter
```
# CLI commands
crawly -u https://www.google.com/ --dir
crawly -u https://www.google.com/ --common
crawly -u https://www.google.com/ --dir --random-agent -c "200,302,403"
crawly -u https://www.google.com/ --dir --output="/home/user/.crawly/report.txt" -t 40
```
```python
  class Dirbrute:
    __init__(self, URL, AGENT=True, COMMON=False, WORDLIST=None, 
    THREADS=35, CODES=["200"], REPORT=False, OUTPUT=None)

>>> from crawly import Dirbrute
>>> Dirbrute("https://www.google.com/")
>>> Dirbrute("https://www.google.com/", COMMON=True)
```
```
AGENT = True for a random user-agent
COMMON = True for a wordlist with most common directories (this option cannot work with a wordlist != None)
WORDLIST = "/path/to/word.txt", if WORDLIST is None a wordlist will be used in db/ directory
THREADS = int for the number of threads
CODES = list of HTTP codes to test, default 200
REPORT = True or False, if True a file will be created with a gived path
OUTPUT = None or "path/report.txt"
````

# DNS bruter
```
# CLI commands
crawly -u https://www.google.com/ --dns
crawly -u https://www.google.com/ --dns -t 15
crawly -u https://www.google.com/ --dns --output="/home/user/.crawly/report.txt" -t 40
```
```python
  class DNSBrute:
    __init__(self, URL, THREADS=35, WORDLIST=None, REPORT=False, OUTPUT=None)

>>> from crawly import DNSBrute
>>> DNSBrute("https://www.google.com/")
>>> DNSBrute("https://www.google.com/", WORDLIST="dns.list")
```
