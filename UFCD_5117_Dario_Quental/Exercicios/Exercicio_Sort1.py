pessoa=[]

def menu():
    print("\n----- Menu -----")
    print("1. Adicionar Utilizador")
    print("2. Pesquisar Utilizador por primeiro nome")
    print("3. Pesquisar Utilizador por ultimo nome")
    print("4. Eliminar Utilizador")
    print("5. Sair")

def opt1():
    while True:
        primeiro=input("Adicione o primeiro nome do utilizador, ou 'PARAR' para encerrar")
        if primeiro == "PARAR":
            break
        else:
            letra=ord(primeiro[0])
            if 65>= letra and letra <=90:
                pessoa.append(primeiro)
            else:
                print("O nome tem que estar escrito com a primeira letra maiúscula e as restantes minúsculas")   
            return
  
        ultimo=input("Insira o ultimo nome do utilizador, ou 'PARAR' para encerrar")
        if ultimo == "PARAR":
            return False
        elif primeira==ultimo[0]:
            pessoa.append(ultimo)
        idade=input("Insira a idade do utilizador, ou 'PARAR' para encerrar")
        if idade == "PARAR":
            return False
        elif idade < 0:
            print("Idade inválida")
        else:
            pessoa.append(idade)




    print("O nome tem que estar escrito com a primeira letra maiúscula e as restantes minúsculas")
    input("Insira o ultimo nome do utilizador")
    
    input("Qual a idade do utilizador")
    print("Idade inválida")

def opt2():
    input("Indique o primeiro nome do utilizador:")

def opt3():
    input("Indique o ultimo nome do utilizador?")

def opt4():
    input("Qual o utilizador que pretende eliminar?")




while True:
    menu()
    escolha = input("\nDigite o número da sua opção: ")

    if escolha=='1':
        opt1()
    elif escolha=='2':
        opt2()
    elif escolha=='3':
        opt3()
    elif escolha=='4':
        opt3()
    elif escolha=='5':
        print("Desligando o programa!")
        break
    else:
        print("Opção inválida. Tente novamente.")