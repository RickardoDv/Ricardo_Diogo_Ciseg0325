#sockets - redes
import socket
s=socket.socket()
s.settimeout(1)
ip= "195.23.212.226"
porta=443

resultado=s.connect_ex((ip,porta))

print(resultado)