# 2 - Classe Livro: Crie uma classe que modele um Livro. Esta classe deve possuir os 
# seguintes atributos:
#  Nome
#  Autor
#  Editora
#  Páginas
#  A classe deve ter o seguintes métodos:
#  Alterar_editora()
#  Listar_qtde_paginas()
class Livro:
  def __init__(self,nome,autor,edit,pags):
    self.nome = nome
    self.author = autor
    self.editora = edit
    self.paginas = pags
    
  def listaQtdePags(self):
    print(self.paginas)
    
  def alterarEditora(self,novaEditora):
    self.editora = novaEditora
    
livro1 = Livro("MENÓRIAS POSTUMAS DE UM FILÓSOFO DE BUTECO","ALMEIDA","THIAGO")
livro2 = Livro("BIOGRAFIA DE UM GRANDÍSSIMO HOMEM","ELIANDRO","VIDA",798)
livro3 = Livro("PERIFÉCIAS DA GRATA","GRAZI CARASINI","GRATILUZ",588)

livro2.listaQtdePags   