from setuptools import *
import re

with open("README.md", "rb") as file:
    description = file.read().decode("utf-8")

# Regex section, to find the current
# version of the program.
version = re.search(
    "^__version__\s*=\s*'(.*)'",
    open('crawly/core/version.py').read(),
    re.M
    ).group(1)
 
 
setup(
    name = "Crawly",
    packages=find_packages(),
    package_dir={'crawly': 'crawly'},
    entry_points={
        'console_scripts': 
        [
            'crawly = crawly.Runner:run'
        ]
    },
    version = version,
    description = "Simple web scanner.",
    long_description = description,
    author = "Helix (@ZenixIs)",
    install_requires=['bs4', 'requests', 'dnspython', 'paramiko', 'lxml', 'httplib2', 'colorama'],
)
