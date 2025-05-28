
num=2
contador=0

while contador < 10:
    verif = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            verif=False
            break
    if verif:
            print(num)
            contador+=1
    num+=1