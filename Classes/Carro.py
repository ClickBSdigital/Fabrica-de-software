class Carro:
    def __init__(self,marca,modelo,cor,ano,valor,nivel=5) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.nivel = nivel
        self.consumo = 8
        self.valor = valor
        self.ligado = False

    def ligar(self):
        self.ligado = True
        return f" {self.modelo} ligado....."

    def desligar(self):
        self.ligado = False
        return "CARRO DESLIGADO"

    def calculaImposto(self):
        imposto = self.valor * 0.025
        return imposto
    
    def abastecer(self,quant):
        self.nivel += quant
    
    def verificaNivel(self):
        return self.nivel
    
    def andar(self,km):
        litros = km / self.consumo
        self.nivel -= litros
        print("CONSUMO....",litros)


car1 = Carro("CHEVROLET","CELTA","PRATA",2012,79000)
imp = car1.calculaImposto()
print(imp)
car1.abastecer(30)
print(car1.verificaNivel())
car1.andar(65)
print(car1.verificaNivel())