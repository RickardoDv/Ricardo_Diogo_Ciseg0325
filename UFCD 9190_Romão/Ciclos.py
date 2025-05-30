#Ciclos
import os

lista_A=["8.8.8.8","8.8.4.4","10.2.2.2","127.0.0.1","192.23.212.226"]

for letra in lista_A:
    #print(letra)
    cmd_ping="ping -c 1 " + letra
    resposta = os.popen(cmd_ping).read()
    #print(resposta)

    if "ttl" in resposta:
        print("[{}] Ligado".format(letra))
    else:
        print("[{}] DesLigado".format(letra))