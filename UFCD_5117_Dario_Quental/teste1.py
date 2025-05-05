marcas=[]
modelos=[]

def addmarca():
        while marcas.len()<=100:
            marca=input("Introduza a marca da viatura")
            marcas.append(marca)
        else:
            print("Tabela Marcas está cheia.")

def addmodelo():
        while modelos.len()<=100:
            modelo=input("Introduza o modelo da viatura")
            modelos.append(modelo)
        else:
            print("Tabela Modelos está cheia.")

def procmarca():
        termo = input("Introduza a Marca a procurar: ")
        achou = False
        for i in range(len(marcas)):
            if termo.lower() in marcas[i].lower():
                print(f"Posição {i}: {marcas[i]}")
                achou = True
        if not achou:
            print("Nenhuma a Marca encontrado.")

def procmodelo():
        termo = input("Introduza o Modelo a procurar: ")
        achou = False
        for i in range(len(marcas)):
            if termo.lower() in modelos[i].lower():
                print(f"Posição {i}: {modelos[i]}")
                achou = True
        if not achou:
            print("Nenhum Modelo encontrado.")

def exmarca():
    termo=input("Introduza a Marca a excluir")
    achou = False
    for i in range(len(marcas)):
        if termo.lower() in marcas[i].lower():
            marcas.pop(termo)
            print(f"{termo} Removido da lista")
            achou = True
    if not achou:
            print("Nenhuma Marca encontrada.")
            
def exmodelo():
    termo=input("Introduza o Modelo a excluir")
    achou = False
    for i in range(len(modelos)):
        if termo.lower() in modelos[i].lower():
            modelos.pop(termo)
            print(f"{termo} Removido da lista")
            achou = True
    if not achou:
            print("Nenhuma Modelo encontrada.")

def menu():
    print("===== MENU PRINCIPAL =====")
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
        opt=input("\nEscolha uma opção!!\n")
        if opt=='1':
            print("Adicionar Marca!")
            addmarca()
        elif opt=='2':
            print("Adicionar Modelo!!")
            addmodelo()
        elif opt=='3':
            print("Procurar Marca!!")
            procmarca()
        elif opt=='4':
            print("Procurar Modelo!!")
            procmodelo()
        elif opt=='5':
            print("Excluir Marca!!")
            exmarca()
        elif opt=='6':
            print("Excluir Modelo!!")
            exmodelo()
        elif opt=='7':
            print("A sair do programa...")
            break
        else:
            print("Opção Invalida!!! Tente novamente")
main()