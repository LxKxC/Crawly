# Scan

# File

- [x] scan.py

This file contains scanning classes of crawly. Each class instancied is auto runned with the gived paremeters.

# Crawler

```python
  class Crawl:
    __init__(self, URL, AGENT=True)
    
>>> from crawly import Crawl
>>> Crawl("https://www.google.com")
>>> Crawl("https://www.google.com", True/False) # True is for a random user-agent.
```

# Dirbruter
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
COMMON = True for a wordlist with most common directorys (this option cannot work with a wordlist != None)
WORDLIST = "/path/to/word.txt", if WORDLIST is None a wordlist will be used in db/ directory
THREADS = int for the number of threads
CODES = list of HTTP codes to test, default 200
REPORT = True or False, if True a file will be created with a gived path
OUTPUT = None or "path/report.txt"
````

# DNS bruter

```python
  class DNSBrute:
    __init__(self, URL, THREADS=35, WORDLIST=None, REPORT=False, OUTPUT=None)

>>> from crawly import DNSBrute
>>>
```
