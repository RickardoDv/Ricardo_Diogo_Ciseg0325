## Exec 1
prentede-se criar uma calculadora que faça
a soma de duas variaveis 
A e B que vao ser colocadas pelo utilizador

Res:
var1=int(input("Introduza o primeiro numero "))
var2=int(input("Introduza o segundo numero "))
print("A soma dos dois numeros é", var1+var2)

## Exec 2
uma empresa pretende fazer uma validação de login
o utilizador devera de introduzir um username e uma password
e a aplicação deverá ser capaz de validar se

username = teste123
password = Buefixe

Res:
user=input("Introduza o username")
while user!=("teste123"):
    user=input("Username errado, tente outra vez!!")
passw=input("Introduza a Password")
while passw!=("Buefixe"):
    passw=input("Password errada, tente outra vez!!")
print("LOGIN ACEITE")

## Exec 3
Deverá desenvolver uma calculadora onde
o utilizador irá inserir dois valores
e depois deverá de aparecer a opção se o mesmo quer 
somar ou subtrair 

Res:
num1=int(input("Introduza o primeiro valor "))
num2=int(input("Introduza o segundo valor "))
opt=input("Escolha soma(+) ou subtração(-)")
match opt:
    case ("+"):
        print("O resultado da soma é: ", num1+num2)
    case ("-"):
        print("O resultado da subtração é: ", num1-num2)

## Exec 3.1 
Deverá de criar uma função soma_subtracao
que irá fazer as duas contas



## Exec 4
O programa deverá ler 3 numeros

depois de ler deverá de dar as seguintes opções ao utilizador:

- mostrar o maior
- mostrar o menor
- listar todos
- somar todos
- subtrair todos

deverá de reaproveitar o maximo de condigo 

num1=int(input("introduza o primeiro valor"))
num2=int(input("introduza o segundo valor"))
num3=int(input("introduza o terceiro valor"))
if num1>num2 and num1>num3:
    print(f"O {num1} é o numero maior")
elif num2>num1 and num2>num3:
    print(f"O {num2} é o numero maior")
else:
    print(f"O {num3} é o numero maior")
if num1<num2 and num1<num3:
    print(f"O {num1} é o numero menor")
elif num2<num1 and num2<num3:
    print(f"O {num2} é o numero menor")
else:
    print(f"O {num3} é o numero menor")
print("Os numeros escolhidos foram: ",num1,num2,num3)
print("A soma dos numeros é: ", num1+num2+num3)
print("a subtração dos numeros é: ", num1-num2-num3)

## Exec 4.1

devera de criar uma variavel enviar_log
e cada função que for executada irá enviar uma log com o seguinte formato

DATA - (O QUE FOI FEITO)

devera de guardar no ficheiro sistema.txt

## Exec 5 


Uma empresa pretende criar uma aplicação onde no início
deverá de pedir um login ao utilizador:

Existem dois tipos de utilizador:

Utilizador normal -> Irá ser o João
Administrador -> Irá ser o Administrador

Os utilizadores deveram de ter as seguintes funções:

- Calculadora (Somar, Dividir, Multiplicar, Subtrair)
- Cálculos (Calcular a área do Quadrado, Círculo, Retângulo)

Para todas as ações deverá de ser criada uma log com o seguinte formado
DATA - (Todos os detalhes, como o que foi feito (valores introduzidos e resultado)

Os Administradores deveram de ter as seguintes funções:

- Consultar as logs

Bom trabalho :)
Deverá de reaproveitar o máximo de condigo de modo a otimizar.
