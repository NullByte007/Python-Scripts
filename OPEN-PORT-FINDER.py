#!/usr/bin/python3
# Copyright 2019, Aniket.N.Bhagwate, All rights reserved.
# Date Created : 2 February 2019
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
#libraries
import os
import socket
print("[*] Downloading Required Library...")
os.system("pip install colorama==0.3.3")
from colorama import Fore, Back, Style
os.system("clear")
print(Fore.GREEN + Style.BRIGHT + "") 

a = """
		------------------------------------------------
		|	  ___       ____       ____            |
		|	 / _ \     |  _ \     / ___|           |
		|	| | | |    | |_) |    \___ \           |
		|	| |_| |PEN |  __/ ORT  ___) |CANNER    |
		|	 \___/     |_|        |____/           |
		|----------------------------------------------|
"""
print(a)
print("		------------------------------------------------")
print(Fore.RED + Style.BRIGHT + "")
print("                                         [ ~Aniket.N.Bhagwate]")
print(Fore.GREEN + Style.BRIGHT + "")
print("		------------------------------------------------")


menu = """
|-------------------------------|
| [*] CHOOSE FROM THE OPTIONS   |
|-------------------------------|
| 1 |	LOCALHOST		|
|-------------------------------|
| 2 |	REMOTE-HOST		|
|-------------------------------|
| 3 |	IMPORT FROM FILE	|
|-------------------------------|
"""

print(menu)
choice = int(input("==>> "))


#ifconfig | grep -m1 "inet " | cut -d"t" -f2 | cut -d"n" -f1 

if choice==1:
	print("[*] [OPTION 1: LOCALHOST]")
	print("SCAN REPORT FOR  ==>> {}".format(os.system("ifconfig | grep -m1 'inet ' | cut -d't' -f 2 | cut -d'n' -f1")))
	os.system("ifconfig | grep -m1 'inet ' | cut -d't' -f 2 | cut -d'n' -f1")
	print("----------------------------")
	print("\n[*] OPEN PORTS : \n")
	os.system("nc -nv -z {} {} 2> choice1.txt".format(os.system("ifconfig | grep -m1 'inet ' | cut -d't' -f2 | cut -d'n' -f1 "),"1-1023"))
	os.system("cat choice1.txt | cut -d']' -f2 | cut -d'(' -f1 > ports.txt")
	f = open("ports.txt","r")
	f = f.read()
	f = f.split("\n")
	f.pop()
	print("\n")
	for x in f:
		print("[{}] has Service : ".format(x) + socket.getservbyport(int(x)))
	os.system("rm -rf choice*")
		
		
elif choice==2:
	
	add = input("Input Remote address : ")
	print("Performing Port Scan on HOST Address :>>\n----------------------------")
	print(add)
	print("----------------------------")
	print("\n[*] OPEN PORTS : \n")
	os.system("nc -nv -z {} {} 2> choice2.txt".format(add,"1-1023"))
	os.system("cat choice2.txt | cut -d']' -f2| cut -d'(' -f1 > ports.txt")
	f = open("ports.txt","r")
	f = f.read()
	f = f.split("\n")
	f.pop()
	print("\n")
	for x in f:
		print("[{}] has Service : ".format(x) + socket.getservbyport(int(x)))
	os.system("rm -rf choice*")	
		
elif choice==3:
	print("[*] DRAG THE FILE HERE ! :\n")
	ip_file = input("[*] ==>>> ")
	ip_file = ip_file.split("'")
	f = open("{}".format(ip_file[1]),"r")
	f = f.read()
	f = f.split("\n")
	f.pop()
	
	for x in f:
		print("\nPerforming Port Scan on HOST Address :>>\n----------------------------")
		print(x)
		print("----------------------------\n")
		print("\n[*] OPEN PORTS : \n")
		os.system("nc -nv -z {} {} 2> choice3.txt".format(x,"1-1023"))
		os.system("cat choice3.txt | cut -d']' -f2| cut -d'(' -f1 > ports.txt")
		f = open("ports.txt","r")
		f = f.read()
		f = f.split("\n")
		f.pop()
		print("\n")
		for x in f:
			print("[{}] has Service : ".format(x) + socket.getservbyport(int(x)))
	
		os.system("rm -rf choice*")
		
		
		
		
		
		
		
