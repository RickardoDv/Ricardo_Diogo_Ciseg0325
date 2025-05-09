livros=[]

def adicionar():
    if len(livros)<=100:
        livro=input("Insira o nome do livro ")
        livros.append(livro)
    else:
        print("A tabela livros está cheia")

def procurar():
    procurar=input("Qual o livro a procurar? ")
    if procurar in livros:
        print("Livro encontrado na base de dados.",)
    else:
        print("Livro não encontrado na base de dados")

def excluir():
    exclude=input("Qual o livro a excluir? ")
    if exclude in livros:
        livros.remove(exclude)
        print(f"Livro {exclude} eliminado")
    else:
        print("Livro não encontrado.")


def ordenar():
    print("Listando os livros ordenados: ", livros.sort)

def listar ():
    print("Os livros registados são: ", livros)

def main():
    while True:
        print("1 - Adicionar novo livro")
        print("2 - Procurar por titulo ou autor")
        print("3 - Excluir livro")
        print("4 - Ordenar livros")
        print("5 - Listar livros")
        print("6 - Sair do programa")
        match input("Escolha uma opção "):
            case('1'):
                adicionar()
            case('2'):
                procurar()
            case('3'):
                excluir()
            case('4'):
                ordenar()
            case('5'):
                listar()
            case('6'):
                print("A sair do programa")
                break
            case(_):
                print("Opção inválida, tente novamente")

main()