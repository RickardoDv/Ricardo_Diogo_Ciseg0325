#	Leitura de até 50 valores de entrada (com validação para garantir que estejam entre 1 e 1000).
#	Para cada valor inserido, o programa deve identificar se é um número primo, 
# quantos divisores ele possui e se é um número perfeito e se é par ou ímpar.
#	Para a exibição e armazenamento dos valores, o programa deve parar de 10 em 10 valores, 
# e o usuário deverá ter a opção de sair e voltar ao menu principal.
#	O programa deve exibir os resultados e, após processar 10 valores, 
# perguntar ao usuário se deseja continuar ou parar.

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