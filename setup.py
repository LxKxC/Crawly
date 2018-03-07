import re
from setuptools import setup, find_packages

with open("README.md", "rb") as f:
    description = f.read().decode("utf-8")


version = re.search(
    "^__version__\s*=\s*'(.*)'",
    open('crawly/core/version.py').read(),
    re.M
    ).group(1)
 
 
setup(
    name = "Crawly",
    packages=find_packages(),
    package_dir={'crawly': 'crawly/'},
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