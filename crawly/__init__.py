'''
Find the crawly documentation at :
>>> https://github.com/ZenixIs/Crawly/tree/master/doc
'''
# Infos
__author__    = "helix"
__copyright__ = "Copyright (c) 2018, Helix." 
__credits__   = ["MorpheusTor"]
# __version__ = Defined in crawly/core/version.py

# < Core files >
# Importing error classes
from core.errors import WindowsError
from core.errors import BadURLError
# Importing color strings
from core.headers import Strings
# Importing http URI module
from core.http import URI
# Importing CLI stdout module
from core.stdout import CLI
# Importing tool module
from core.tool import Tools
# Importing crawly version
from core.version import __version__
#
# < Lib files >
# Scan module
from lib.scan import Crawl
from lib.scan import Dirbrute
from lib.scan import DNSBrute
# Attack module
from lib.attack import Shellshock
from lib.attack import Bashdoor
from lib.attack import HTMLBrute
from lib.attack import HTTPBrute
from lib.attack import SSHBrute
