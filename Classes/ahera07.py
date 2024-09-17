# 7 - Classe Brinquedos: Andy Davis precisa classificar seus brinquedos por Subclasses, 
# sabemos que cada brinquedo tem atributos e métodos diferentes, 
# exemplo Buzz Lightyear voa e Woody laça. Defina principais atributos:
# Nome, Cor, Tamanho, Preço;
# Método:
# brincar(); - fazer um print simples, estou brincando com {nome do brinquedo}
# Subclasses:
# Crie 10 sub classes de brinquedos com seus respectivos atributos e métodos.
# Utilize o polimorfismo para reescrever o método herdado da super classe
# Superclasse Brinquedo
class Brinquedo:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"Estou brincando com {self.nome}.")

# Subclasse Buzz Lightyear
class BuzzLightyear(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, tipo_de_asa):
        super().__init__(nome, cor, tamanho, preco)
        self.tipo_de_asa = tipo_de_asa

    def brincar(self):
        print(f"Estou brincando com {self.nome}, que está voando com suas asas {self.tipo_de_asa}!")

    def voar(self):
        print(f"{self.nome} está voando alto!")

# Subclasse Woody
class Woody(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, chapéu):
        super().__init__(nome, cor, tamanho, preco)
        self.chapeu = chapéu

    def brincar(self):
        print(f"Estou brincando com {self.nome}, que está laçando!")

    def laco(self):
        print(f"{self.nome} está laçando com seu chapéu {self.chapeu}!")

# Subclasse Rex
class Rex(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, dentes):
        super().__init__(nome, cor, tamanho, preco)
        self.dentes = dentes

    def brincar(self):
        print(f"Estou brincando com {self.nome}, o dinossauro assustador!")

    def rugir(self):
        print(f"{self.nome} está rugindo com seus dentes {self.dentes} afiados!")

# Subclasse Sr. Cabeça de Batata
class SrCabeçaDeBatata(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, pecas_intercambiaveis):
        super().__init__(nome, cor, tamanho, preco)
        self.pecas_intercambiaveis = pecas_intercambiaveis

    def brincar(self):
        print(f"Estou brincando com {self.nome}, trocando suas peças!")

    def trocarPecas(self):
        print(f"Troquei as peças do {self.nome}!")

# Subclasse Slinky
class Slinky(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, comprimento):
        super().__init__(nome, cor, tamanho, preco)
        self.comprimento = comprimento

    def brincar(self):
        print(f"Estou brincando com {self.nome}, que está descendo as escadas!")

    def esticar(self):
        print(f"{self.nome} está se esticando até {self.comprimento} metros!")

# Subclasse Jessie
class Jessie(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, grito):
        super().__init__(nome, cor, tamanho, preco)
        self.grito = grito

    def brincar(self):
        print(f"Estou brincando com {self.nome}, que está gritando!")

    def gritar(self):
        print(f"{self.nome} grita: {self.grito}!")

# Subclasse Bo Peep
class BoPeep(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, cajado):
        super().__init__(nome, cor, tamanho, preco)
        self.cajado = cajado

    def brincar(self):
        print(f"Estou brincando com {self.nome}, cuidando das ovelhas!")

    def cuidarDasOvelhas(self):
        print(f"{self.nome} está cuidando das ovelhas com seu cajado {self.cajado}.")

# Subclasse Porquinho
class Porquinho(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, moedas):
        super().__init__(nome, cor, tamanho, preco)
        self.moedas = moedas

    def brincar(self):
        print(f"Estou brincando com {self.nome}, o cofrinho!")

    def guardarMoedas(self):
        print(f"Coloquei {self.moedas} moedas no {self.nome}!")

# Subclasse Zurg
class Zurg(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, raio):
        super().__init__(nome, cor, tamanho, preco)
        self.raio = raio

    def brincar(self):
        print(f"Estou brincando com {self.nome}, o vilão do espaço!")

    def dispararRaio(self):
        print(f"{self.nome} está disparando seu raio {self.raio}!")

# Subclasse Patinho
class Patinho(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, som):
        super().__init__(nome, cor, tamanho, preco)
        self.som = som

    def brincar(self):
        print(f"Estou brincando com {self.nome}, que faz {self.som}!")

    def apertar(self):
        print(f"{self.nome} faz {self.som} quando você o aperta!")

# Exemplo de uso das classes
buzz = BuzzLightyear("Buzz Lightyear", "Branco e Verde", "Médio", 50.00, "retráteis")
buzz.brincar()
buzz.voar()

print("\n")

woody = Woody("Woody", "Amarelo e Marrom", "Grande", 40.00, "de cowboy")
woody.brincar()
woody.laco()

print("\n")

rex = Rex("Rex", "Verde", "Grande", 30.00, "grandes")
rex.brincar()
rex.rugir()


# Explicação do código:
# Superclasse Brinquedo:

# Contém os atributos básicos comuns a todos os brinquedos: nome, cor, tamanho, preco.
# O método brincar() imprime uma mensagem simples indicando que a pessoa está brincando com o brinquedo.
# Subclasses Específicas:

# BuzzLightyear: Possui o atributo específico tipo_de_asa e o método voar(). O método brincar() foi reescrito para indicar que Buzz está voando.
# Woody: Tem o atributo específico chapeu e o método laco(). O método brincar() foi reescrito para indicar que Woody está laçando.
# Rex: Possui o atributo específico dentes e o método rugir(). O método brincar() foi reescrito para indicar que Rex é assustador.
# SrCabeçaDeBatata: Tem o atributo pecas_intercambiaveis e o método trocarPecas(). O método brincar() foi reescrito para indicar a troca de peças.
# Slinky: Possui o atributo comprimento e o método esticar(). O método brincar() foi reescrito para indicar que Slinky está descendo as escadas.
# Jessie: Possui o atributo grito e o método gritar(). O método brincar() foi reescrito para indicar que Jessie está gritando.
# BoPeep: Tem o atributo cajado e o método cuidarDasOvelhas(). O método brincar() foi reescrito para indicar que Bo Peep está cuidando das ovelhas.
# Porquinho: Tem o atributo moedas e o método guardarMoedas(). O método brincar() foi reescrito para indicar que ele é um cofrinho.
# Zurg: Possui o atributo raio e o método dispararRaio(). O método brincar() foi reescrito para indicar que Zurg é um vilão.
# Patinho: Tem o atributo som e o método apertar(). O método brincar() foi reescrito para indicar o som que o patinho faz.
# Testes:
# No exemplo, são criadas instâncias das classes BuzzLightyear, Woody, Rex, e outros brinquedos, e os métodos específicos são chamados para demonstrar a funcionalidade.