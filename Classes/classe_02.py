class Aluno:
    def __init__(self,nome,idade,email,nota=0): #método construtor
        self.__nome = nome #atributo privado
        self.idade = idade
        self.email = email
        self.nota = nota

    def hello(self):    #####MÉTODO DA CLASSE
        print(f"Hello {self.__nome}")

    def getIdade(self):
        return self.idade

a1 = Aluno("THIAGO",28,"thiago@gmail.com")

print(a1.nome)