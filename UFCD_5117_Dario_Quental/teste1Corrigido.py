marcas = []
modelos = []

def addmarca():
    while len(marcas) < 100:
        marca = input("Introduza a marca da viatura (ou 'sair' para terminar): ")
        if marca.lower() == 'sair':
            break
        marcas.append(marca)
    if len(marcas) >= 100:
        print("Tabela Marcas está cheia.")

def addmodelo():
    while len(modelos) < 100:
        modelo = input("Introduza o modelo da viatura (ou 'sair' para terminar): ")
        if modelo.lower() == 'sair':
            break
        modelos.append(modelo)
    if len(modelos) >= 100:
        print("Tabela Modelos está cheia.")

def procmarca():
    termo = input("Introduza a Marca a procurar: ")
    achou = False
    for i, marca in enumerate(marcas):
        if termo.lower() in marca.lower():
            print(f"Posição {i}: {marca}")
            achou = True
    if not achou:
        print("Nenhuma Marca encontrada.")

def procmodelo():
    termo = input("Introduza o Modelo a procurar: ")
    achou = False
    for i, modelo in enumerate(modelos):
        if termo.lower() in modelo.lower():
            print(f"Posição {i}: {modelo}")
            achou = True
    if not achou:
        print("Nenhum Modelo encontrado.")

def exmarca():
    termo = input("Introduza a Marca a excluir: ")
    achou = False
    for i, marca in enumerate(marcas):
        if termo.lower() == marca.lower():
            marcas.pop(i)
            print(f"{termo} removido da lista.")
            achou = True
            break
    if not achou:
        print("Nenhuma Marca encontrada.")

def exmodelo():
    termo = input("Introduza o Modelo a excluir: ")
    achou = False
    for i, modelo in enumerate(modelos):
        if termo.lower() == modelo.lower():
            modelos.pop(i)
            print(f"{termo} removido da lista.")
            achou = True
            break
    if not achou:
        print("Nenhum Modelo encontrado.")

def menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Adicionar Marca")
    print("2 - Adicionar Modelo")
    print("3 - Procurar Marca")
    print("4 - Procurar Modelo")
    print("5 - Excluir Marca")
    print("6 - Excluir Modelo")
    print("7 - Sair")

def main():
    while True:
        menu()
        opt = input("\nEscolha uma opção: ")
        if opt == '1':
            addmarca()
        elif opt == '2':
            addmodelo()
        elif opt == '3':
            procmarca()
        elif opt == '4':
            procmodelo()
        elif opt == '5':
            exmarca()
        elif opt == '6':
            exmodelo()
        elif opt == '7':
            print("A sair do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
