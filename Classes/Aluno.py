class Aluno:
    def __init__(self,nome,idade,n1,n2,n3,n4):
        self.nome = nome  
        self.idade = idade
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4

    def getDados(self):
        print(f" {self.nome} tem {self.idade}")
    
    def mostrarSituation(self):
        media = (self.n1 + self.n2 + self.n3 + self.n4) / 4
        if media < 4.0:
            return "REPROVADO"
        elif media >= 4.0 and media < 5.9:
            return "EXAME"
        else:
            return "APROVADO"

    
aluno = Aluno("Juliana Juju",17,6,5,5,4)

print(aluno.nome)
print(aluno.n4)

situacao = aluno.mostrarSituation()

print(situacao)