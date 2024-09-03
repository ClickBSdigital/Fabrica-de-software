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
# Classe Funcionario
class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nome_completo(self):
        """Exibe o nome completo do funcionário."""
        print(f"Nome Completo: {self.nome} {self.sobrenome}")

    def calcular_salario(self):
        """Calcula e exibe o salário do funcionário."""
        salario = self.horas_trabalhadas * self.valor_hora
        print(f"Salário: {salario:.2f} euros")

    def incrementar_horas(self, horas):
        """Adiciona um valor ao número de horas trabalhadas."""
        if horas > 0:
            self.horas_trabalhadas += horas
            print(f"Horas trabalhadas atualizadas: {self.horas_trabalhadas} horas")
        else:
            print("O número de horas a ser incrementado deve ser positivo.")

# Exemplo de uso da classe
funcionario1 = Funcionario("João", "Silva", 160, 20.00)

# Usando os métodos da classe
funcionario1.nome_completo()            # Exibe o nome completo do funcionário
funcionario1.calcular_salario()         # Calcula e exibe o salário
funcionario1.incrementar_horas(10)      # Incrementa as horas trabalhadas
funcionario1.calcular_salario()         # Recalcula e exibe o novo salário após o incremento

# # =======================================
# Explicação do Código:
# Atributos:

# nome: Nome do funcionário.
# sobrenome: Sobrenome do funcionário.
# horas_trabalhadas: Número de horas trabalhadas no mês.
# valor_hora: Valor por hora trabalhada.
# Métodos:

# nome_completo(): Exibe o nome completo do funcionário, concatenando nome e sobrenome.
# calcular_salario(): Calcula o salário do funcionário multiplicando horas_trabalhadas pelo valor_hora e exibe o resultado.
# incrementar_horas(horas): Adiciona um valor ao número de horas trabalhadas, desde que seja positivo, e exibe a nova quantidade de horas.
# Exemplo de Uso:
# No exemplo, uma instância da classe Funcionario é criada. Os métodos da classe são utilizados para exibir o nome completo do funcionário, calcular o salário com base nas horas trabalhadas e no valor por hora, e incrementar as horas trabalhadas, recalculando o salário após o incremento.