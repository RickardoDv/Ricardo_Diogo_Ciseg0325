valores=[]
countnum=0
def numeros():
    countnum=0
    while countnum<=100:
        num1=int(input("Insira um valor"))
        if 0<num1>1001:
        # verificacao numero par
            if num1%2==0:
                print("Número Par")
            else:
                print("Número Impar")
        # verificacao numero primo
        # verificacao de divisores
        # verificacao se numero perfeito 
        soma=0
        for i in range (1, num1):
            if num1%i==0:
                soma+=i
            if soma==num1:
                print("Número perfeito")
            else:
                print("Número imperfeito")


        valores.append(num1)
        countnum+=1
    else:
        print("Valor inválido, tente de novo")


def listar():
    print("Os valores inseridos são:", valores)
def main():
    while True:
        print("1 - Inserir números")
        print("2 - Ver números")
        print("3 - Sair do programa")
        match input("Escolha uma opção "):
            case('1'):
                numeros()
            case('2'):
                listar()
            case('3'):
                print("A sair do programa")
                break
            case(_):
                print("Opção inválida, tente novamente")

main()