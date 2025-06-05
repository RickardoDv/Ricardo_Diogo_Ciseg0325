#trabalhar com funcões e crypto
from cryptography.fernet import Fernet

import sqlite3

nomeBD="BaseDeDados.db"
global conn
conn=sqlite3.connect(nomeBD)
global c
c = conn.cursor()



def generate_key():
    key=Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    pass

def load_key():
    with open("secret.key", "rb") as f:
        return f.read()
    pass

def encrypt_password(key):
    f=Fernet(key)
    username=input("insira o nome de utilizador: ")
    plain_text_password=input("Insira nova pass em plain text: ")
    encrypted_pass=f.encrypt(plain_text_password.encode())
    print("Encrypted password: {}".format(encrypted_pass))
    sql="INSERT INTO helldivers (username, password) VALUES (?,?);"
    dados=(username,encrypted_pass)
    c.execute(sql, dados)
    conn.commit()
    print("Password guardada em bases de dados")
    pass

def decrypt_password(key):
    sql="SELECT id, username FROM helldivers;"
    c.execute(sql)
    resultado=c.fetchall()

    for registo in resultado:
        print(registo)

    id_user=input("Selecionar Utilizador: ")
    sql="SELECT password FROM helldivers WHERE id = ?"
    dados=(id_user)
    c.execute(sql,dados )
    resultado=c.fetchall()

    for registo in resultado:
        #print(registo[0])
        encrypted_password=registo[0]

    f=Fernet(key)
    decrypted_password=f.decrypt(encrypted_password).decode()
    print("Decrypted Password: {}".format(str(decrypted_password)))
    pass


if __name__=="__main__":
    menu_text="""
1- Gerar chave de cripto
2- resgistar novo username e password
3- ler passwords
'EXIT' - Sair
"""
    opcao = 0
    while opcao!="exit":
        print(menu_text)
        opcao= input("INserir opcao: ")

        if opcao=="1":
            generate_key()
        elif opcao=="2":
            key=load_key()
            encrypt_password(key)
        elif opcao=="3":
            key=load_key()
            decrypt_password(key)
        else:
            print("Opçao invalida")




"""
    #generate_key()
    key=load_key()
    password=input("inserir uma password: ")
    encrypt_password(password,key)
    texto_cifrado=input("inserir texto cifrado: ")
    decrypt_password(texto_cifrado, key)
    pass
"""