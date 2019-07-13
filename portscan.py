import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = input("Masukan IP Server : ")

def portscan(port):
	try:
		s.connect((server, port))
		return True
	except:
		return False

x = int(input("Mulai range : "))

y = int(input("Akhir range : "))

for x in range(x, y):
	if portscan(x):
		print("Port ", x, "Is Open")
	else:
pass
