opt=int(input("Insira um numero entre 1 e 12:"))
match opt:
    case int(1):
        print("JANEIRO")
    case int(2):
        print("FEVEREIRO")
for i in range(11):
    if i%2==0:
        print("numero par",i)
    else:
        print("numero impar",i)
        
notas=[]
i=1
for i in range(10):
    notas.append(float(input("Introduza a nota do aluno: ")))
soma_notas=sum(notas)
contagem=len(notas)
print(contagem)
print(soma_notas)
for i in range(1, 10):
  print(str(i) * i)
  
import time
i=0
while i<=258:
    print(f"Numero por Caracteres {chr(i)}" )
    print(f"Caracteres por numero {ord(chr(i))}")
    time.sleep(1)
    i+=1
    
soma = 0
num1=int(input("insira um numero: "))
for i in range(1, num1):
    if num1 % i == 0:
        soma += i
if soma == num1:
    print("Numero perfeito")
else:
    print("Numero imperfeito")
    
if num1%2==0:
    print("numero par")
else:
    print("numero impar")
    
def listar():
    while count<=50:
        print("lista")
        count+=1
        if count%10==0:
            resp=input("Deseja continuar? (s/n): ")
            if resp!="s" or "S":
                print("Programa encerrado pelo utilizador.")
            break
        
lista=[]
count=0
soma=0

def inserir():
    count=0
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
                if num1 % i==0:
                    soma+=i
            if soma==num1:
                print("Numero perfeito")
            else:
                print("Numero imperfeito")
    # Verificação de numero primo
    # Verificação de divisores
    # Pergunta se quer continuar ou sair
        if count%10==0:
            resp=input("Deseja continuar? (s/n): ")
            if resp!="s" or "S":
                print("Programa encerrado pelo utilizador.")
            break      
    else:
        print("O valor escolhido tem que estar entre 1 e 1000")  

def listar():
    while count<=50:
        print("lista")
        count+=1
        if count%10==0:
            resp=input("Deseja continuar? (s/n): ")
            if resp!="s" or "S":
                print("Programa encerrado pelo utilizador.")
            break

def calculadora():
    num1=int(input("Insira o primeiro numero: "))
    if num1<=0 and num1>=1000:
        print("Numero inválido, deve ser entre 1 e 1000")
    num2=int(input("Insira o segundo numero: "))
    if num2<=0 and num2>=1000:
        print("Numero inválido, deve ser entre 1 e 1000")

    opt=input("\nQual a operação a realizar?")   
    match opt:
        case("+"):
            print("O resultado é:", num1+num2)
        case("-"):
            print("O resultado é:", num1-num2)
        case("*"):
            print("O resultado é:", num1*num2)
        case("/"):
            print("O resultado é:", num1/num2)
        case(_):
            print("Opção invalida")

def menu():
    print("===== MENU PRINCIPAL =====")
    print("1 - Inserir números")
    print("2 - Ver números")
    print("3 - Calculadora")
    print("4 - Sair do programa")

def main():
    while True:
        menu()
        opcao=input("\nEscolha uma opção: ")
        if opcao=='1':
            print("---Inserção de números---")
            inserir()
        if opcao=='2':
            print("---Listagem de números---")
            listar()
        elif opcao=='3':
            print("---Calculadora---")
            calculadora()
        elif opcao=='4':
            print("A sair do programa")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()

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
num=2
contador=0
while contador < 10:
    verif = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            verif=False
            break
    if verif:
            print(num)
            contador+=1
    num+=1