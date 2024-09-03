class Pessoa:  #SUPERCLASSE 10 ATRIBUTOS
    def __init__(self,nome,endereco,telefone):
        self.name = nome #ATRIBUTO PRIVADO
        self.local = endereco
        self.fone = telefone
    
    def hello(self):
        print(f" Olá {self.name}")

    def imprimeEndereco(self):
        print(self.local)


class PessoaFisica(Pessoa):  #SUBCLASSE
    def __init__(self, nome, endereco, telefone,cpf,rg):
        super().__init__(nome, endereco, telefone)
        self.cpf = cpf
        self.rg = rg

class PessoaJuridica(Pessoa):
    def __init__(self, nome, endereco, telefone,cnpj,ie):
        super().__init__(nome, endereco, telefone)
        self.cnpj = cnpj
        self.ie = ie

    def hello(self): ####POLIMORFISMO -> PODER REESCREVER UM MÉTODO HERDADO
        print(f" HELLO PJ {self.name} CNPJ: {self.cnpj} ")

    def getCNPJ(self):
        return self.cnpj
    

empresa = PessoaJuridica("CLARO","SAO PAULO",1199999,123456789,789798)
empresa.hello()

empresa.imprimeEndereco()
cnpj = empresa.getCNPJ()
print(cnpj)
