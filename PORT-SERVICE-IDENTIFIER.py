#!/usr/bin/python3
# Date created : 5 January 2019
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
import socket
import os
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
print(Fore.RED + Style.BRIGHT + "")
print("                                             [ ~ #Code By: Aniket.N.Bhagwate]")
print(Fore.GREEN + Style.BRIGHT + "")
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
