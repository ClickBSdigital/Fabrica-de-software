# 2 - Classe Pessoa: Crie uma super classe que modele uma Pessoa. 
# Esta classe deve possuir os seguintes atributos:
# Matricula; Nome; Idade;  
# Subclasses:
# Defina as subclasses de Pessoa serão Aluno e Professor, estas devem conter além dos 
# atributos herdados de Pessoa seus atributos identificadores, ex: Classe Aluno (NOTAS; MEDIA). 
# Classe Professor (Formacao, Disciplina, Carga Horária e Salario)
# Você deve criar métodos específicos para cada subclasse, 
# ex: calcular_media, estudar, lecionar.

# Superclasse Pessoa
class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Matrícula: {self.matricula}")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

# Subclasse Aluno
class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas):
        super().__init__(matricula, nome, idade)
        self.notas = notas
        self.media = self.calcular_media()

    def calcular_media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        else:
            return 0

    def estudar(self):
        print(f"{self.nome} está estudando.")

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Notas: {self.notas}")
        print(f"Média: {self.media}")

# Subclasse Professor
class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga_horaria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def lecionar(self):
        print(f"{self.nome} está lecionando {self.disciplina}.")

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Formação: {self.formacao}")
        print(f"Disciplina: {self.disciplina}")
        print(f"Carga Horária: {self.carga_horaria} horas por semana")
        print(f"Salário: {self.salario} euros")

# Exemplo de uso das classes
aluno1 = Aluno(101, "Carlos Souza", 20, [8.0, 7.5, 9.0])
aluno1.mostrar_dados()
aluno1.estudar()

print("\n")

professor1 = Professor(202, "Ana Costa", 35, "Matemática", "Álgebra", 20, 2500)
professor1.mostrar_dados()
professor1.lecionar()


# Explicação do código:
# Superclasse Pessoa:

# Contém os atributos comuns a todas as pessoas: matricula, nome, idade.
# O método mostrar_dados() exibe os dados básicos da pessoa.
# Subclasse Aluno:

# Herda os atributos e métodos da classe Pessoa.
# Adiciona os atributos notas e media.
# O método calcular_media() calcula a média das notas do aluno.
# O método estudar() simula a ação de estudar.
# O método mostrar_dados() é reescrito para incluir as notas e a média do aluno.
# Subclasse Professor:

# Herda os atributos e métodos da classe Pessoa.
# Adiciona os atributos formacao, disciplina, carga_horaria, e salario.
# O método lecionar() simula a ação de lecionar uma disciplina.
# O método mostrar_dados() é reescrito para incluir as informações específicas do professor.
# Testes:
# No exemplo, criamos instâncias das classes Aluno e Professor, chamando os métodos para demonstrar como as subclasses funcionam.