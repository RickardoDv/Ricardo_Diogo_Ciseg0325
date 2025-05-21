prova1=float(input("Qual a nota da primeira prova? "))
prova2=float(input("Qual a nota da segunda prova? "))
prova3=float(input("Qual a nota da terceira prova? "))

nota1=prova1*0.2
nota2=prova2*0.3
nota3=prova3*0.5

media=(prova1+prova2+prova3)/10

if media >= 6:
    print("Aprovado",media)
else:
    print("Reprovado",media)