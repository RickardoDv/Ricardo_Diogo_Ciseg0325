num1=int(input("Qual o valor do numero 1: "))
num2=int(input("Qual o valor do numero 2: "))
num3=int(input("Qual o valor do numero 3: "))


if num1>num2 and num1>num3:
        print("O numero 1 é o maior")      
elif num2>num1 and num2>num3:
        print("O numero 2 é o maior")
elif num3>num2 and num3>num1:
        print("O numero 3 é o maior")


if num1<num2 and num1<num3:
        print("O numero 1 é o menor")      
elif num2<num1 and num2<num3:
        print("O numero 2 é o menor")
elif num3<num2 and num3<num1:
        print("O numero 3 é o menor")


if num1>num2 and num1<num3 or num1<num2 and num1>num2:
        print("O numero 1 é o do meio")      
elif num2>num1 and num2<num3 or num2<num1 and num2>num3:
        print("O numero 2 é o do meio")
elif num3>num2 and num3<num1 or num3<num2 and num3>num1:
        print("O numero 3 é o do meio")
