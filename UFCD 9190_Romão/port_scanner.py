#sockets - redes
import socket
s=socket.socket()

s.settimeout(1)
ip= "195.23.212.226"

porta_inicial=int(input("indique a porta inicial de rede: "))
porta_final=int(input("indique a porta final de rede: "))

for port in range(porta_inicial,porta_final+1):
    resultado=s.connect_ex((ip,port))
    if resultado==0:
        print("Porta", port, "aberta")
    else:
        print("Porta", port, "fechada")
    
    s.close()
    s=socket.socket()
    s.settimeout(1)    
    pass

