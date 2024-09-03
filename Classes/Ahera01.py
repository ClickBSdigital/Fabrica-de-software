# 1 - Classe Filme: Crie uma super classe que modele um Filme. 
# Esta classe deve possuir os seguintes atributos:
# Nome;
# Duração;
# Método:
# Play(): deve exibir que foi dado play no filme;
# Subclasses:
# Defina as subclasses de Filme, exemplo Ação, Drama e Suspense. 
# Após a criação das subclasses você deve criar novos métodos específicos a cada subclasse, 
# ex: explodir() em Ação.
class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print(f"{self.nome} Começouuuu...............")

class FilmeAcao(Filme):
    def __init__(self, nome, duracao, produtora):
        super().__init__(nome, duracao)
        self.produtora = produtora

    def explodir(self,explosivo):
        print(f"Ativar.... {explosivo}  3.........2......1.........kabouououummmmmmmmmm")

class FilmeDrama(Filme):
    def __init__(self, nome, romance):
        super().__init__(nome, duracao)
        self.romance = romance

    def romance(self,beijusss):
        print(f"ENCONTRO..... {beijusss} deu casamento..........;)")

filme1 = Filme("TITANIC",300)
filme1.play()

filme2 = FilmeAcao("RAMBO",185,"PARAMOUNT")
filme2.play()

filme2.explodir("Dinamite //ATIVADA//")

filme3 = FilmeDrama("")