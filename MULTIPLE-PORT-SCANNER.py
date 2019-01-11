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
print("                                                        [ ~Aniket.N.Bhagwate]")
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
	
