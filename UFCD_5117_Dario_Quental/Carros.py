class Carro:
    def __init__(self,marca,modelo,ano,vel):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.vel=vel
    
    def Acelera(self,nivel):
        if nivel==1:
            self.vel+=10
        if nivel==2:
            self.vel+=15
        if nivel==3:
            self.vel+=20

    def Travar(self,nivel):
        if nivel==1:
            self.vel-=10
        if nivel==2:
            self.vel-=15
        if nivel==3:
            self.vel-=20
            
Carro1=Carro("BMW","M3","2020",0)
print("Velocidade", Carro1.vel)
Carro1.Acelera(1)
print("Velocidade", Carro1.vel)
Carro1.Acelera(2)
print("Velocidade", Carro1.vel)
Carro1.Travar(2)
print("Velocidade", Carro1.vel)
Carro1.Acelera(3)
print("Velocidade", Carro1.vel)
Carro1.Travar(3)
print("Velocidade", Carro1.vel)
Carro1.Travar(1)
print("Velocidade", Carro1.vel)