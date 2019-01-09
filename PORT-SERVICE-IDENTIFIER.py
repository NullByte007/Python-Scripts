#!/usr/bin/python3
import socket
import os
os.system("pip install colorama==0.3.3")
from colorama import Fore, Back, Style
os.system("clear")
print(Fore.GREEN + Style.BRIGHT + "") 
print("		 ____   ___  ____ _____   ____  _____ ______     _____ ____ _____  ")
print("		|  _ \ / _ \|  _ \_   _| / ___|| ____|  _ \ \   / /_ _/ ___| ____| ")
print("		| |_) | | | | |_) || |   \___ \|  _| | |_) \ \ / / | | |   |  _|  ")
print("		|  __/| |_| |  _ < | |    ___) | |___|  _ < \ V /  | | |___| |___ ")
print("		|_|    \___/|_| \_\|_|   |____/|_____|_| \_\ \_/  |___\____|_____|  ")                                                         
print("		 ___ ____  _____ _   _ _____ ___ _____ ___ _____ ____   ")
print("		|_ _|  _ \| ____| \ | |_   _|_ _|  ___|_ _| ____|  _ \  ")
print("		 | || | | |  _| |  \| | | |  | || |_   | ||  _| | |_) | ")
print("		 | || |_| | |___| |\  | | |  | ||  _|  | || |___|  _ <  ")
print("		|___|____/|_____|_| \_| |_| |___|_|   |___|_____|_| \_\ ")
print("		--------------------------------------------------------------------")
print("                                                     [ ~NULLBYTE007]")
print("		--------------------------------------------------------------------")
print("\n")
print(Fore.CYAN + Style.BRIGHT + "")
port_input = input("INPUT PORT NUMBERS : ")
print(Fore.GREEN + Style.BRIGHT + "")
port_input = port_input.split(" ")
print(port_input)
print("--------------------------------------------------------------------------------")	
for (count,x) in enumerate(port_input) :
	try:
		print("\n[*]Service Running on -->> " + str(x) + " is : \" " + socket.getservbyport(int(x)) + "\"")
		#print(count)   Use this to just count the actual count going on 
	except:
		print("\n!!! [*]No Service exists on PORT !!! : --> " + str(x))
		pass
	
	if count > len(port_input):
		break
	print("--------------------------------------------------------------------------------")	