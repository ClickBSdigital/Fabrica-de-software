# 1 - Classe Pessoa: Crie uma classe que modele uma pessoa. Esta classe deve possuir os 
# seguintes atributos:
#  Nome
#  Idade
#  Endereço
#  A classe deve ter os seguintes métodos:
#  Mostrar nome;
#  Alterar a idade;
#  Imprimir endereço.
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrarNome(self):
        print(f"Nome: {self.nome}")

    def alterarIdade(self):
        alterar = int(input("Digite a sua idade: "))
        self.idade = alterar
        print("Idade alterada com sucesso!!!")
    
    def mostrarEndereco(self):
        print(f"Endereço: {self.endereco}")

def menu():
    print("#"*20)
    print("Digite sua opção: \n 1-Alterar idade \n 2-Mostrar endereço \n 3-Mostrar Nome")

nome = input("Digite seu nome: ")
idade =int(input("Digite sua idade: "))
endereco = input("Digite seu enderço: ")

pessoa1 = Pessoa(nome, idade, endereco)

while True:
    menu()
    opcao = int(input())
    if(opcao == 1):
        pessoa1.alterarIdade()
    elif(opcao == 2):
        pessoa1.mostrarEndereco()
    elif(opcao == 3):
        pessoa1.mostrarNome()