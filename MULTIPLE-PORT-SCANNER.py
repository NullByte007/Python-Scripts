#!/usr/bin/python3
# libraries 
import os
import socket
os.system("pip install colorama==0.3.3")
from colorama import Fore, Back, Style
os.system("clear")
print(Fore.GREEN + Style.BRIGHT + "")  	
print("		 __  __ _   _ _   _____ ___ ____  _     _____      ____   ___  ____ _____ ") 
print("		|  \/  | | | | | |_   _|_ _|  _ \| |   | ____|    |  _ \ / _ \|  _ \_   _| ")
print("		| |\/| | | | | |   | |  | || |_) | |   |  _| _____| |_) | | | | |_) || |  ")
print("		| |  | | |_| | |___| |  | ||  __/| |___| |__|_____|  __/| |_| |  _ < | |  ")
print("		|_|  |_|\___/|_____|_| |___|_|   |_____|_____|    |_|    \___/|_| \_\|_|   ")                                                                      
print("		 ____   ____    _    _   _ _   _ _____ ____   ")
print("		/ ___| / ___|  / \  | \ | | \ | | ____|  _ \  ")
print("		\___ \| |     / _ \ |  \| |  \| |  _| | |_) | ")
print("		 ___) | |___ / ___ \| |\  | |\  | |___|  _ <  ")
print("		|____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\ ")                                            
print("		--------------------------------------------------------------------")
print("                                                     [ ~NULLBYTE007]")
print("		--------------------------------------------------------------------")
host_name = socket.gethostname()
host_ip_address = socket.gethostbyname(host_name)
print(Fore.CYAN + Style.BRIGHT + "")
ip_range = input("Input the Port range for Scan\nExample : 100-200\n  -->> ")
print(Fore.GREEN + Style.BRIGHT + "")
ip_range = ip_range.split("-")
for x in range(int(ip_range[0]),int(ip_range[1])):
	try:
		print("\nHost Name : " + str(host_name) + " Has Ip address : " + str(host_ip_address) + " Has -->>  \"" + socket.getservbyport(x) + "\" <<-- Running on Port : " + str(x))
	except:
		pass
		
	if x != 100:	
		continue	
	