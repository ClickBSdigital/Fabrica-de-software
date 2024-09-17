# 3 - Classe Aluno: Crie uma classe que modele um aluno. Esta classe deve possuir os 
# seguintes atributos:
#  Nome;
#  RA;
#  Nota 1, nota 2, nota 3, nota 4;
#  A classe deve ter o seguintes método:
#  Mostrar_situacao: (APROVADO / EXAME / REPROVADO). Considere que, nesse caso, a média final 
# é calculada pela média aritmética simples de todas as notas e que o aluno é aprovado 
# somente se obtiver média maior ou igual a sete. Exame entre 5 e 6.9. Reprovado abaixo de 5
#  A situação será retornada a partir das notas obtidas pelo aluno.
class Aluno:
  # def __init__(self,nome,ra,n1,n2,n3,n4):
  #   self.__nome = nome
  #   self.ra = ra
  #   self.nota1 = n1
  #   self.nota2 = n2
  #   self.nota3 = n3
  #   self.nota4 = n4
  ## OU ##
  def __init__(self,nome,ra,*args):
    self.__nome = nome
    self.ra = ra
    self.notas = args
      
  def getNome(self):
    return self.__nome
  
  def setNome(self,novo_nome):
    self.__nome = novo_nome
    return True
  
  def situation(self):
    media = sum(self.notas) / len(self.notas)
    if media > 5:
      return f"{self.__nome} REPROVADO"
    else:
      return f"{self.__nome} APROVADO"
  
a1 = Aluno("JOÃO",1234,5,6,8,9)

print( a1.getNome())
a1.setNome("MARIA")
print( a1.getNome())
print( a1.situation())