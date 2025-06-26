#operadores matematico
# +,-,/,*,// <-- divisão por inteiro, ** >-- expoente, 
# % <-- modulo devolve o resto de uma divisão

num1=0
num2=0
total=0

num1=int(input("introduza o numero 1: "))
num2=int(input("Introduza o numero 2: "))

total= num1/num2
print("O total da divisão: ", total)

total= num1*num2
print("O total da multiplicação: ", total)

total= num1-num2
print("O total da Subtração: ", total)

total= num1+num2
print("O total da Soma: ", total)

total= num1//num2
print("O total da divisão por inteiro: ", total)

total= num1**num2
print("O total do exponete: ", total)

total= num1%num2
print("O total da modulo: ", total)