# 5 - Classe Círculo: crie uma classe que represente um círculo. Esta classe deve possuir o 
# seguinte atributo:
#  raio
#  A classe deve ter os seguintes métodos:
#  imprimir o valor do raio;
#  calcular a área do círculo;
#  calcular a circunferência do círculo.
import math

# Classe Circulo
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def imprimir_raio(self):
        """Imprime o valor do raio do círculo."""
        print(f"Raio do círculo: {self.raio}")

    def calcular_area(self):
        """Calcula e retorna a área do círculo."""
        area = math.pi * (self.raio ** 2)
        print(f"Área do círculo: {area:.2f} unidades quadradas")
        return area

    def calcular_circunferencia(self):
        """Calcula e retorna a circunferência do círculo."""
        circunferencia = 2 * math.pi * self.raio
        print(f"Circunferência do círculo: {circunferencia:.2f} unidades")
        return circunferencia

# Exemplo de uso da classe
circulo1 = Circulo(5)

# Usando os métodos da classe
circulo1.imprimir_raio()             # Imprime o valor do raio
circulo1.calcular_area()             # Calcula e imprime a área do círculo
circulo1.calcular_circunferencia()   # Calcula e imprime a circunferência do círculo

# +++++++++++++++++=================================

# Explicação do Código:
# Atributos:

# raio: Representa o raio do círculo.
# Métodos:

# imprimir_raio(): Exibe o valor do raio do círculo.
# calcular_area(): Calcula a área do círculo usando a fórmula 
# Area = 𝜋 × raio 2
# Area = π × raio 2
#   e exibe o resultado.
# calcular_circunferencia(): Calcula a circunferência do círculo usando a fórmula 
# Circunferencia = 2 × 𝜋 × raio
# Circunferencia = 2 × π × raio e exibe o resultado.
# Exemplo de Uso:
# No exemplo, uma instância da classe Circulo é criada com um raio de 5 unidades. Os métodos da classe são utilizados para exibir o raio, calcular a área, e calcular a circunferência do círculo.