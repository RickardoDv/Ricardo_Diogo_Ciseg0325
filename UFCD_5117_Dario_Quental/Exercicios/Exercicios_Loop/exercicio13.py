#Elabore um programa que
#leia um número e mostre a tabuada. 
#(multiplicar de 1 a 10)

num1=int(input("Introduza um valor:"))

num2=1
while num2<=10:
    result=num1*num2
    print(num1,"X",num2,"=", result)
    num2+=1