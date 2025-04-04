#operadores logicos
#compara 2 numeros ou strings e devolve sempre True ou False (Bool)
# > maior, < menor , >= maior ou igual , <= menor ou igual , == igual , != diferente


print (2>3)
print (type(2>3))

#   Condições
#------if------
#if
#elif
#else
#------- match case ------
#MATCH CASE

#entre o num1 e o num2 quem é o maior ou menor
"""
num1=int(input("Qual o valor do numero 1: "))
num2=int(input("Qual o valor do numero 2: "))

if num1>num2:
    print("O numero maior é", num1,", e o menor", num2)
else:
    print("O numero maior é", num2,", e o menor", num1)
    
"""

#entre o num1, o num2 e o num3 quem é o maior ou menor
#num1> num2 && nm1 >num3, num1 é maior
#num2>num1 && num2> num3, num2 é maior
#num3>num1 && num3>num2, num3 é o maior
#num1<num2 && nm1<num3, num1 é menor
#num2<num1 && num2<num3, num2 é menor
#num3<num1 && num3<num2, num3 é o menor
num1=int(input("Qual o valor do numero 1: "))
num2=int(input("Qual o valor do numero 2: "))
num3=int(input("Qual o valor do numero 3: "))


if num1>num2:
    if num1>num3:
        print("num1 é o maior")
        
elif num2>num1:
    if num2>num3:
        print("num2 é o maior")
        
elif num3>num2:
    if num3>num1:
        print("num3 é o maior")