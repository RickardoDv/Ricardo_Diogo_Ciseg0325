notas=[]
i=1

for i in range(10):
    notas.append(float(input("Introduza a nota do aluno: ")))

soma_notas=sum(notas)
contagem=len(notas)

print(contagem)
print(soma_notas)