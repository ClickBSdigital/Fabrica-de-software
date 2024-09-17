class Animal:
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor
    
    def mover(self):
        print(f" {self.nome} andou... ")


class Cachorro(Animal):
    def __init__(self, nome, cor, raca):
        super().__init__(nome, cor)
        self.raca = raca

    def mover(self):
        print(f" {self.nome} cooorrrreeuuuuuu... ")


class Peixe(Animal):
    def __init__(self, nome, cor, peso):
        super().__init__(nome, cor)
        self.peso = peso

    def mover(self):
        print(f" {self.nome} nadou... ")
    

dog1 = Cachorro("TOTO","CARAMELO","VIRALATA")
dog1.mover()

peixe1 = Peixe("NEMO","AZUL",8)
peixe1.mover()

print(peixe1.nome)
        