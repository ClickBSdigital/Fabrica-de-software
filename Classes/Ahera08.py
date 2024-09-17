# 8 - Classe Imóvel: Uma Imobiliária precisa de um sistema que controle o aluguel de seus Imóveis. 
# Para isto você deve definir em um módulo a super classe Imóvel com os seguintes atributos:
# InscricaoMunicipal; Valor_aluguel; IPTU;
# Método:
# obter_parcela_IPTU();
# Set_valor_aluguel();
# Subclasses:
# Defina as subclasses de Imóvel sendo: Casa, Condomínio; Apartamento; Terreno e Chácara;
# Defina os atributos específicos para cada sub classe, exemplo: piscina, sala_de_estar, 
# Quartos, churrasqueira, área m², elevador, área_de_lazer,   .

# Superclasse Imóvel
class Imovel:
    def __init__(self, inscricao_municipal, valor_aluguel, iptu):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu

    def obter_parcela_IPTU(self, parcelas):
        return self.iptu / parcelas

    def set_valor_aluguel(self, novo_valor):
        self.valor_aluguel = novo_valor
        print(f"O novo valor do aluguel é R$ {self.valor_aluguel} reais.")

    def mostrar_detalhes(self):
        print(f"Inscrição Municipal: {self.inscricao_municipal}")
        print(f"Valor do Aluguel: R$ {self.valor_aluguel} reais")
        print(f"IPTU: R$ {self.iptu} reais")

# Subclasse Casa
class Casa(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, quartos, piscina, churrasqueira):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.quartos = quartos
        self.piscina = piscina
        self.churrasqueira = churrasqueira

    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Quartos: {self.quartos}")
        print(f"Piscina: {'Sim' if self.piscina else 'Não'}")
        print(f"Churrasqueira: {'Sim' if self.churrasqueira else 'Não'}")

# Subclasse Condomínio
class Condominio(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area_lazer, seguranca):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area_lazer = area_lazer
        self.seguranca = seguranca

    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Área de Lazer: {self.area_lazer} m²")
        print(f"Segurança 24h: {'Sim' if self.seguranca else 'Não'}")

# Subclasse Apartamento
class Apartamento(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, andar, elevador, quartos):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.andar = andar
        self.elevador = elevador
        self.quartos = quartos

    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Andar: {self.andar}")
        print(f"Elevador: {'Sim' if self.elevador else 'Não'}")
        print(f"Quartos: {self.quartos}")

# Subclasse Terreno
class Terreno(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area = area

    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Área: {self.area} m²")

# Subclasse Chácara
class Chacara(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area, lago, arvores_frutiferas):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area = area
        self.lago = lago
        self.arvores_frutiferas = arvores_frutiferas

    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Área: {self.area} m²")
        print(f"Lago: {'Sim' if self.lago else 'Não'}")
        print(f"Árvores Frutíferas: {'Sim' if self.arvores_frutiferas else 'Não'}")

# Exemplo de uso das classes
casa1 = Casa(12345, 1500, 500, 4, True, True)
casa1.mostrar_detalhes()
print(f"Parcela do IPTU em 4x: R$ {casa1.obter_parcela_IPTU(4)} reais\n")

condominio1 = Condominio(54321, 3000, 800, 500, True)
condominio1.mostrar_detalhes()
condominio1.set_valor_aluguel(3200)
print("\n")

apartamento1 = Apartamento(67890, 2000, 600, 10, True, 3)
apartamento1.mostrar_detalhes()
print("\n")

terreno1 = Terreno(98765, 800, 200, 1000)
terreno1.mostrar_detalhes()
print("\n")

chacara1 = Chacara(13579, 2500, 700, 5000, True, True)
chacara1.mostrar_detalhes()