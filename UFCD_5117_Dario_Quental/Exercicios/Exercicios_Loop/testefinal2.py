#Elabore uma base de dados de clientes de uma fábrica de materiais.
#O programa deverá possibilitar inserção e listagem dos clientes 
#bem como as compras por eles efetuadas
#( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ). 
#Divida final=compra – desconto, valor do desconto se compra for entre 100 e 200 é 5%,
#se for superior a 200 e inferior a 500 é 10% se superior a 500 é 15%.
#O programa deve validar todas as entradas e na listagem deve parar cliente a cliente
#e ser possível busca direta por número de cliente. 5v. 
#O programa deve conter (Estruturas 3v, funções .5v, Vetores .4v, apontadores .3v). 
compra=int(input("Introduza o valor da compra: "))
if compra >= 100 and compra <= 200:
    valor_desconto = compra *0.05
    valorfinal = compra - valor_desconto
    print(f"O valor a pagar é {valorfinal} euros")
elif compra > 200 and compra <=500:
    valor_desconto= compra *0.1
    valorfinal = compra - valor_desconto
    print(f"O valor a pagar é {valorfinal} euros")
elif compra >500:
    valor_desconto=compra*0.15
    valorfinal=compra -valor_desconto
    print(f"O valor a pagar é {valorfinal} euros")
else:
    print(f"O valor a pagar é {compra} euros")