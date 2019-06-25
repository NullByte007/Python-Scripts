	------------------------------------------
	|----------------------------------------|
	|	NULLBYTE-SCRIPTS-COLLECTION      |
	|----------------------------------------|
	------------------------------------------

# Python-Scripts
Basic Introduction : 

	--> This is a collection of Python Scripts specifically used for Network Security !
	--> This Scripts are created to be used on -> LINUX <-  ONLY !!

Usage Information :
	
	[*] Run: pip3 install -r requirements.txt
	[*] Grant execution permissions to the scripts before using them.
	[*] TYPE : chmod +x <file_name> and 
	[*] Run using ./<script_name.py>
	[*] Also You can run them with simple python3 command (use python3 specifically!)
	[*] Run using python3 <script_name.py>
	
SCRIPTS PROVIDED : 
	
	[1] SUBDOMAIN-FINDER
		This script is used for finding the subdomains of any domain on the Internet !
		Also their IP Address are fetched directly through the Script itself and saved in a file for future usage !
	
	[2] MULTIPLE-PORT-SCANNER
		This script is used to scan all the ports for the provided range and fetch the service running on each of them
		
	[3] PORT-SERVICE-IDENTIFIER
		This script works same as the  MULTIPLE-PORT-SCANNER ,but the difference is that in this script you can specify
		each port seperately and identify service specifically for them !
		
	[4] NETCAT
		This script is a simple implementation of NetCat tool
		This script will save you dozens of commands and works with simple Menu Driven functionality !!
		
	[5] OPEN-PORT-FINDER
		This tool works on nmap utility and can be used to check for open ports in target machine !
	
	[6] TCP-SOCKET-TESTER
		This tool can be used to create multiple listening sockets for testing purpose.
		Basically this sockets can be directly connected using any tool or protocol.
		
	[7] NETWORK-MONITOR-SNIFFER
		This tool can be used to monitor network and is built/automated on top of "tcpdump".
		Also a network sniffer is added to sniff the data flowing back and forth through the network.
		[sniffer only works for UNENCRYPTED data !!]

	[8] PING-SWEEP
		This tool can be used to ping sweep an entire subnet and find all the alive[online] hosts on the given network!.
		Also found ip can be stored into a seperate file for future use !
