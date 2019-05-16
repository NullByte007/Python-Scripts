#!/usr/bin/python3
# Copyright 2019, Aniket.N.Bhagwate, All rights reserved.
# Date Created : 26 february 2019
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# libraries 
import os
banner = '''
|--------------------------------------------------------------------------------------|
|          _   _ _____ _____       __  __  ___  _   _ ___ _____ ___  ____              |
|	 | \ | | ____|_   _|     |  \/  |/ _ \| \ | |_ _|_   _/ _ \|  _ \    ||        |
|	 |  \| |  _|   | | _____ | |\/| | | | |  \| || |  | || | | | |_) |   ||	       |
|	 | |\  | |___  | | _____ | |  | | |_| | |\  || |  | || |_| |  _ <    ||        |
|	 |_| \_|_____| |_|       |_|  |_|\___/|_| \_|___| |_| \___/|_| \_\   ||	       |
|			 ____  _   _ ___ _____ _____ _____ ____  		       |
|			/ ___|| \ | |_ _|  ___|  ___| ____|  _ \ 		       |
|			\___ \|  \| || || |_  | |_  |  _| | |_) |		       |
|			 ___) | |\  || ||  _| |  _| | |___|  _ < 		       |
|			|____/|_| \_|___|_|   |_|   |_____|_| \_\		       |
|--------------------------------------------------------------------------------------|
|--------------------------------------------------------------------------------------|
| # CODE BY : ~NULLBYTE007		      					       |
|--------------------------------------------------------------------------------------|                                
'''

import os
os.system("pip install colorama==0.3.3")
from colorama import Fore, Back, Style
print("[*] Downloading Required Library...")
os.system("clear")
print(Fore.GREEN + Style.BRIGHT + "") 

def print_dash_line():
	print("|--------------------------------------------------------------|")


print(banner)

print("|-----------------------------------------|")
print("| [*] CURRENT NETWORK CONNECTION DETAILS  |")
print("|-----------------------------------------|\n")

try:
	print_dash_line()
	os.system('ifconfig | grep -m1 "inet " | cut -d"t" -f2 | cut -d"n" -f1 > info.txt')
	f = open("info.txt","r")
	f = f.read()
	f = str(f)
	print("-->  IP ADDRESS [IPV4] : " + Fore.CYAN + Style.BRIGHT + " {}".format(f) + Fore.GREEN + Style.BRIGHT )
	print_dash_line()

	os.system('ifconfig | grep -m 1 "inet6" | cut -d" " -f10 > info.txt')
	f = open("info.txt","r")
	f = f.read()
	f = str(f)
	print("-->  IP ADDRESS [IPV6] : " + Fore.CYAN + Style.BRIGHT + " {}".format(f) + Fore.GREEN + Style.BRIGHT) 
	print_dash_line()

	os.system('ifconfig | grep "broadcast " | cut -d" " -f16  > info.txt')
	f = open("info.txt","r")
	f = f.read()
	f = str(f)
	print("-->  BROADCAST ADDRESS : " + Fore.CYAN + Style.BRIGHT + " {}".format(f) + Fore.GREEN + Style.BRIGHT )
	print_dash_line()


	os.system('ifconfig | grep -m 1 "netmask" | cut -d"n" -f3 | cut -d" " -f2 > info.txt')
	f = open("info.txt","r")
	f = f.read()
	f = str(f)
	print("-->  SUBNET MASK : " + Fore.CYAN + Style.BRIGHT + " {}".format(f) + Fore.GREEN + Style.BRIGHT )
	print_dash_line()


	print("\n[*] PLEASE SELECT THE INTERFACE  YOU WISH TO CAPTURE TRAFFIC\n")
	os.system('nmcli device status | cut -d" " -f1 > networks.txt')
	f = open("networks.txt","r")
	f = f.read();
	f = f.split("\n")
	f.pop()	
	del f[0]
	rr=0
	for x in f:
		rr = rr+1
		print("|------------------------|")
		print("|"+Fore.CYAN + Style.BRIGHT + " [*] {} : {}".format(rr,x))
		print(Fore.GREEN + Style.BRIGHT + "|------------------------|")
	print("\n[*] TOTAL INTERFACES AVAILABLE : {}".format(rr))
	choice = int(input("[*] ==> "))
	ifname = f[choice-1]
	print("[*] YOU SELECTED ==>"+Fore.CYAN + Style.BRIGHT +" {}".format(ifname) + Fore.GREEN + Style.BRIGHT )


	options = '''

|--------------------------------------------|
| [*] SELECT FILTERS FROM THE GIVEN OPTIONS  |
|--------------------------------------------|
|--------------------------------------------|	
| [1] HTTP				     |
| [2] HTTPS 				     |
| [3] DNS				     |
| [4] ICMP (ping packets)		     |
| [5] ARP				     |
| [6] NO FILTER				     |
| [7] ENTER PORT !			     |
|--------------------------------------------|
	'''

	print(Fore.WHITE + Style.BRIGHT + options +Fore.GREEN + Style.BRIGHT )

	choice = int(input("[*] ==> "))


## MAIN FUNCTION INFORMING THE SCAN-----------------------------------------------------------------------------------------------------

	def choice_body(par1,par2):
		print("[*] CAPTURING PACKETS ON INTERFACE"+Fore.CYAN + Style.BRIGHT + " {} ".format(par1) + Fore.GREEN + Style.BRIGHT +"WITH "+Fore.CYAN+ Style.BRIGHT + " {} ".format(par2)+Fore.GREEN + Style.BRIGHT +" PORT")

		os.system('tcpdump -i {} port {} | cut -d"," -f1 '.format(par1,par2))
# --------------------------------------------------------------------------------------------------------------------------------------

	if choice==1:
		choice_body(ifname,80)		# FOR HTTP

	elif choice==2:
		choice_body(ifname,443)		# FOR HTTPS

	elif choice==3:
		choice_body(ifname,53)		# FOR DNS

	elif choice==4:
		os.system('tcpdump -n -i {} icmp | cut -d"," -f1,4 '.format(ifname))		# FOR ICMP

	elif choice==5:
		os.system('tcpdump -n  -i {} arp'.format(ifname))		# FOR ARP	

	elif choice==6:
		os.system('tcpdump -n  -i {}'.format(ifname))		# FOR NO FILTER SCAN
	elif choice==7:
		port = int(input("[*] PLEASE ENTER THE PORT : "))
		os.system('tcpdump -XX -i eth0 port {}'.format(port))

#os.system('tcpdump -n -i {} port {} | cut -d"," -f1 '.format(ifname,80))
	
except:
	print("\n")
	print_dash_line()
	print(Fore.RED + Style.BRIGHT +" ===> PLEASE ENTER VALID INFORMATION <=== "+Fore.GREEN + Style.BRIGHT)
	print_dash_line()
	print("\n")
	

