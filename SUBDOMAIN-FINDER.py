#!/usr/bin/python3
# libraries 
import os
print("[*] Downloading Required Library...")
os.system("pip install colorama==0.3.3")
from colorama import Fore, Back, Style
os.system("clear")
print(Fore.GREEN + Style.BRIGHT + "") 	 
print("		--------------------------------------------------------------------")
print("		 ____  _   _ ____        ____   ___  __  __    _    ___ _   _")
print("		/ ___|| | | | __ )      |  _ \ / _ \|  \/  |  / \  |_ _| \ | |")
print("		\___ \| | | |  _ \ _____| | | | | | | |\/| | / _ \  | ||  \| |")
print("		 ___) | |_| | |_) |_____| |_| | |_| | |  | |/ ___ \ | || |\  |")
print("		|____/ \___/|____/      |____/ \___/|_|  |_/_/   \_\___|_| \_| ")                                                     
print("		 _____ ___ _   _ ____  _____ ____  ")
print("		|  ___|_ _| \ | |  _ \| ____|  _ \ ")
print("		| |_   | ||  \| | | | |  _| | |_) |")
print("		|  _|  | || |\  | |_| | |___|  _ < ")
print("		|_|   |___|_| \_|____/|_____|_| \_\ ")
print("		--------------------------------------------------------------------")
print(Fore.RED + Style.BRIGHT + "")
print("                                                              [ ~ #Code By: Aniket.N.Bhagwate]")
print(Fore.GREEN + Style.BRIGHT + "")
print("		--------------------------------------------------------------------")
os.system("rm -rf index.html*")
print(Fore.CYAN + Style.BRIGHT + "")
print("[*] INPUT DOMAIN \nExample:www.google.com\n\n")
print(Fore.YELLOW + Style.BRIGHT + "")
domain =  input("DOMAIN -> ")
print(" ")
print(Fore.CYAN + Style.BRIGHT + "")
print(Fore.GREEN + Style.BRIGHT + "")
print("[*] FINDING ALL SUBDOMAINS FOR --> {}".format(domain))
print("\n\n")
os.system("wget {}".format(domain))
main_domain_keyword = domain.split(".")
main_domain_keyword = main_domain_keyword[1]+"."+main_domain_keyword[2]

os.system("cat index.html | grep 'href=' | cut -d'/' -f3  | cut -d'\"' -f1 | grep '{}' | sort -u > subdomains.txt".format(main_domain_keyword))

print(Fore.CYAN + Style.BRIGHT + "")
# 								^^^^
# HERE we are using \" instead of just " , due to colon issue becoz python -> \" <- as -> " <-
print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
os.system("cat subdomains.txt")
print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
print(Fore.GREEN + Style.BRIGHT + "")

print("[*] Successfully found all possible subdomains !")
print(" ")
print("[*] FILE CREATED : subdomains.txt")

choice = "yes"

print("[*] YOU WANT THEIR RESPECTIVE IP ADDRESSES ? :[yes/no].. [DEFAULT : yes] : ")
choice = input(" ")

if choice=="no":
	print("Thank you for using SUBDOMAIN-FINDER !!")
	exit(0)
	
print("[*] FINDING ALL THE IP ADDRESSES FOR ABOVE SUBDOMAINS !!")
f = open("subdomains.txt","r")
f = f.read();
f = f.split("\n")
f.pop()
os.system("touch subdomain-ip.txt")
r = open("subdomain-ip.txt" , "a")
os.system("echo 'start------------------------------------------------' > subdomain-ip.txt")    # This statement is to overwtite previous result
for dom in f:
	print("------------------------------------------------")
	print(Fore.CYAN + Style.BRIGHT +"{} ".format(dom)+Fore.GREEN + Style.BRIGHT+ "HAS ADDRESS:"+ Fore.GREEN + Style.BRIGHT)
	os.system("host {} | grep 'has address' | cut -d' ' -f4".format(dom))
	os.system("host {} | grep 'has address' | cut -d' ' -f4 >> subdomain-ip.txt".format(dom))
	print("\n")
	print("------------------------------------------------")
os.system("cat subdomain-ip.txt")
os.system("rm -rf index.html*")
	
