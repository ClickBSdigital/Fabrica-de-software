class Pessoa:  #SUPERCLASSE 10 ATRIBUTOS
    def __init__(self,nome,endereco,telefone):
        self.name = nome #ATRIBUTO PRIVADO
        self.local = endereco
        self.fone = telefone
    
    def hello(self):
        print(f" Olá {self.name}")

    def imprimeEndereco(self):
        print(self.local)


p1 = Pessoa("THIAGO","AV AFONSO PENA, 99",67999999)

print(p1.name)

p1.hello()
p1.imprimeEndereco()

p1.name = "TEODORO"
p1.hello()