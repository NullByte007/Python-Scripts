#!/usr/bin/python3

#Copyright 2019, Aniket.N.Bhagwate, All rights reserved.
#
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
from colorama import Fore, Back, Style

print(Fore.GREEN + Style.BRIGHT + "")

banner ="""
	|-----------------------------------------------------------|
	| ____ ___ _   _  ____   ____ __        _______ _____ ____  |
	||  _ \_ _| \ | |/ ___| / ___ \ \      / / ____| ____|  _ \ |
	|| |_) | ||  \| | |  _  \___ \ \ \ /\ / /|   | |  _| | |_) ||
	||  __/| || |\  | |_| |  ___) | \ V  V / | |___| |___|  __/ |
	||_|  |___|_| \_|\____| |____/   \_/\_/  |_____|_____|_|    |
	|-----------------------------------------------------------|
	|                                    CODE BY ~NULLBYTE007   |
	|-----------------------------------------------------------|

"""
print(banner)
os.system("rm -rf IP_ADDRESS.txt")
ipadd =''
ip_list = []
ip = input("[*] PLEASE ENTER IP ADDRESS : " + Fore.CYAN + Style.BRIGHT)
ip = ip.split(".")
ip.pop()

for x in ip:
	ipadd = ipadd + x + "."

print(Fore.CYAN + Style.BRIGHT+ "[*] STARTED PING SWEEPER\n[*] GATHERING ALIVE HOSTS !!" + Fore.GREEN + Style.BRIGHT)
input("[*] PRESS ENTER TO CONTINUE !!")
for x in range(200,210):
	if os.system("ping -c 2 {}{}".format(ipadd,x)) == 0:
		ip_list.append("{}{}".format(ipadd,x))

os.system("clear")
print(banner)
print("\n[*] FOUND ALIVE HOSTS :"+Fore.CYAN + Style.BRIGHT+ " : {}".format(len(ip_list)))
print(Fore.WHITE + Style.BRIGHT)
for x in ip_list:
	print("[-->] {}".format(x))


choice = input(Fore.GREEN + Style.BRIGHT + "\n[!] DO YOU WISH TO SAVE THE OBTAINED IP ADDRESS TO A FILE ? [Y/N] : ")
if choice =='Y' or choice=='y':
	os.system("touch IP_ADDRESS.txt")
	f = open("IP_ADDRESS.txt","a")
	for x in ip_list:
		f.write(x)
	f.close()
	print("[*] SAVED DATA IN -->" +Fore.CYAN + Style.BRIGHT + "IP_ADDRESS.txt")
else:
	print(Fore.RED + Style.BRIGHT +"[!] QUITTING !!")
	exit(0)

	

