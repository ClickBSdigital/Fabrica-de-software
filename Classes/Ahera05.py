# 5 - Classe Pessoa: Crie uma super classe que modele uma Pessoa. 
# Esta classe deve possuir os seguintes atributos:
# Nome; Telefone; E-mail; Endereço;
# Métodos:
# negociar: deve printar uma mensagem de negociação;
# Subclasses:
# Defina as subclasses de Pessoa serão Física e Jurídica, estas devem conter 
# além dos atributos herdados de Pessoa seus atributos identificadores, ex: CPF, CNPJ.
# Além de herdar o método negociar() crie métodos específicos para as subclasses;
class Pessoa:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"{self.nome} está em negociação.")

    def mostrarDetalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco}")

# Subclasse Pessoa Física
class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def mostrarDetalhes(self):
        super().mostrarDetalhes()
        print(f"CPF: {self.cpf}")

    def pagarImpostoDeRenda(self):
        print(f"{self.nome} está pagando o Imposto de Renda como Pessoa Física.")

# Subclasse Pessoa Jurídica
class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj

    def mostrarDetalhes(self):
        super().mostrarDetalhes()
        print(f"CNPJ: {self.cnpj}")

    def emitirNotaFiscal(self):
        print(f"{self.nome} está emitindo uma Nota Fiscal.")

# Exemplo de uso das classes
pessoa_fisica = PessoaFisica("João Silva", "91234-5678", "joao.silva@email.com", "Rua das Flores, 123", "123.456.789-00")
pessoa_fisica.mostrarDetalhes()
pessoa_fisica.negociar()
pessoa_fisica.pagarImpostoDeRenda()

print("\n")

pessoa_juridica = PessoaJuridica("Empresa XYZ Ltda", "98765-4321", "contato@xyz.com", "Av. Central, 456", "12.345.678/0001-90")
pessoa_juridica.mostrarDetalhes()
pessoa_juridica.negociar()
pessoa_juridica.emitirNotaFiscal()


# explicação:
#   superclasse Pessoa que modela uma pessoa com atributos básicos, 
#   e duas subclasses PessoaFisica e PessoaJuridica que representam indivíduos 
#   e empresas, respectivamente. As subclasses herdam os atributos e métodos da 
#   superclasse e também possuem seus próprios atributos específicos, 
#   como CPF para PessoaFisica e CNPJ para PessoaJuridica. 
#   Além disso, cada subclasse tem um método específico.
#   Explicação do código:
# Superclasse Pessoa:

# Contém os atributos básicos comuns a todas as pessoas: nome, telefone, email, e endereco.
# O método negociar() imprime uma mensagem indicando que a pessoa está em negociação.
# O método mostrarDetalhes() exibe todas as informações da pessoa.
# Subclasse PessoaFisica:

# Herda os atributos e métodos da classe Pessoa.
# Adiciona o atributo cpf, específico para indivíduos.
# O método pagarImpostoDeRenda() simula o pagamento de imposto de renda.
# Subclasse PessoaJuridica:

# Herda os atributos e métodos da classe Pessoa.
# Adiciona o atributo cnpj, específico para empresas.
# O método emitirNotaFiscal() simula a emissão de uma nota fiscal.
# Testes:
# O código cria instâncias de PessoaFisica e PessoaJuridica, 
# chama os métodos herdados e os específicos para demonstrar a funcionalidade.