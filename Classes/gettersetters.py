class Pessoa:  #SUPERCLASSE 10 ATRIBUTOS
    def __init__(self,nome,endereco,telefone,idade=0):
        self.__name = nome #ATRIBUTO PRIVADO
        self.local = endereco
        self.fone = telefone
        self.idade = idade

    def getNome(self):
        return self.__name
    
    def setNome(self,novo):
        self.__name = novo

    def verificaIdade(self):
        if self.idade > 18:
            return True
        else:
            return "TEXTO MENOR"

    def setEndereco(self,novo_end):
        self.local = novo_end
    
    def getEndereco(self):
        return self.local
    
    def getTelefone(self):
        return self.fone

    def setTelefone(self,novo_fone):
        self.fone = novo_fone


p1 = Pessoa("JOAO","RUA BARAO DO RIO BRANCO, 666",9999,17)
p1.setNome("THIAGO ALMEIDA DA SILVA")
nomedapessoa = p1.getNome()
print(nomedapessoa)

print(p1.getEndereco())

p1.setEndereco("AERO RANCHO")
print(p1.getEndereco())


teste = p1.verificaIdade()

print(teste)