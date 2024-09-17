# 5 - Classe Círculo: crie uma classe que represente um círculo. Esta classe deve possuir o 
# seguinte atributo:
#  raio
#  A classe deve ter os seguintes métodos:
#  imprimir o valor do raio;
#  calcular a área do círculo;
#  calcular a circunferência do círculo.
import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def imprimir_raio(self):
        print(f"Raio: {self.raio}")

    def calcular_area(self):
        area = math.pi * (self.raio ** 2)
        print(f"Área do círculo: {area:.2f}")

    def calcular_circunferencia(self):
        circunferencia = 2 * math.pi * self.raio
        print(f"Circunferência do círculo: {circunferencia:.2f}")

# Exemplo de uso:
circulo = Circulo(5)

circulo.imprimir_raio()            # Imprime o valor do raio
circulo.calcular_area()            # Calcula e imprime a área do círculo
circulo.calcular_circunferencia()  # Calcula e imprime a circunferência do círculo


# ##################################

# Explicação da Classe Circulo:
# Atributo:

# raio: Armazena o raio do círculo.
# Métodos:

# imprimir_raio(): Exibe o valor do raio do círculo.
# calcular_area(): Calcula a área do círculo usando a fórmula π * raio^2 e exibe o resultado.
# calcular_circunferencia(): Calcula a circunferência do círculo usando a fórmula 2 * π * raio
# e exibe o resultado.
# Exemplo de Uso:
# No exemplo de uso, criamos uma instância da classe Circulo com um raio de 5. O valor do raio 
# é impresso, seguido pelo cálculo e impressão da área e da circunferência do círculo.

# Fórmulas Usadas:
# Área do Círculo: 
# A
# ˊ
# rea
# =
# 𝜋
# ×
# (
# raio
# )
# 2
# A
# ˊ
#  rea=π×(raio) 
# 2
 
# Circunferência do Círculo: 
# Circunfer
# e
# ˆ
# ncia
# =
# 2
# ×
# 𝜋
# ×
# raio
# Circunfer 
# e
# ˆ
#  ncia=2×π×raio
# Se precisar de mais informações ou ajuda sobre como modelar classes em Python, 
# estou à disposição! Para mais informações e novidades, acesse GPT Chat Online.

# Experimente o nosso novo Kleurplaten - Gerador de Kleurplaat Gratuito.

# You said:
# import math explique?
# ChatGPT said:

# O comando import math em Python é usado para importar o módulo math, que é uma biblioteca 
# padrão fornecida pela linguagem Python. Este módulo contém um conjunto de funções e 
# constantes matemáticas que são úteis para realizar diversas operações matemáticas, 
# como cálculos trigonométricos, logaritmos, exponenciais, entre outros.

# O que o Módulo math Oferece?
# Aqui estão algumas das funções e constantes mais comuns disponíveis no módulo math:

# Funções Matemáticas Comuns:

# math.sqrt(x): Calcula a raiz quadrada de x.
# math.pow(x, y): Calcula x elevado à potência y.
# math.log(x): Calcula o logaritmo natural (base e) de x.
# math.log10(x): Calcula o logaritmo na base 10 de x.
# math.exp(x): Calcula e elevado à potência x.
# Funções Trigonométricas:

# math.sin(x): Calcula o seno de x (em radianos).
# math.cos(x): Calcula o cosseno de x (em radianos).
# math.tan(x): Calcula a tangente de x (em radianos).
# math.radians(x): Converte um ângulo de graus para radianos.
# math.degrees(x): Converte um ângulo de radianos para graus.
# Constantes Matemáticas:

# math.pi: Representa o valor de π (pi), aproximadamente 3.14159.
# math.e: Representa o valor de e, a base dos logaritmos naturais, aproximadamente 2.71828.
# Outras Funções Úteis:

# math.factorial(x): Calcula o fatorial de x.
# math.ceil(x): Arredonda x para cima, para o menor número inteiro maior ou igual a x.
# math.floor(x): Arredonda x para baixo, para o maior número inteiro menor ou igual a x.
# Exemplo de Uso do Módulo math:
# Aqui está um exemplo simples utilizando algumas funções do módulo math:

# python
# Copiar código
# import math

# # Cálculo da raiz quadrada
# raiz = math.sqrt(16)
# print(f"A raiz quadrada de 16 é: {raiz}")

# # Cálculo do seno de 45 graus (convertido para radianos)
# seno = math.sin(math.radians(45))
# print(f"O seno de 45 graus é: {seno}")

# # Cálculo da circunferência de um círculo de raio 5 usando math.pi
# raio = 5
# circunferencia = 2 * math.pi * raio
# print(f"A circunferência de um círculo de raio 5 é: {circunferencia}")
# Explicação do Exemplo:
# math.sqrt(16): Calcula a raiz quadrada de 16, resultando em 4.0.
# math.sin(math.radians(45)): Converte 45 graus para radianos e calcula o seno, 
# resultando em aproximadamente 0.7071.
# math.pi: Usado para calcular a circunferência de um círculo, com o valor de π multiplicado 
# por 2 e pelo raio.
# Conclusão:
# O comando import math é muito útil quando você precisa realizar operações matemáticas 
# avançadas em Python. Com ele, você pode acessar uma variedade de funções e constantes
# que facilitam a implementação de cálculos complexos.