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
# Classe Aluno
class Aluno:
    def __init__(self, nome, ra, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def calcular_media(self):
        """Calcula a média aritmética das notas."""
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

    def mostrar_situacao(self):
        """Mostra a situação do aluno com base na média das notas."""
        media = self.calcular_media()
        
        if media >= 7.0:
            situacao = "APROVADO"
        elif 5.0 <= media < 7.0:
            situacao = "EXAME"
        else:
            situacao = "REPROVADO"

        print(f"O aluno {self.nome} com RA {self.ra} tem média {media:.2f} e está {situacao}.")

# Exemplo de uso da classe
aluno1 = Aluno("João Silva", "123456", 6.0, 7.5, 8.0, 5.5)
aluno1.mostrar_situacao()

aluno2 = Aluno("Maria Oliveira", "654321", 4.0, 5.0, 4.5, 6.0)
aluno2.mostrar_situacao()


# # =========================================
# Explicação do Código:
# Atributos:

# nome: Nome do aluno.
# ra: Registro Acadêmico (RA) do aluno.
# nota1, nota2, nota3, nota4: Notas obtidas pelo aluno em quatro avaliações.
# Métodos:

# calcular_media(): Calcula a média aritmética simples das quatro notas do aluno.
# mostrar_situacao(): Determina a situação do aluno com base na média das notas:
# APROVADO: Média maior ou igual a 7.
# EXAME: Média entre 5 e 6.9.
# REPROVADO: Média abaixo de 5.
# Exibe a média e a situação do aluno.
# Exemplo de Uso:
# No exemplo, duas instâncias da classe Aluno são criadas, cada uma com suas notas. O método mostrar_situacao() é chamado para determinar e exibir a situação de cada aluno com base na média das notas.