import time
# controlo de listas em duas dimensões
cidades=["Lisboa","Madrid","São Paulo"]
#index 1ª dimensão
#           L I S B O A
#           0 1 2 3 4 5  #2ª dimensão
#
print(cidades[0][0])
print(ord(cidades[0][0]))


i=0
it=0
while i<=2:
    print("Valor na 1ª dimensão",cidades[i])
    #cidades[i][?]
    it=0
    while it< len(cidades[i]):
        print(f"1ª dimensão i={i}")
        print(f"1ª dimensão it={it}")
        print("Letra na segunda dimensão",cidades[i][it])
        time.sleep(1)
        it+=1
    i+=1