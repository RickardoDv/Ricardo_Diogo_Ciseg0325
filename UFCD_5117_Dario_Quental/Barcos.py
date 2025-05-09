class Barco:
    def __init__(self,marca,tipo,ano,carga):
        self.marca=marca
        self.tipo=tipo
        self.ano=ano
        self.carga=carga
    
    def Carga(self,carga):
        if carga==1:
            self.carga+=100
        if carga==2:
            self.carga+=200

    def Descarga(self,nivel):
        if nivel==1:
            self.carga-=100
        if nivel==2:
            self.carga-=200

Barco1=Barco("Maersk","Cargueiro","2012",0)

print(Barco1.tipo,Barco1.marca,"carga atual", Barco1.carga,"toneladas")
Barco1.Carga(2)
print(Barco1.tipo,Barco1.marca,"carga atual", Barco1.carga,"toneladas")
Barco1.Descarga(1)
