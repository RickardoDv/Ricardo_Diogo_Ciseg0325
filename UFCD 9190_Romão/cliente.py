#Codigo de socket cliente
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip="81.193.162.124"
porta=5000

s.connect((ip,porta))

s.send(b"DOS REINOS DO ALGARVE")

msg=s.recv(1024)

print("Mensagem recebida do servidor!!!", msg.decode())

print("ola")