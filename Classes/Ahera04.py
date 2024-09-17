# 4 - Classe Passagem: Crie uma super classe que modele uma Passagem. 
# Esta classe deve possuir os seguintes atributos:
# Preco;
# Assento;
# Método:
# alterar_preco() e escolher_assento();
# Subclasses:
# Defina a subclasse PassagemBus e PassagemAviao com os seguintes 
# atributos: portaodeembarque e checkin para classe PassagemAviao, 
# placa e leito par PassagemBus;
# Crie um novo método específico para cada subclasse. Ex: decolar() e abastecer()

# ===========================================
# class Passagem:
#   def __init__(self,preco,assento,):
#     self.preco = preco
#     self.assento = assento
        
#   def alterar_preco(self,novo_preco):
#     self.novo_peco = novo_preco
    
#   def escolher_assento(self,escolher_assento):
#     self.escolher_assento = escolher_assento
#     return self.assento
  
# class passagemBus(Passagem):
#   def __init__(self, preco, assento, placa, modelo, leito, consumo, nivel=5):
#     super().__init__(preco, assento)
#     self.placa = placa
#     self.modelo = modelo
#     self.leito = leito
#     self.consumo = consumo
#     self.ligado = False
#     self.nivel = nivel
    
#   def ligar(self):
#         self.ligado = True
#         return f" {self.modelo} ligado Pronto para partida....."
  
#   def abastecer(self,quant):
#         self.nivel += quant
    
#   def verificaNivel(self):
#         return self.nivel
    
#   def andar(self,km):
#       litros = km / self.consumo
#       self.nivel -= litros
#       print("CONSUMO....",litros)
   
# class passagemAviao(Passagem):
#   def __init__(self, preco, assento, portaodeembarque, checkin):
#      super().__init__(preco, assento)  
#      self.portaodeembarque = portaodeembarque
#      self.checkin = checkin
     
class Passagem:
    def __init__(self, numero, data, origem, destino):
        self.numero = numero
        self.data = data
        self.origem = origem
        self.destino = destino

    def mostrarDetalhes(self):
        print(f"Número da Passagem: {self.numero}")
        print(f"Data: {self.data}")
        print(f"Origem: {self.origem}")
        print(f"Destino: {self.destino}")

# Subclasse para passagens de avião
class PassagemAviao(Passagem):
    def __init__(self, numero, data, origem, destino, portaoDeEmbarque, checkin):
        super().__init__(numero, data, origem, destino)
        self.portaoDeEmbarque = portaoDeEmbarque
        self.checkin = checkin

    def mostrarDetalhes(self):
        super().mostrarDetalhes()
        print(f"Portão de Embarque: {self.portaoDeEmbarque}")
        print(f"Check-in: {self.checkin}")

    def decolar(self):
        print(f"O voo com número de passagem {self.numero} está decolando do portão {self.portaoDeEmbarque}.")

# Subclasse para passagens de ônibus
class PassagemBus(Passagem):
    def __init__(self, numero, data, origem, destino, placa, leito):
        super().__init__(numero, data, origem, destino)
        self.placa = placa
        self.leito = leito

    def mostrarDetalhes(self):
        super().mostrarDetalhes()
        print(f"Placa do Ônibus: {self.placa}")
        print(f"Tipo de Leito: {self.leito}")

    def abastecer(self):
        print(f"O ônibus com placa {self.placa} está sendo abastecido para a viagem de {self.origem} para {self.destino}.")

# Exemplo de uso das classes
passagem_aviao = PassagemAviao(12345, "2024-09-10", "Fortalesa ", "Poços de Caldas", "A17", "Online")
passagem_aviao.mostrarDetalhes()
passagem_aviao.decolar()

print("\n")

passagem_bus = PassagemBus(67890, "2024-09-11", "São Paulo", "Rio de Janeiro", "ABC-1234", "Leito Executivo")
passagem_bus.mostrarDetalhes()
passagem_bus.abastecer()


# Explicação do código:
# Classe Base (Passagem):

# Contém os atributos comuns a todas as passagens (numero, data, origem, destino).
# O método mostrarDetalhes() exibe os detalhes básicos da passagem.
# Subclasse PassagemAviao:

# Herda de Passagem e adiciona os atributos específicos portaoDeEmbarque e checkin.
# O método decolar() é exclusivo desta classe e simula a decolagem.
# Subclasse PassagemBus:

# Herda de Passagem e adiciona os atributos específicos placa e leito.
# O método abastecer() é exclusivo desta classe e simula o abastecimento do ônibus.
# Testes:
# Ao executar o código, são criadas instâncias das classes PassagemAviao e PassagemBus,
# e seus métodos específicos são chamados para demonstrar as funcionalidades.