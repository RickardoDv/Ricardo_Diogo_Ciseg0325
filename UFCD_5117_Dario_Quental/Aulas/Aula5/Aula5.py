import os
os.system('cls' if os.name == 'nt' else 'clear')


numeros=[4,3,5,6,7,8]
#Index   0 1 2 3 4 5
#length 6

# For se houver numero definido de loop inicial
# For each é usado para listas
# while é usado para loops indefenidos

i=0
print(numeros)
while i <5:
    if (numeros[i]>numeros[i+1]):
        numeros[i] , numeros [i+1]= numeros[i+1], numeros [i]
    i+=1
    
print(numeros)