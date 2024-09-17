# 9 - Classe Carro: Crie uma classe que modele um Carro. Esta classe deve possuir os seguintes 
# atributos:
#  Modelo, Marca, Cor, Ano, Valor, Nível (default 5) , Consumo
#  A classe deve ter o seguintes métodos:
#  ligar(); - para andar o carro deve estar ligado, use variável booleana.
#  abastecer(); - deve incrementar no nível do tanque de combustível
#  andar(); - recebe a distancia em km que o veículo andou
#  verificar_nível(); - o deve criar uma forma de calcular quantos litros de comb. foram gasto por km
#  calcular_imposto() - deve considerar o IPVA do carro em 2,5% do valor.
class Carro:
    def __init__(self, modelo, marca, cor, ano, valor, consumo, nivel=5):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo  # Consumo em km/l
        self.nivel = nivel  # Nível de combustível no tanque (em litros)
        self.ligado = False  # O carro começa desligado

    def ligar(self):
        """Liga o carro, permitindo que ele ande."""
        self.ligado = True
        print("O carro está ligado.")

    def desligar(self):
        """Desliga o carro."""
        self.ligado = False
        print("O carro está desligado.")

    def abastecer(self, litros):
        """Abastece o carro, incrementando o nível de combustível."""
        if litros > 0:
            self.nivel += litros
            print(f"Carro abastecido com {litros} litros. Nível atual: {self.nivel} litros.")
        else:
            print("Valor de abastecimento inválido.")

    def andar(self, distancia):
        """Faz o carro andar uma certa distância, consumindo combustível."""
        if not self.ligado:
            print("O carro precisa estar ligado para andar.")
            return

        consumo_necessario = distancia / self.consumo
        if consumo_necessario <= self.nivel:
            self.nivel -= consumo_necessario
            print(f"O carro andou {distancia} km e consumiu {consumo_necessario:.2f} litros de combustível.")
        else:
            print("Combustível insuficiente para essa distância.")

    def verificar_nivel(self):
        """Verifica o nível atual de combustível no tanque."""
        print(f"Nível atual de combustível: {self.nivel:.2f} litros.")

    def calcular_imposto(self):
        """Calcula o valor do IPVA, que é 2,5% do valor do carro."""
        ipva = self.valor * 0.025
        print(f"O IPVA do carro é: R${ipva:.2f}")

# Exemplo de uso:
meu_carro = Carro(modelo="Civic", marca="Honda", cor="Preto", ano=2020, valor=90000, consumo=15)

# Ligar o carro
meu_carro.ligar()

# Abastecer o carro
meu_carro.abastecer(20)

# Andar com o carro
meu_carro.andar(100)

# Verificar o nível de combustível
meu_carro.verificar_nivel()

# Calcular o imposto do carro
meu_carro.calcular_imposto()

# Desligar o carro
meu_carro.desligar()

##################################

# Explicação da Classe Carro:
# Atributos:

# modelo, marca, cor, ano, valor: Armazenam informações básicas sobre o carro.
# consumo: Armazena o consumo do carro em km/l (quilômetros por litro).
# nivel: Armazena o nível atual do tanque de combustível, com valor padrão de 5 litros.
# ligado: Um atributo booleano que indica se o carro está ligado ou desligado.
# Métodos:

# ligar(): Liga o carro, permitindo que ele possa andar.
# desligar(): Desliga o carro.
# abastecer(litros): Incrementa o nível do tanque de combustível com a quantidade especificada de litros.
# andar(distancia): Calcula o consumo de combustível necessário para a distância percorrida e ajusta o nível do tanque. O carro precisa estar ligado para andar.
# verificar_nivel(): Exibe o nível atual do tanque de combustível.
# calcular_imposto(): Calcula o valor do IPVA, que é 2,5% do valor do carro.
# Como Funciona:
# Ligar o Carro:

# O carro precisa estar ligado para realizar certas operações, como andar.
# Abastecer:

# O método abastecer permite adicionar combustível ao tanque.
# Andar com o Carro:

# O método andar verifica se o carro está ligado e calcula se há combustível suficiente para percorrer a distância. Caso contrário, o carro não pode andar.
# Calcular Imposto:

# O método calcular_imposto calcula o valor do IPVA baseado em 2,5% do valor do carro.
# Exemplo de Uso:
# No exemplo fornecido, criamos uma instância do carro "Civic", ligamos o carro, verificamos o nível de combustível, abastecemos, dirigimos o carro por 100 km, calculamos o imposto e, finalmente, desligamos o carro.