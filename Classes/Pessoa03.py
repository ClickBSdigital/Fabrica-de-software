class Pessoa:  #SUPERCLASSE  , SE TIVER 10 CLASSES
    def __init__(self,nome,endereco,telefone):
        self.nome = nome  #####self.__nome = nome / / / ATRIBUTO PRIVADO
        self.local = endereco
        self.fone = telefone

    def hello(self):
        print(f"Olá {self.nome}")

    def imprimeEndereco(self):
        print(self.local)

class PessoaFisica(Pessoa):  #SUBCLASSE  , ERDARIA AS 10 CLASSES
    def __init__(self, nome, endereco, telefone,cpf,rg):
        super().__init__(nome, endereco, telefone)
        self.cpf = cpf
        self.rg = rg

class PessoaJuridica(Pessoa):  #SUBCLASSE
    def __init__(self, nome, endereco, telefone,cnpj,ie):
        super().__init__(nome, endereco, telefone)
        self.cnpj = cnpj
        self.ie = ie

    def hello(self): ###### POLIMORFISMO -> PODER REESCREVER UM MÉTODO HERDADO
        print(f"HELLO PJ {self.nome} CNPJ {self.cnpj}")

    def getCNPJ(self):
        return self.cnpj

p1 = Pessoa("THIAGO","RUA RUA RUA", "6732321381")

pes1 = PessoaFisica("JOAO","RUA","999","65421544","4651254654")
pes1.hello()
pes1.imprimeEndereco()
print()
empresa = PessoaJuridica("CLARO","SÃO PAULO","11333333","541532168212000156","4568451555")
empresa.hello()
empresa.imprimeEndereco()
print()

x = empresa.getCNPJ
print(x)

