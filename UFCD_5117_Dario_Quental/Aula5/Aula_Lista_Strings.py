import time
# controlo de listas em duas dimensões
cidades=["Lisboa","Madrid","São Paulo"]

print(cidades[0][0])
print(ord(cidades[0][0]))

#index 1ª dimensão
i=0
it=0
while i<=2:
    print(f"1ª dimensão i={i}")
    #numeros[i][?]
    print("Valor na 1ª dimensão",cidades[i])
    i+=1