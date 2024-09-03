# 8 - Classe Aluno_Academia: Uma academia mantem registro de seus alunos e precisa
# armazenar os seguintes atributos:
#  Nome, Idade, Peso, Altura, Mensalidade (valor default: R$ 120,00)
#  A academia faz um desconto especial para menores de idade, portanto, é
# necessário saber distinguir entre um aluno maior e menor. Além disso, a
# academia também tem interesse em acompanhar o desempenho de seus alunos,
# por isso, ela também necessita conhecer o índice de massa corporal (IMC) deles,
# para isso a classe deve ter os seguintes métodos:
#  Calcular_IMC()
#  Obter_valor_mensalidade()
class AlunoAcademia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def calcular_IMC(self):
        """Calcula o Índice de Massa Corporal (IMC) do aluno."""
        imc = self.peso / (self.altura ** 2)
        return imc

    def obter_valor_mensalidade(self):
        """Retorna o valor da mensalidade, com desconto para menores de idade."""
        if self.idade < 18:
            desconto = self.mensalidade * 0.2  # 20% de desconto
            valor_final = self.mensalidade - desconto
            print(f"Desconto aplicado: R${desconto:.2f}")
        else:
            valor_final = self.mensalidade

        return valor_final

    def exibir_informacoes(self):
        """Exibe as informações do aluno, incluindo IMC e mensalidade."""
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")
        print(f"IMC: {self.calcular_IMC():.2f}")
        print(f"Mensalidade: R${self.obter_valor_mensalidade():.2f}")

# Exemplo de uso:
nome = input("Informe o nome do aluno: ")
idade = int(input("Informe a idade do aluno: "))
peso = float(input("Informe o peso do aluno (em kg): "))
altura = float(input("Informe a altura do aluno (em metros): "))

# Criar uma instância da classe AlunoAcademia
aluno = AlunoAcademia(nome, idade, peso, altura)

# Exibir as informações do aluno, incluindo IMC e valor da mensalidade
aluno.exibir_informacoes()



#############################################

# Explicação da Classe AlunoAcademia:
# Atributos:

# nome: Armazena o nome do aluno.
# idade: Armazena a idade do aluno.
# peso: Armazena o peso do aluno em quilogramas.
# altura: Armazena a altura do aluno em metros.
# mensalidade: Armazena o valor da mensalidade, com valor padrão de R$ 120,00.
# Métodos:

# calcular_IMC(): Calcula e retorna o Índice de Massa Corporal (IMC) do aluno usando a fórmula 
# IMC
# =
# peso
# altura
# 2
# IMC= 
# altura 
# 2
 
# peso
# ​
#  .
# obter_valor_mensalidade(): Verifica se o aluno é menor de idade (idade < 18). Se for, aplica um desconto de 20% na mensalidade e retorna o valor final.
# exibir_informacoes(): Exibe todas as informações do aluno, incluindo o IMC e o valor da mensalidade.
# Como Funciona:
# Entrada de Dados:

# O programa solicita ao usuário que insira o nome, idade, peso e altura do aluno.
# Criação da Instância:

# Com os valores inseridos, uma instância da classe AlunoAcademia é criada.
# Cálculo e Impressão dos Resultados:

# O programa calcula o IMC, verifica se o aluno tem direito a desconto na mensalidade, e exibe todas essas informações na tela.
# Exemplo de Uso:
# Se o usuário informar um aluno chamado "Carlos" com idade 16, peso 70 kg, e altura 1.75 m, o programa calculará o IMC, aplicará o desconto na mensalidade, e exibirá:

# yaml
# Copiar código
# Nome: Carlos
# Idade: 16 anos
# Peso: 70.0 kg
# Altura: 1.75 m
# IMC: 22.86
# Desconto aplicado: R$24.00
# Mensalidade: R$96.00
# Considerações:
# Desconto para Menores de Idade: O desconto é de 20% para alunos menores de 18 anos.
# Fórmula do IMC: O IMC é calculado dividindo o peso pela altura ao quadrado.