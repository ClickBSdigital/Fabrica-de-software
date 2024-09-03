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
# Classe ContaCorrente
class ContaCorrente:
    def __init__(self, nome, cpf, numero, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        """Deposita um valor na conta, aumentando o saldo."""
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor:.2f} euros realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """Saca um valor da conta, diminuindo o saldo, desde que o saldo seja suficiente."""
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de {valor:.2f} euros realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def imprimir_saldo(self):
        """Imprime o saldo atual da conta."""
        print(f"Saldo atual: {self.saldo:.2f} euros")

# Exemplo de uso da classe
conta1 = ContaCorrente("Ana Pereira", "123.456.789-00", "0001-1", 500.00)

# Usando os métodos da classe
conta1.imprimir_saldo()          # Imprime o saldo inicial
conta1.depositar(200.00)         # Realiza um depósito
conta1.imprimir_saldo()          # Imprime o saldo após o depósito
conta1.sacar(100.00)             # Realiza um saque
conta1.imprimir_saldo()          # Imprime o saldo após o saque
conta1.sacar(700.00)             # Tenta realizar um saque maior que o saldo disponível
conta1.imprimir_saldo()          # Imprime o saldo final


# # ++++++++++++++++================================
# Explicação do Código:
# Atributos:

# nome: Nome do cliente.
# cpf: CPF do cliente.
# numero: Número da conta-corrente.
# saldo: Saldo atual da conta, inicializado com um valor padrão de 0.
# Métodos:

# depositar(valor): Aumenta o saldo da conta com o valor fornecido, desde que seja positivo.
# sacar(valor): Diminui o saldo da conta com o valor fornecido, desde que o saldo seja suficiente e o valor seja positivo.
# imprimir_saldo(): Exibe o saldo atual da conta.
# Exemplo de Uso:
# No exemplo, uma instância da classe ContaCorrente é criada com um saldo inicial. Os métodos da classe são utilizados para realizar operações como depósito, saque, e impressão do saldo, demonstrando o funcionamento da conta-corrente.