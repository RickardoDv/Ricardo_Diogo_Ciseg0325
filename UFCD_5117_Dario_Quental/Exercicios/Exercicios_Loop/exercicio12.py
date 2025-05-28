#Elabore um programa que leia quantos números quer que se efetue a soma, 
# subtrações, divisões, multiplicações e no fim por meio de um acumulador 
# diga quantas operações foram efetuadas. 
# Exemplo introduzindo o número 60 o programa deve apresentar 60 a somar, 
# dividir multiplicar e subtrair por todos os números menores que ele

num1=int(input("Introduza um valor:"))
count=num1
while count>0:
    print(num1*count)
    count-=1

count=num1
while count>0:
    print(num1/count)
    count-=1
    
count=num1
while count>0:
    print(num1+count)
    count-=1

count=num1
while count>0:
    print(num1-count)
    count-=1