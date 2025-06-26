print("Insira 50 numeros a sua escolha, entre 1 e 1000 ")
while count<51:
    num1=int(input(f"Insira o {count+1}º numero entre 1 e 1000 "))
    if num1>0 and num1<1001:
    # -----verificação de numero par ou impar----
        if num1%2==0:
                print("numero par")
        else:
                print("numero impar")
        lista.append(num1)
        count+=1
    # ------verificação de numero perfeito-----
        soma=0
        for i in range(1, num1):
            if num1 % i==0:
                soma+=i
        if soma==num1:
                print("Numero perfeito")
        else:
                print("Numero imperfeito")
    # -----Verificação de numero primo-----
        verif = True
        for it in range(2, int(num1**0.5)+1):
            if num1 % it == 0:
                verif=False
                print("O numero não é primo")
        if verif:
                print("O numero é primo")
    # ------Verificação de divisores------
        divisores = []
        for itt in range(1, num1 + 1):
            if num1 % itt == 0:
                divisores.append(itt)
        print(f"Os seus divisores são: {divisores}")
    # ------Match\Case------
opt=int(input("Insira um numero entre 1 e 12:"))
match opt:
    case int(1):
        print("JANEIRO")
    case int(2):
        print("FEVEREIRO")
    #-----Menu------
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
        case(_):
            print("Opção invalida")
def menu():
    print("===== MENU PRINCIPAL =====")
    print("1 - Inserir números")
    print("4 - Sair do programa")
def main():
    while True:
        menu()
        opcao=input("\nEscolha uma opção: ")
        if opcao=='1':
            print("---Inserção de números---")
            inserir()
        elif opcao=='4':
            print("A sair do programa")
            break
        else:
            print("Opção inválida. Tente novamente.")
main()
def listar():
    while count<=50:
        print("lista")
        count+=1
        if count%10==0:
            resp=input("Deseja continuar? (s/n): ")
            if resp!="s" or "S":
                print("Programa encerrado pelo utilizador.")
            break