class Pessoa:  #SUPERCLASSE  , SE TIVER 10 CLASSES
    def __init__(self,nome,endereco,telefone,idade):
        self.__name = nome  #####self.__nome = nome / / / ATRIBUTO PRIVADO
        self.local = endereco
        self.fone = telefone
        self.idade = idade


    def getNome(self):
        return self.__name
    
    def setNome(self,novo_nome):
        self.__name = novo_nome

    def verificaIdade(self):
        if self.idade > 18:
            return True
        else:
            return False

    
    def setEndereco(self,novo_endereco):
        self.local = novo_endereco

    def getEndereco(self,novo_endereco):
        self.local = novo_endereco

    def setTelefone(self,novo_fone):
        self.fone = novo_fone

p1 = Pessoa("JOAO", "RUA RUA, 666", 9999)
p1.setNome("thiago almeida da silva")
print(p1.getNome())
nomedapessoa = p1.getNome()
print(nomedapessoa) 

print(p1.getEndereco())

teste = p1.verificaIdade

if teste:
    print("MAIOR DE IDADE")

else:
    print("IDADE MENOR")