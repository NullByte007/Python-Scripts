#!/usr/bin/python3
import os
print("[*] Downloading Required Library...")
os.system("pip install colorama==0.3.3")
from colorama import Fore, Back, Style
os.system("clear")
print(Fore.GREEN + Style.BRIGHT + "") 
a="""
--------------------
|TCP-SOCKET-TESTER |
------------------------------
|#code by : Aniket.N.Bhagwate|
------------------------------
"""

print(a)

print("---------------------------------------------")
print("PLEASE ENTER THE PORTS TO START LISTENING ON")
print("---------------------------------------------")

ch = input("==>> ")
ch = ch.split(" ")
print(ch)

for x in ch:
	os.system("nc -l -v -p {} &".format(x))
