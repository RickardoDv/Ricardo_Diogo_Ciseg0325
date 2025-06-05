#sockets_servidor

import socket
ip="localhost"
porta=5000

print("Servidor a iniciar!!")
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#socket.SOCK_STREAM ---> TCP
#socket.SOCK_DGRAM ---> UDP

s.bind((ip, porta))
s.listen(20)

while True:
    c, addr=s.accept()
    print ("Mensagem recebida de: ",addr)
    msg=c.recv(1024)
    print("Mensagem recebida: ", msg)

    resposta="Tun Tun ATEC!!"
    c.send(resposta.encode())
    pass