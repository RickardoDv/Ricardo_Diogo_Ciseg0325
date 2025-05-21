#Elabore um programa que leia uma entrada e diga quantos números perfeitos existem.
#Exemplo de numero perfeito em que somando todos os divisores ele da o numero inicial.
#6=3+2+1 .


limite = int(input("Digite um número inteiro: "))
quantidade = 0

print("Números perfeitos encontrados:")

for n in range(1, limite + 1):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    if soma == n:
        print(n)
        quantidade += 1

print(f"Quantidade de números perfeitos entre 1 e {limite}: {quantidade}")
