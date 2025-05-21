# Funcão input
#tipos de dados primários
# int 0...9 ex: 0489
# float 1.0 .... 9.9  ex: 3.14
# bool ex: True ou False
# str "aqwsdefrgt 68513216 oiucobaovb"
# casting "cast"--> converte um tipo de dados em outro
"""
num_tel=0
nom_cli= ""

num_tel=input("Qual o Numero de telefone: ")
nom_cli=input("Qual o Nome do Cliente: ")

print("Nome do cliente: ", nom_cli,"\nNumero de telefone: ", num_tel)
"""

num1=int(input("Introduza o numero 1: "))
num2=int(input("Introduza o numero 2: "))

#total1= num1+num2 #quando é uma string: as duas váriaveis irão se juntar a formar só uma

print("Tipo de Numero1: ",type(num1),"\nTipo de Numero2: ",type(num2)) # está a perguntar qual o tipo da variavel

total=num1/num2
print("\n\n\n")
print("a divisão dos dois números é: ",total)