#Escreva um programa que mostre os primeiros 60 números da serie bonatchi.
#1, 1, 2, 3, 5, 8, 13, 21.
#Como se constrói.
#1+1=2
#    1+2=3
#        2+3=5
num1=1
num2=1
count=1
while count<=60:
    num3=num1+num2
    num1=num2
    num2=num3
    count+=1
    print(num3)