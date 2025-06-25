import os

try:
    print("Tetas")
    f=open(badjoraas.txt)   
except:
    print("File does not exist")
    
print("funciona bem")


try:
    #print(Tetas)
    f=open(badjoras.txt)
    
except FileNotFoundError:
    print ("Ficheiro nao existe!!")
    os.system("touch badjorras.txt")
except Exception as e:
    print(e)
finally:
    print("funciona bem")
    
##-------------------

n=0

if n == 0:
    raise Exception("isto nao pode ser zero")
if type(n) is not int:
    raise Exception("Precisa de ser numero")