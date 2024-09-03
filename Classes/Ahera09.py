# 9 - Classe Compra: Crie uma super classe que modele uma Venda. 
# Esta classe deve possuir os seguintes atributos:
# Numero; Produto; Valor; Valor_total = 0;
# Método:
# calcular_valor_total(): deve somar ao valor_total o imposto de 17% do ICMS + o Frete de 5% 
# sobre o valor do produto;
# Subclasses:
# Defina as subclasses Avista e Parcelada, na classe de compra a vista deve ter 
# o atributo desconto e na classe Parcelada numero de parcelas.
# Em cada subclasse definir um método que retorna o preço com desconto ou o valor das parcelas.
# Superclasse Compra
class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0

    def calcular_valor_total(self):
        icms = 0.17 * self.valor  # 17% de ICMS
        frete = 0.05 * self.valor  # 5% de frete
        self.valor_total = self.valor + icms + frete
        return self.valor_total

    def mostrar_detalhes(self):
        print(f"Número da Compra: {self.numero}")
        print(f"Produto: {self.produto}")
        print(f"Valor do Produto: R$ {self.valor:.2f} reais")
        print(f"Valor Total (com impostos e frete): R$ {self.valor_total:.2f} reais")

# Subclasse Avista
class Avista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto

    def calcular_valor_total(self):
        valor_com_impostos = super().calcular_valor_total()
        valor_com_desconto = valor_com_impostos * (1 - self.desconto)
        self.valor_total = valor_com_desconto
        return self.valor_total

    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Desconto: {self.desconto * 100}%")
        print(f"Valor Final com Desconto: R$ {self.valor_total:.2f} reais")

# Subclasse Parcelada
class Parcelada(Compra):
    def __init__(self, numero, produto, valor, numero_parcelas):
        super().__init__(numero, produto, valor)
        self.numero_parcelas = numero_parcelas

    def calcular_valor_total(self):
        super().calcular_valor_total()
        return self.valor_total

    def calcular_valor_parcela(self):
        valor_parcela = self.valor_total / self.numero_parcelas
        return valor_parcela

    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Número de Parcelas: {self.numero_parcelas}")
        print(f"Valor de Cada Parcela: R$ {self.calcular_valor_parcela():.2f} reais")

# Exemplo de uso das classes
compra_avista = Avista(1, "Notebook", 1500.00, 0.10)  # 10% de desconto
compra_avista.calcular_valor_total()
compra_avista.mostrar_detalhes()

print("\n")

compra_parcelada = Parcelada(2, "Smartphone", 1200.00, 6)  # Parcelado em 6x
compra_parcelada.calcular_valor_total()
compra_parcelada.mostrar_detalhes()


# Explicação do código:
# Superclasse Compra:

# Contém os atributos comuns a todas as compras: numero, produto, valor, valor_total.
# O método calcular_valor_total() calcula o valor total da compra, somando 17% de ICMS e 5% de frete ao valor do produto.
# O método mostrar_detalhes() exibe os detalhes básicos da compra.
# Subclasse Avista:

# Herda os atributos e métodos da classe Compra.
# Adiciona o atributo desconto, que representa o desconto aplicado na compra à vista.
# O método calcular_valor_total() é reescrito para aplicar o desconto sobre o valor total.
# O método mostrar_detalhes() exibe os detalhes da compra à vista, incluindo o valor com desconto.
# Subclasse Parcelada:

# Herda os atributos e métodos da classe Compra.
# Adiciona o atributo numero_parcelas, que representa o número de parcelas em que a compra será dividida.
# O método calcular_valor_parcela() calcula o valor de cada parcela, dividindo o valor total pelo número de parcelas.
# O método mostrar_detalhes() exibe os detalhes da compra parcelada, incluindo o valor de cada parcela.
# Testes:
# No exemplo, são criadas instâncias das classes Avista e Parcelada, e os métodos específicos são chamados para demonstrar como as subclasses funcionam.