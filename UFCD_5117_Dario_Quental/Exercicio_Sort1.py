def menu():
    print("\n----- Menu -----")
    print("1. Adicionar Utilizador")
    print("2. Pesquisar Utilizador por primeiro nome")
    print("3. Pesquisar Utilizador por ultimo nome")
    print("4. Eliminar Utilizador")
    print("5. Sair")

def opt1():
    primeiro=input("Adicione o primeiro nome do utilizador, ou 'PARAR' para encerrar")
        if primeiro
    print("O nome tem que estar escrito com a primeira letra maiúscula e as restantes minúsculas")
    input("Insira o ultimo nome do utilizador")
    print("O nome tem que estar escrito com a primeira letra maiúscula e as restantes minúsculas")
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
        print("Saindo do programa!")
        break
    else:
        print("Opção inválida. Tente novamente.")