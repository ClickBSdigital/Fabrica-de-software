############CLASSE PESSOA 
##ABSTRAÇÃO DO OBJETO PESSOA NA PROGRAMAÇÃO  POO

######ATRIBUTOS NOME,IDADE,EMAIL,CIDADE
######MÉTODOS comer, dormir, estudar (AÇÕES -> FUNÇÕES -> MÉTODOS)
class Pessoa:
    def __init__(self,nome,idade,email,cidade):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cidade = cidade

    def oi(self):
        print(f' Olá {self.nome}')

###### INSTANCIAR UMA CLASSE
pes1 = Pessoa("JOAO",18,"joao@gmail","CG")
print(pes1.nome)
print(pes1.idade)

pes2 = Pessoa("Maria",52,"maria@gmail.com","RJ")
print(pes2.nome)
print(pes2.idade)
pes2.oi

