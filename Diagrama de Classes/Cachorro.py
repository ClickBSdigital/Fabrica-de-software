class Cachorro:
    ###SEMPRE COMEÇAR PELO MÉTODO CONSTRUTOR
    def __init__(self,nome=None,idade=None,peso=None,cor=None):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.cor = cor

    #MÉTODOS.... todos os métodos devem ter como parametro SELF 
    def latir(self):
        print(f" {self.nome}  AU AU ")
    
    def comer(self):
        print(f" {self.nome}  comeu ")

    def dormir(self,quant):
        print(f" {self.nome} dormiu ZZZ ZZZ ZZZ ZZZ {quant} horas de sono")

dog1 = Cachorro("Bilu",2,5,"Branco")

print(dog1)
print(dog1.nome)
print(dog1.cor)

dog2 = Cachorro("Belinha",10,2.5,"Caramelo")
print(dog2.nome)
print(dog2.cor)
dog2.latir()
dog1.comer()
dog1.dormir(2)


cachorrao = Cachorro()
print(cachorrao.nome)
print(cachorrao.idade)
print(cachorrao)
#imagine mil linhas para baixo
cachorrao.nome = "PITBULL ENRAIVADO"
cachorrao.cor = "PRETO"
cachorrao.idade = 7

print(cachorrao.nome)
print(cachorrao.cor)
print(cachorrao.idade)



