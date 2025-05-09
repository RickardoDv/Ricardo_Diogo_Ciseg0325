class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.vel=0
        self.ligado=False
        self.luzes=False
    
    def getmarca (self):
        return self.marca
    
    def getmodelo (self):
        return self.modelo 
      
    def getano (self):
        return self.ano
    
    def getvelocidade (self):
        return self.vel
    
    def getligado (self):
        return self.ligado
    
    def getluzes (self):
        return self.luzes
    
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
            
Carro1=Carro("BMW","M3","2020")
print("Velocidade", Carro1.getvelocidade())
Carro1.Acelera(int(input("qual a Velocidade de 1 a 3")))
print("Velocidade", Carro1.getvelocidade())
Carro1.Acelera(2)
print("Velocidade", Carro1.getvelocidade())
Carro1.Travar(2)
print("Velocidade", Carro1.getvelocidade())
Carro1.Acelera(3)
print("Velocidade", Carro1.getvelocidade())
Carro1.Travar(3)
print("Velocidade", Carro1.getvelocidade())
Carro1.Travar(1)
print("Velocidade", Carro1.getvelocidade())