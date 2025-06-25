#funcoes
#import modulosfuncoes as t
from modulosfuncoes import *

def imprime_tretas():
    print("\n\nCenas e tretas update")
    pass

def imprimir_argumentos(texto):
    print(f"inseriste o valor:{texto}")
    pass

def funcao_argumento(arg1,arg2):
    print(f"Valor do argumento 1: {arg1} e valor do argumento 2: {arg2}")
    pass

v=10
print("Mostrar valor de v:" + str(v))

def altera_valor(valor):
    #tronar v global
    #global v
    #v = 8  #variavel local para funcao
    valor=valor*2
    print("Mostrar valor de v dentro da função:" + str(v))
    return valor
    pass


#valor_modificado, valor_original = t.funcao1(10)
valor_modificado, valor_original = funcao1(20)


print(valor_modificado)
print(valor_original)





"""
altera_valor(v)
print("Mostrar valor de v:" + str(v))

print("inicio do codigo")
imprime_tretas()
imprimir_argumentos("mercedes")
funcao_argumento("Joao","Ricardo")
funcao_argumento(arg2="joaquim", arg1="Rui")
print("fim do codigo" )
"""