def validar_nome(nome):
    if not nome:
        return False
    if not nome[0].isupper():
        return False
    for char in nome[1:]:
        if not (char.islower() or char in "áéíóúãõâêôçüÁÉÍÓÚÃÕÂÊÔÇÜ"):
            return False
    return True

def adicionar_pessoa(lista_pessoas):
    while True:
        primeiro_nome = input("Digite o primeiro nome (ou 'sair' para parar): ")
        if primeiro_nome.lower() == 'sair':
            break
        if not validar_nome(primeiro_nome):
            print("Primeiro nome inválido. A primeira letra deverá ser maiúscula e o resto é minúsculo.")
            continue

        ultimo_nome = input("Digite o último nome: ")
        if not validar_nome(ultimo_nome):
            print("Último nome inválido. A primeira letra deverá ser maiúscula e o resto é minúsculo.")
            continue

        while True:
            try:
                idade = int(input(f"Digite a idade de {primeiro_nome} {ultimo_nome}: "))
                if idade >= 0:
                    break
                else:
                    print("A idade deve ser um número não negativo.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

        lista_pessoas.append({'primeiro_nome': primeiro_nome, 'ultimo_nome': ultimo_nome, 'idade': idade})
        print(f"{primeiro_nome} {ultimo_nome} adicionado(a) com sucesso.")
    return lista_pessoas

def ordenar_lista(lista_pessoas, por='primeiro_nome'):
    if por == 'primeiro_nome':
        return sorted(lista_pessoas, key=lambda pessoa: pessoa['primeiro_nome'])
    elif por == 'ultimo_nome':
        return sorted(lista_pessoas, key=lambda pessoa: pessoa['ultimo_nome'])
    else:
        return lista_pessoas

def listar_pessoas(lista_pessoas, ordenacao='primeiro_nome'):
    if not lista_pessoas:
        print("A lista de pessoas está vazia.")
        return

    lista_ordenada = ordenar_lista(lista_pessoas, ordenacao)
    print(f"\nLista de pessoas (ordenada por {ordenacao}):")
    for pessoa in lista_ordenada:
        print(f"{pessoa['primeiro_nome']} {pessoa['ultimo_nome']}")

def remover_pessoa(lista_pessoas, remover_por='primeiro_nome'):
    nome_remover = input(f"Digite o {remover_por} da pessoa que deseja remover: ")
    encontrado = False
    for i, pessoa in enumerate(lista_pessoas):
        if pessoa[remover_por] == nome_remover:
            del lista_pessoas[i]
            print(f"{pessoa['primeiro_nome']} {pessoa['ultimo_nome']} removido(a) com sucesso.")
            encontrado = True
            break
    if not encontrado:
        print(f"Não foi encontrado nenhum nome com o {remover_por} '{nome_remover}' na lista.")
    return lista_pessoas

def main():
    lista_de_pessoas = []

    while True:
        print("\nOpções:")
        print("1 - Adicionar pessoa")
        print("2 - Listar por primeiro nome")
        print("3 - Listar por último nome")
        print("4 - Remover por primeiro nome")
        print("5 - Remover por último nome")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            lista_de_pessoas = adicionar_pessoa(lista_de_pessoas)
        elif opcao == '2':
            listar_pessoas(lista_de_pessoas, 'primeiro_nome')
        elif opcao == '3':
            listar_pessoas(lista_de_pessoas, 'ultimo_nome')
        elif opcao == '4':
            lista_de_pessoas = remover_pessoa(lista_de_pessoas, 'primeiro_nome')
        elif opcao == '5':
            lista_de_pessoas = remover_pessoa(lista_de_pessoas, 'ultimo_nome')
        elif opcao == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()