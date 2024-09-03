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
    def __init__(self,marca,modelo,cor,ano,valor,nivel=5) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.nivel = nivel
        self.consumo = 8
        self.valor = valor
        self.ligado = False

    def ligar(self):
        self.ligado = True
        return f" {self.modelo} ligado....."

    def desligar(self):
        self.ligado = False
        return "CARRO DESLIGADO"

    def calculaImposto(self):
        imposto = self.valor * 0.025
        return imposto
    
    def abastecer(self,quant):
        self.nivel += quant
    
    def verificaNivel(self):
        return self.nivel
    
    def andar(self,km):
        litros = km / self.consumo
        self.nivel -= litros
        print("CONSUMO....",litros)


car1 = Carro("CHEVROLET","CELTA","PRATA",2012,79000)
imp = car1.calculaImposto()
print(imp)
car1.abastecer(30)
print(car1.verificaNivel())
car1.andar(65)
print(car1.verificaNivel())

# ================================:

# Vou explicar como o código funciona e o que ele faz:

# Classe Carro
# Atributos:

# marca: A marca do carro (ex: "CHEVROLET").
# modelo: O modelo do carro (ex: "CELTA").
# cor: A cor do carro (ex: "PRATA").
# ano: O ano de fabricação do carro (ex: 2012).
# valor: O valor do carro (ex: 79000).
# nivel: O nível de combustível (inicialmente 5).
# consumo: Consumo do carro em km por litro (fixo em 8 km/L).
# ligado: Um valor booleano para indicar se o carro está ligado ou desligado (inicialmente False).
# Métodos:

# ligar(): Liga o carro e retorna uma mensagem confirmando que o carro foi ligado.
# desligar(): Desliga o carro e retorna uma mensagem confirmando que o carro foi desligado.
# calculaImposto(): Calcula e retorna o imposto baseado em 2.5% do valor do carro.
# abastecer(quant): Aumenta o nível de combustível em uma quantidade especificada.
# verificaNivel(): Retorna o nível atual de combustível.
# andar(km): Simula o carro andando uma certa quantidade de quilômetros e diminui o nível de combustível de acordo com o consumo.
# Execução do Código
# No bloco de execução:

# Um carro (car1) é criado com os atributos fornecidos.
# O imposto sobre o valor do carro é calculado e impresso.
# O carro é abastecido com 30 unidades de combustível, e o nível de combustível atualizado é impresso.
# O carro percorre 65 km, o consumo de combustível é calculado e o nível de combustível restante é impresso.
# Saída Esperada
# python
# Copiar código
# 1975.0  # Imposto calculado
# 35      # Nível de combustível após abastecer
# CONSUMO.... 8.125  # Consumo ao andar 65 km
# 26.875   # Nível de combustível após o consumo
# Portanto, o carro começa com um nível de combustível de 5, é abastecido com mais 30 unidades, totalizando 35. Depois, ele anda 65 km, o que consome 8.125 litros de combustível, restando 26.875 no tanque.