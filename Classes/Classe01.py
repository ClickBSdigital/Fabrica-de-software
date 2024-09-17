# 1 - Classe Pessoa: Crie uma classe que modele uma pessoa. Esta classe deve possuir os 
# seguintes atributos:
#  Nome
#  Idade
#  Endereço
#  A classe deve ter os seguintes métodos:
#  Mostrar nome;
#  Alterar a idade;
#  Imprimir endereço.
# Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_nome(self):
        """Mostra o nome da pessoa."""
        print(f"Nome: {self.nome}")

    def alterar_idade(self, nova_idade):
        """Altera a idade da pessoa para um novo valor."""
        self.idade = nova_idade
        print(f"A idade de {self.nome} foi alterada para {self.idade} anos.")

    def imprimir_endereco(self):
        """Imprime o endereço da pessoa."""
        print(f"Endereço: {self.endereco}")

# Exemplo de uso da classe
pessoa1 = Pessoa("João Silva", 30, "Rua das Flores, 123, Lisboa")

# Usando os métodos da classe
pessoa1.mostrar_nome()           # Exibe o nome da pessoa
pessoa1.alterar_idade(31)        # Altera a idade da pessoa para 31 anos
pessoa1.imprimir_endereco()      # Exibe o endereço da pessoa

# # +++++===================================
# Explicação do Código:
# Atributos:

# nome: Representa o nome da pessoa.
# idade: Representa a idade da pessoa.
# endereco: Representa o endereço da pessoa.
# Métodos:

# mostrar_nome(): Exibe o nome da pessoa.
# alterar_idade(nova_idade): Permite alterar a idade da pessoa para um novo valor fornecido.
# imprimir_endereco(): Exibe o endereço da pessoa.
# Exemplo de Uso:
# Ao criar uma instância da classe Pessoa, você pode utilizar os métodos para exibir o nome, alterar a idade e imprimir o endereço da pessoa.