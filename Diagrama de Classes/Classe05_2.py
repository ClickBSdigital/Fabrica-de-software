# 4 - Classe Funcionário: Uma empresa quer criar um controle de pagamento para os 
# funcionários. Crie uma classe que modele um Funcionário com os seguintes atributos e 
# métodos:
#  Nome; Sobrenome; Horas_trabalhadas; Valor_hora;
#  A classe deve ter o seguintes métodos:
#  O método nomeCompleto deve escrever na tela o atributo nome concatenado ao atributo 
# sobrenome.
#  O método calcularSalario faz o cálculo de quanto o funcionário irá receber no mês, 
# multiplicando o atributo horasTrabalhadas pelo atributo valorPorHora. Em seguida, 
# escreve o valor na tela.
#  O método incrementarHoras adiciona um valor passado por parâmetro ao valor já 
# existente no atributo valorPorHora.
class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas=0, valor_hora=0.0):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nome_completo(self):
        print(f"Nome Completo: {self.nome} {self.sobrenome}")

    def calcular_salario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        print(f"Salário: R${salario:.2f}")

    def incrementar_horas(self, horas):
        if horas > 0:
            self.horas_trabalhadas += horas
            print(f"Horas trabalhadas incrementadas em {horas} horas.")
        else:
            print("O valor para incrementar deve ser positivo.")

# Exemplo de uso:
funcionario = Funcionario("Maria", "Silva", 160, 25.0)

funcionario.nome_completo()          # Nome completo do funcionário
funcionario.calcular_salario()       # Calcular salário com base nas horas trabalhadas e valor por hora

funcionario.incrementar_horas(20)    # Incrementar horas trabalhadas
funcionario.calcular_salario()       # Calcular salário novamente com as horas incrementadas


#######################
# Explicação da Classe Funcionario:
# Atributos:

# nome: Armazena o primeiro nome do funcionário.
# sobrenome: Armazena o sobrenome do funcionário.
# horas_trabalhadas: Armazena a quantidade de horas trabalhadas no mês. É inicializado com 0 por padrão.
# valor_hora: Armazena o valor pago por hora de trabalho. É inicializado com 0.0 por padrão.
# Métodos:

# nome_completo(): Exibe o nome completo do funcionário, concatenando nome e sobrenome.
# calcular_salario(): Calcula o salário do funcionário multiplicando horas_trabalhadas por
# valor_hora e exibe o resultado na tela.
# incrementar_horas(horas): Adiciona o número de horas especificado ao valor atual de 
# horas_trabalhadas. Se o valor de horas for positivo, a operação é realizada e uma mensagem 
# de confirmação é exibida.
# Exemplo de Uso:
# No exemplo de uso, criamos uma instância da classe Funcionario para uma funcionária chamada
# "Maria Silva". O salário é calculado com base nas horas trabalhadas e no valor por hora. 
# Depois, as horas trabalhadas são incrementadas, e o salário é recalculado com as novas horas.