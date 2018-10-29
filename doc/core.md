# Core

Files
----

- [x] errors.py
- [x] headers.py
- [x] http.py
- [x] stdout.py
- [x] tool.py
- [ ] version.py (useless for you)

## Errors

The file errors.py define two crawly errors to be raised.
```python
  class WindowsError(Exception)
       # Raise an error when Windows is not compatible
       # With Crawly.
  
  class BadURLError(Exception)
       # Raise an error when the URL does not contain
       # 'http' or 'https'
```

## Headers

This file contains predefined colored strings,
Strings can detect which platform is used and adapt to unix or windows.

```python
  class Strings:
      ...
>>> from crawly import Strings
>>> color = Strings()
>>> print color.R + "RED msg" + color.O
```

There is many colors:
```
   Strings().R = RED
   Strings().G = GREEN
   ...Y = YELLOW
   ...B = BLUE
   ...BOLD = BOLD
   ...O = RESET COLORS
   ...ERROR = RED + "[ERROR]" + RESET
   ...PASS = GREEN + "[+]" + RESET
   ...INFO = BLUE + BOLD + "[INFO]" + RESET
   ...MED = YELLOW + "[~]" + RESET
```
## HTTP module

This file is an HTTP module to replace URL, like Ruby. [HTTP module in Ruby](https://ruby-doc.org/stdlib-2.4.2/libdoc/net/http/rdoc/Net/HTTP.html)

```python
  class URI:
    ...
    # Contains
    port()
    host()
    path()
    prepare()

>>> from crawly import URI
>>> uri = URI("http://test.com/path")
>>> uri.port()
80
>>> uri.host()
'test.com'
>>> uri.path()
'/path'
>>> uri.prepare()
'http://test.com/path/'
```
  
## Stdout file

This file is not realy useful for you.. It is a wrapped print which can avoid threads print errors

```python
  class CLI(COLOR="", MSG=""):
    write()

>>> from crawly import CLI
>>> CLI("Msg").write()
Msg
>>> CLI("\033[1m", "bold msg").write()
bold msg
```

## Tool 
  
 Tool contains a lot of methods, but only two are useful for you.
 
 ```python
  class Tools:
      PrintHostInfos()
      randomagent()
      
>>> from crawly import Tools
>>> Tools().PrintHostInfos("https://google.com/")
[INFO] URL to scan : https://google.com/
[INFO] Server IP : 216.58.204.142
[INFO] Port : 443
[INFO] Server : gws
>>>
>>> Tools.randomagent()
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8) Gecko/20060118 Firefox/1.5'
```
  
  
