#Elabore um programa que constitua a média de 30 números pares que sejam introduzidos.
#Validando a entrada de números inteiros entre 1 e 50.
count=1
lista=[]
while count<=30:
    num1=int(input("Introduza um numero par entre 1 e 50: "))
    if num1%2==0:
        if num1 <=50 and num1 >= 1:
                lista.append(num1)
                count+=1
    else:
        print("O numero tem que ser par e estar entre 1 e 51:")
print(lista)