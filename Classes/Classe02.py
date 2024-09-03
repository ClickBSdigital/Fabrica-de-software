# 2 - Classe Livro: Crie uma classe que modele um Livro. Esta classe deve possuir os 
# seguintes atributos:
#  Nome
#  Autor
#  Editora
#  Páginas
#  A classe deve ter o seguintes métodos:
#  Alterar_editora()
#  Listar_qtde_paginas()
# Classe Livro
class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self, nova_editora):
        """Altera a editora do livro para um novo valor."""
        self.editora = nova_editora
        print(f"A editora do livro '{self.nome}' foi alterada para '{self.editora}'.")

    def listar_qtde_paginas(self):
        """Lista a quantidade de páginas do livro."""
        print(f"O livro '{self.nome}' tem {self.paginas} páginas.")

# Exemplo de uso da classe
livro1 = Livro("1984", "George Orwell", "Companhia das Letras", 416)

# Usando os métodos da classe
livro1.alterar_editora("Editora Nova")  # Altera a editora do livro
livro1.listar_qtde_paginas()            # Exibe a quantidade de páginas do livro

# # ===================================
# Explicação do Código:
# Atributos:

# nome: Nome do livro.
# autor: Autor do livro.
# editora: Editora que publicou o livro.
# paginas: Número de páginas do livro.
# Métodos:

# alterar_editora(nova_editora): Altera a editora do livro para o valor fornecido e exibe uma mensagem confirmando a alteração.
# listar_qtde_paginas(): Exibe a quantidade de páginas do livro.
# Exemplo de Uso:
# No exemplo, uma instância da classe Livro é criada com um nome, autor, editora e número de páginas. Os métodos da classe permitem alterar a editora do livro e listar o número de páginas.