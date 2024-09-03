# 6 - Classe Funcionário: Crie uma super classe que modele um Funcionário genérico. 
# Esta classe deve possuir os seguintes atributos:
# Nome;
# Matricula;
# Salario;
# Método:
# Bater_ponto(): deve criar uma lista de pontos do funcionário, pode ser booleana 0 ou 1;
# Subclasses:
# Defina as subclasses de Funcionário, exemplo Vendedor e Gerente. 
# Após a criação das subclasses você deve criar atributos e métodos específicos de cada subclasse;
# Ex: atributo comissão e método bater_meta() para Vendedor e atributo senha para o Gerente.
class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.lista_pontos = []

    def bater_ponto(self, ponto):
        if ponto in [0, 1]:  # Verifica se o ponto é 0 (ausente) ou 1 (presente)
            self.lista_pontos.append(ponto)
            status = "presente" if ponto == 1 else "ausente"
            print(f"{self.nome} marcou o ponto como {status}.")
        else:
            print("Ponto inválido! Use 1 para presente e 0 para ausente.")

    def mostrar_pontos(self):
        print(f"Pontos de {self.nome}: {self.lista_pontos}")

# Subclasse Vendedor
class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao

    def bater_meta(self, vendas, meta):
        if vendas >= meta:
            print(f"{self.nome} atingiu a meta! Receberá uma comissão de {self.comissao}.")
        else:
            print(f"{self.nome} não atingiu a meta.")

# Subclasse Gerente
class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha

    def validar_senha(self, senha):
        if senha == self.senha:
            print(f"Senha válida. Acesso concedido ao gerente {self.nome}.")
        else:
            print("Senha inválida. Acesso negado.")

# Exemplo de uso das classes
vendedor = Vendedor("Carlos Silva", 1234, 2500.00, 500.00)
vendedor.bater_ponto(1)
vendedor.bater_meta(10, 8)
vendedor.mostrar_pontos()

print("\n")

gerente = Gerente("Ana Costa", 5678, 5000.00, "senha123")
gerente.bater_ponto(1)
gerente.validar_senha("senha123")
gerente.mostrar_pontos()

# Explicação do código:
# Superclasse Funcionario:

# Contém os atributos básicos comuns a todos os funcionários: nome, matricula, salario.
# O método bater_ponto(ponto) permite registrar se o funcionário está presente (1) ou ausente (0) em um determinado dia.
# O método mostrar_pontos() exibe a lista de pontos do funcionário.
# Subclasse Vendedor:

# Herda os atributos e métodos da classe Funcionario.
# Adiciona o atributo comissao, que representa a comissão do vendedor.
# O método bater_meta(vendas, meta) verifica se o vendedor atingiu a meta de vendas e, se sim, informa sobre a comissão recebida.
# Subclasse Gerente:

# Herda os atributos e métodos da classe Funcionario.
# Adiciona o atributo senha, que representa a senha de acesso do gerente.
# O método validar_senha(senha) verifica se a senha fornecida corresponde à senha do gerente, permitindo ou negando o acesso.
# Testes:
# No exemplo, criamos instâncias das classes Vendedor e Gerente e utilizamos os métodos específicos de cada uma, além dos métodos herdados da classe Funcionario.