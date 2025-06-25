#trabalhar com funcões e crypto
from cryptography.fernet import Fernet

def generate_key():
    key=Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    pass

def load_key():
    with open("secret.key", "rb") as f:
        return f.read()
    pass

def encrypt_password(plain_text_password,key):
    f=Fernet(key)
    encrypted_pass=f.encrypt(plain_text_password.encode())
    print("Encrypted password: {}".format(encrypted_pass))
    pass

def decrypt_password(encrypted_password, key):
    f=Fernet(key)
    decrypted_password=f.decrypt(encrypted_password).decode()
    print("Decrypted Password: {}".format(str(decrypted_password)))
    pass

if __name__=="__main__":
    #generate_key()
    key=load_key()
    password=input("inserir uma password: ")
    encrypt_password(password,key)
    texto_cifrado=input("inserir texto cifrado: ")
    decrypt_password(texto_cifrado, key)
    pass