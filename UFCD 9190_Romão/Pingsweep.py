#ping sweep
import os

lista_IP=list()

rede="192.168.255."

for octeto in range(1, 255):
    ip = rede+ str(octeto)
    #print(ip)
    lista_IP.append(ip)

for ip in lista_IP:
    #print(letra)
    cmd_ping="ping -c 1 " + ip
    resposta = os.popen(cmd_ping).read()
    #print(resposta)

    if "ttl" in resposta:
        print("[{}] Ligado".format(ip))
    else:
        print("[{}] DesLigado".format(ip))