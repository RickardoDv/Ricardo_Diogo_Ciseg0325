# Operadores Logicos 
# compara dois numeros ou strings e devolve sempre  True Ou False (Bool)
# > maior , < menor ,<= menor ou igual, >= maior ou igual, == igual , != difente
#if
#if 
#elif
#else
#match case 

# entre o num1 and  num2 e  num3 quem o maior e o menor

# num1 > num2 and  num2 > num3  num1 é o maior , meio num2 e menor num3
# num1 > num3 and  num3 > num2  num1 é o maior , meio num3 e menor num2
# num2 > num1 and  num1 > num3  num2 é o maior , meio num1 e menor num3
# num2 < num3 and  num3 < num1  num2 é o maior , meio num3 e menor num1
# num3 < num2 and  num2 < num1  num3 é o maior , meio num2 e menor num1
# num3 < num1 and  num1 < num2  num3 é o maior , meio num1 e menor num2

num1=0
num2=0
num3=0

num1=int(input("Intrud um numero 1 : "))
num2=int(input("Intrud um numero 2 : "))
num3=int(input("Intrud um numero 3 : "))

if num1>num2 and num2>num3:
        print("num 1 é o maior, num 2 é do meio,num 3 é o menor")
elif num1>num3 and num3>num2:
        print("num 1 é o maior, num 3 é do meio,num 2 é o menor")
elif num2>num1 and num1>num3:
        print("num 2 é o maior, num 1 é do meio,num 3 é o menor")
elif num2>num3 and num3>num1:
        print("num 2 é o maior, num 3 é do meio,num 1 é o menor")
elif num3>num1 and num1>num2:
        print("num 3 é o maior, num 1 é do meio,num 2 é o menor")
elif num3>num2 and num2>num1:
        print("num 3 é o maior, num 2 é do meio,num 1 é o menor")