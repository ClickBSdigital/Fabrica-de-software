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
class AlunoAcad:
    def __init__(self, nome, idade, peso, altura, mensalidade=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade
    
    def calculaIMC(self):
        """Calcula e retorna o IMC do aluno."""
        imc = self.peso / (self.altura ** 2)
        return round(imc, 2)
    
    def calculaDesconto(self):
        """Calcula e retorna a mensalidade com desconto se aplicável."""
        if self.idade < 18:
            desconto = self.mensalidade * 0.20
            return self.mensalidade - desconto
        else:
            return self.mensalidade

# Criando uma instância da classe AlunoAcad
juju = AlunoAcad("JOÃO", 99, 45, 1.60)

# Calculando e exibindo o IMC
imc = juju.calculaIMC()
print(f"IMC de {juju.nome}: {imc}")

# Exibindo a mensalidade original
print(f"Mensalidade original: {juju.mensalidade} reais")

# Calculando e exibindo a mensalidade com desconto
desc = juju.calculaDesconto()
print(f"Mensalidade com desconto: {desc} reais")


# ========================================


# Explicações das Melhorias:
# Método calculaIMC():

# O cálculo do IMC foi mantido, mas agora o valor é arredondado para duas casas decimais, usando round(imc, 2), para uma apresentação mais limpa e típica para valores de IMC.
# Método calculaDesconto():

# O cálculo do desconto foi ajustado para que a mensalidade seja reduzida corretamente em 20% se o aluno for menor de 18 anos. O método retorna a mensalidade com desconto se aplicável ou a mensalidade original se o aluno não for elegível para desconto.
# Instância juju:

# A instância juju da classe AlunoAcad é criada com os valores fornecidos, e tanto o IMC quanto a mensalidade com desconto são calculados e exibidos.
# Exemplo de Saída:
# Se o código for executado, ele imprimirá o IMC de "JUAO" e a mensalidade, tanto antes quanto após a aplicação do desconto (se aplicável). No caso do aluno "JUAO", como ele tem 99 anos, ele não recebe desconto, então a mensalidade permanece a mesma.

# Este código refatorado é mais robusto e legível, oferecendo um cálculo preciso do IMC e do desconto na mensalidade baseado na idade do aluno.