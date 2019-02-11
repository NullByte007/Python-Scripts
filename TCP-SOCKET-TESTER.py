#!/usr/bin/python3
# Date Created : 3 February 2019
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
