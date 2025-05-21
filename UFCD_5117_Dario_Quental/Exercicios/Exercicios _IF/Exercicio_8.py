"""
aluno1=float(input("Qual a nota de 0-20 do 1º aluno? "))
aluno2=float(input("Qual a nota de 0-20 do 2º aluno? "))
aluno3=float(input("Qual a nota de 0-20 do 3º aluno? "))
aluno4=float(input("Qual a nota de 0-20 do 4º aluno? "))
aluno5=float(input("Qual a nota de 0-20 do 5º aluno? "))
aluno6=float(input("Qual a nota de 0-20 do 6º aluno? "))
aluno7=float(input("Qual a nota de 0-20 do 7º aluno? "))
aluno8=float(input("Qual a nota de 0-20 do 8º aluno? "))
aluno9=float(input("Qual a nota de 0-20 do 9º aluno? "))
aluno10=float(input("Qual a nota de 0-20 do 10º alno? "))
"""
#soma=aluno1+aluno2+aluno3+aluno4+aluno5+aluno6+aluno7+aluno8+aluno9+aluno10
#media=soma/10

#if aluno1 >= media:
#    print ("O aluno teve nota acima da média.")

# ISTO VAI OCUPAR MUITO ESPAÇO =|

##### CODIGO MAIS SIMPLES ##### (ou talvez não)
lista= []
acima_media=[]

for i in range(10):
    nota=int(input("Insira a nota do aluno: "))
    lista.append(nota)
    
media=sum(lista)/len(lista)
print("A media das notas é ",media)

for nota in lista:
    if nota >= media:
      acima_media.append(nota)  

print(len(acima_media),"Alunos ficaram acima da média")