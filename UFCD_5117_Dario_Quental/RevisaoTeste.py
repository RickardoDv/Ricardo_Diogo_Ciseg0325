#	Leitura de até 50 valores de entrada (com validação para garantir que estejam entre 1 e 1000).

lista=[]
count=0
soma=0

"""
print("Insira 50 numeros a sua escolha, entre 1 e 1000 ")

while count<51:
    num1=int(input(f"Insira o {count+1}º numero entre 1 e 1000 "))
    if num1>0 and num1<1001:
        lista.append(num1)
        count+=1
    else:
        print("O valor escolhido tem que estar entre 1 e 1000")
print(list)     
"""
#	Para cada valor inserido, o programa deve identificar se é um número primo, quantos divisores ele possui e se é um número perfeito e se é par ou ímpar.

print("Insira 50 numeros a sua escolha, entre 1 e 1000 ")

while count<51:
    num1=int(input(f"Insira o {count+1}º numero entre 1 e 1000 "))
    if num1>0 and num1<1001:
        # verificação de numero par ou impar
        if num1%2==0:
            print("numero par")
        else:
            print("numero impar")
        lista.append(num1)
        count+=1
        # verificação de numero perfeito
        soma=0
        for i in range(1, num1):
            if num1 % i == 0:
                soma += i
        if soma == num1:
            print("Numero perfeito")
        else:
            print("Numero imperfeito")
        # Verificação de numero primo
        
    else:
        print("O valor escolhido tem que estar entre 1 e 1000")
print(list)   

#	O programa deve exibir os resultados e, após processar 10 valores, perguntar ao usuário se deseja continuar ou parar.


#	Para a exibição e armazenamento dos valores, o programa deve parar de 10 em 10 valores, e o usuário deverá ter a opção de sair e voltar ao menu principal.


#   Calculadora simples, que execute as operações de soma, subtração, multiplicação e divisão (com validação de entradas entre 1 e 1000).

num1=int(input("Insira o primeiro numero: "))
if num1>=0 and num1<=1000:
    print("Numero inválido, deve ser entre 1 e 1000")
    
num2=int(input("Insira o segundo numero: "))
if num2>=0 and num2<=1000:
    print("Numero inválido, deve ser entre 1 e 1000")

print("Soma:", num1+num2)
print("Subtração:", num1-num2)
print("Multiplicação:", num1*num2)
print("Divisão:", num1/num2)
    
    
    