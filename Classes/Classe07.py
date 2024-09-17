class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcularPerimetro(self):
        """Calcula e retorna o perímetro do triângulo."""
        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro
    
    def getMaiorLado(self):
        """Retorna qual é o maior lado do triângulo."""
        if self.ladoA >= self.ladoB and self.ladoA >= self.ladoC:
            return "LADO A É O MAIOR"
        elif self.ladoB >= self.ladoA and self.ladoB >= self.ladoC:
            return "LADO B É O MAIOR"
        else:
            return "LADO C É O MAIOR"
        
# Criando uma instância da classe Triangulo
tri1 = Triangulo(35, 45, 23)

# Exibindo os lados do triângulo
print("LADO A:", tri1.ladoA)
print("LADO B:", tri1.ladoB)
print("LADO C:", tri1.ladoC)

# Calculando e exibindo o maior lado
print(tri1.getMaiorLado())

# ==================================================:

# Explicação das Modificações:
# Correção no Método getMaiorLado():

# A lógica anterior estava usando operadores lógicos (or) de forma incorreta. Em vez de comparar todos os lados entre si, ela apenas verificava um lado em relação a um valor booleano, o que é inadequado.
# Agora, o método compara corretamente ladoA, ladoB, e ladoC para determinar qual deles é o maior, retornando a informação correta.
# Testes com os Lados:

# O exemplo testa a instância tri1 com os valores 35, 45, e 23 para os lados A, B e C, respectivamente.
# O método getMaiorLado() deve retornar "LADO B É O MAIOR" porque ladoB é o maior valor entre os três.
# Com essas correções, o código funcionará corretamente para identificar o maior lado do triângulo, além de calcular o perímetro do triângulo.