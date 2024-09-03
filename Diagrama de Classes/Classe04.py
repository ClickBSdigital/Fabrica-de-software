# 4 - Classe Conta: Um banco mantém contas de clientes armazenando o número da conta, o 
# nome do cliente e o saldo atual da conta. Crie uma classe que modele um Conta-Corrente.
#  Nome;
#  CPF;
#  Numero;
#  Saldo;
#  A classe deve ter o seguintes métodos:
#  Depositar()
#  Sacar() - OBS: somente enquanto a conta possuir saldo positivo
#  Imprimir saldo()
##############################################+++++++++++
# class Conta:
#   def __init__(self,nome,cpf,numero,saldo):
#     self.nome = nome
#     self.cpf = cpf
#     self.numero = numero
#     self.saldo = saldo
    
#   def somaDeposito(self):
#     dep = float(input("DIGITE O VALOR DO DEPÓSITO R$: "))
#     novoValor = (self.saldo) + dep
####################################+++++++++++++++++++++
class ContaCorrente:
    def __init__(self, nome, cpf, numero, saldo=0.0):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        elif valor <= 0:
            print("O valor do saque deve ser positivo.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def imprimir_saldo(self):
        print(f"Saldo atual da conta {self.numero}: R${self.saldo:.2f}")

# Exemplo de uso:
conta = ContaCorrente("João Silva", "123.456.789-00", "001122-3", 1000.0)

conta.imprimir_saldo()  # Saldo inicial

conta.depositar(500.0)  # Depositar
conta.imprimir_saldo()  # Verificar saldo após depósito

conta.sacar(200.0)      # Sacar
conta.imprimir_saldo()  # Verificar saldo após saque

conta.sacar(1500.0)     # Tentativa de saque com valor superior ao saldo

# Explicação da Classe ContaCorrente:
# Atributos:

# nome: Armazena o nome do titular da conta.
# cpf: Armazena o CPF do titular da conta.
# numero: Armazena o número da conta.
# saldo: Armazena o saldo atual da conta, inicializado com um valor padrão de 0.0.
# Métodos:

# depositar(valor): Recebe um valor e o adiciona ao saldo da conta se o valor for positivo.
# sacar(valor): Verifica se há saldo suficiente na conta e se o valor é positivo antes de 
# realizar o saque. Se o saldo for insuficiente ou o valor for inválido, uma mensagem de
# erro é exibida.
# imprimir_saldo(): Exibe o saldo atual da conta.
# Exemplo de Uso:
# No exemplo de uso, criamos uma instância da classe ContaCorrente para um cliente chamado 
# "João Silva". 
# Depois, fazemos um depósito, um saque válido, e tentamos realizar um saque superior ao 
# saldo disponível, demonstrando como cada método funciona.