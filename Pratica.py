num1=int(input("introduza o primeiro valor"))
num2=int(input("introduza o segundo valor"))
num3=int(input("introduza o terceiro valor"))
if num1>num2 and num1>num3:
    print(f"O {num1} é o numero maior")
elif num2>num1 and num2>num3:
    print(f"O {num2} é o numero maior")
else:
    print(f"O {num3} é o numero maior")
if num1<num2 and num1<num3:
    print(f"O {num1} é o numero menor")
elif num2<num1 and num2<num3:
    print(f"O {num2} é o numero menor")
else:
    print(f"O {num3} é o numero menor")
print("Os numeros escolhidos foram: ",num1,num2,num3)
print("A soma dos numeros é: ", num1+num2+num3)
print("a subtração dos numeros é: ", num1-num2-num3)