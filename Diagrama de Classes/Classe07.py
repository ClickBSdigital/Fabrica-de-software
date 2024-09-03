# 7 - Classe Triangulo: Crie uma classe que modele um triangulo: 
# – Atributos: LadoA, LadoB, LadoC
# – Métodos: calcular Perímetro, getMaiorLado; 
#  Crie instâncias desta classe. Ele deve pedir ao usuário que informe as medidas de um 
# triangulo. Depois, deve criar um objeto com as medidas e imprimir sua área e maior lado.
import math

class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_perimetro(self):
        """Calcula o perímetro do triângulo."""
        return self.ladoA + self.ladoB + self.ladoC

    def get_maior_lado(self):
        """Retorna o maior lado do triângulo."""
        return max(self.ladoA, self.ladoB, self.ladoC)

    def calcular_area(self):
        """Calcula a área do triângulo usando a fórmula de Herão."""
        s = self.calcular_perimetro() / 2  # Semi-perímetro
        area = math.sqrt(s * (s - self.ladoA) * (s - self.ladoB) * (s - self.ladoC))
        return area

# Função para solicitar as medidas do triângulo ao usuário
def obter_medidas_do_usuario():
    ladoA = float(input("Informe o comprimento do lado A: "))
    ladoB = float(input("Informe o comprimento do lado B: "))
    ladoC = float(input("Informe o comprimento do lado C: "))
    return ladoA, ladoB, ladoC

# Obter as medidas do triângulo do usuário
ladoA, ladoB, ladoC = obter_medidas_do_usuario()

# Criar uma instância da classe Triangulo com as medidas fornecidas
triangulo = Triangulo(ladoA, ladoB, ladoC)

# Exibir o perímetro, maior lado e área do triângulo
print(f"Perímetro do triângulo: {triangulo.calcular_perimetro():.2f}")
print(f"Maior lado do triângulo: {triangulo.get_maior_lado():.2f}")
print(f"Área do triângulo: {triangulo.calcular_area():.2f}")


#############################

# Explicação da Classe Triangulo:
# Atributos:

# ladoA: Armazena o comprimento do lado A do triângulo.
# ladoB: Armazena o comprimento do lado B do triângulo.
# ladoC: Armazena o comprimento do lado C do triângulo.
# Métodos:

# calcular_perimetro(): Calcula e retorna o perímetro do triângulo, que é a soma dos três lados.
# get_maior_lado(): Retorna o comprimento do maior lado do triângulo usando a função max().
# calcular_area(): Calcula a área do triângulo usando a fórmula de Herão, que permite calcular a área com base nos três lados.
# Como Funciona:
# Entrada de Dados:

# O programa solicita ao usuário que insira os comprimentos dos três lados do triângulo (ladoA, ladoB, ladoC).
# Criação da Instância:

# Com os valores inseridos, uma instância da classe Triangulo é criada.
# Cálculo e Impressão dos Resultados:

# O programa calcula o perímetro, identifica o maior lado e calcula a área do triângulo.
# Esses valores são impressos na tela para o usuário.
# Exemplo de Uso:
# Se o usuário informar os valores 3, 4 e 5 para os lados do triângulo, o programa calculará e exibirá:

# arduino
# Copiar código
# Perímetro do triângulo: 12.00
# Maior lado do triângulo: 5.00
# Área do triângulo: 6.00
# Considerações:
# Fórmula de Herão: A fórmula de Herão é usada para calcular a área de um triângulo quando você conhece o comprimento de todos os três lados. A fórmula é 
# A
# ˊ
# rea
# =
# 𝑠
# (
# 𝑠
# −
# 𝑎
# )
# (
# 𝑠
# −
# 𝑏
# )
# (
# 𝑠
# −
# 𝑐
# )
# A
# ˊ
#  rea= 
# s(s−a)(s−b)(s−c)
# ​
#  , onde 
# 𝑠
# s é o semi-perímetro 
# 𝑠
# =
# 𝑎
# +
# 𝑏
# +
# 𝑐
# 2
# s= 
# 2
# a+b+c
# ​
#  .