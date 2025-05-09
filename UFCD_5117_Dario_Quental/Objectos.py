class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
        
    def renovaridade(self,idade):
        self.idade=idade

Pessoas=[]

for i in range(3):    
    nom=input("Introduza o nome")
    idad=input("Introduza a idade")
    Pessoas.append(Pessoa(nom,idad))
    print("O nome é",Pessoas[i].nome)
    print("A idade é",Pessoas[i].idade)
    novaidad=input("Introduza a nova idade")
    Pessoas[i].renovaridade(novaidad)
    print("O nome é",Pessoas[i].nome)
    print("A idade é",Pessoas[i].idade)





"""
def introdnome(nom):           #comportamentos da classe pessoa
    global nome
    nome=nom

def mostrarnome():         #comportamentos d classe pessoa
    print("O seu nome é", nome)

introdnome(input("Introduza o nome"))
mostrarnome()
"""