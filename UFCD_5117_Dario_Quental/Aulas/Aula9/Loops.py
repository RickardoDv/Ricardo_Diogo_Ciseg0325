i=1
it=1

while i<=10:
    print("Numero externo ", i)
    if i%2==0:
        print(i,"É par")
    else:
        print(i, "É impar")
    it=1
    while it<=i:
        print("Numero externo ", i,"numero interno", it)
        if i%it==0:
            print(it," foi divisor de ",i)
        it+=1
    i+=1