class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome
        self.duracao = duracao
    
    def play(self):
        print(f" {self.nome} começou.... ")


class FilmeAcao(Filme):
    def __init__(self, nome, duracao, produtora):
        super().__init__(nome, duracao)
        self.produtora = produtora

    def explodir(self,explosivo):
        print(f" ativar {explosivo}  3...2....1.....BOOOOMMMMM")


filme1 = Filme("TITANIC",300)
filme1.play()
        
filme2 = FilmeAcao("RAMBO",185,"PARAMOUNT")
filme2.play()

filme2.explodir("DINAMITE")
