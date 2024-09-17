class Pessoa:
    def __init__(self,nome,endereco,telefone):
        self.nome = nome
        self.local = endereco
        self.fone = telefone

    def hello(self):
        print(f"Olá {self.nome}")

pes1 = Pessoa("JOAO","AV AFONSO PENA","67999999999")
pes1.hello()