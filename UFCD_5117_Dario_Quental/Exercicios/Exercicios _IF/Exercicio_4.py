saldo=int(input("Qual o valor do seu saldo bancário? "))
cheque=int(input("Qual o valor do cheque a debitar? "))

if saldo>cheque:
    novosaldo=saldo-cheque
    print("o seu novo saldo é:",novosaldo)
else:
    print("Saldo insuficiente")