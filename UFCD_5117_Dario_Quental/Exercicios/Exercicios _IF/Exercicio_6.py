compra=int(input("Qual o valor da compra? "))


if compra<=200:
    desconto=0.1
elif compra>200 and compra<=500:
    desconto=0.15
else:
    desconto=0.2

valor=compra*desconto
valorcompra=compra-valor

print("O novo total com desconto é",valorcompra,"€")
