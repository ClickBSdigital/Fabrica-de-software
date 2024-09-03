# 10 - Classe Transporte: Crie uma super classe Transporte e suas respectivas subclasses, 
# sendo Terrestre e uma terceira subclasse de transporte Automóvel, 
# modele tipos de transportes de acordo com a imagem abaixo:
class Transporte:
  def __init__(self,capacidade, velocidade_maxima):
    self.capacidade = capacidade
    self.velocidade_maxima = velocidade_maxima
    
  def detalhes_transortes(self):
    return (f"Capacidade: {self.capacidade} pessoas, velocidade Máxima: {self.velocidade_maxima} km/h")
  
# subclasse Aquatica
class Aquatica(Transporte):
  def __init__(self, capacidade, velocidade_maxima,tipo_embarcacao):
    super().__init__(capacidade, velocidade_maxima)
    self.tipo_embarcação = tipo_embarcacao
    
  def detalhes_aquatica(self):
    return (f"{self.detalhes_transortes()}, Tipo de Embarcação {self.tipo_embarcação}")
   
#subclasse Terrestre
class Terrestre(Transporte):
  def __init__(self, capacidade, velocidade_maxima,numero_rodas):
    super().__init__(capacidade, velocidade_maxima)
    self.numero_rodas = numero_rodas
    
  def detalhes_terrestre(self):
    return(f"{self.detalhes_transortes()}, Quantidade de Rodas: {self.numero_rodas}")
  
class Automovel(Terrestre):
  def __init__(self, capacidade, velocidade_maxima, numero_rodas,cor,numero_portas,placa):
    super().__init__(capacidade, velocidade_maxima, numero_rodas)
    self.cor = cor
    self.numero_portas = numero_portas
    self.placa = placa
    
  def detalhes_automovel(self):
    return (f"{self.detalhes_terrestre()}, Cor: {self.cor}, Número de portas: {self.numero_portas}, Número da Placa é: {self.placa}")

#subclasse Aéreo
class Aereo(Transporte):
  def __init__(self, capacidade, velocidade_maxima, tipo_aeronave):
    super().__init__(capacidade, velocidade_maxima)
    self.tipo_aeronave = tipo_aeronave
        
  def detalhes_aeroa(self):
    return (f"{self.detalhes_transortes()}, Tipo de Aeronova: {self.tipo_aeronave}")
  
# SubClasse avião (derivadoo de Aero)
class Aviao(Aereo):
  def __init__(self, capacidade, velocidade_maxima, tipo_aeronave, modelo, companhia_aerea):
    super().__init__(capacidade, velocidade_maxima, tipo_aeronave)
    self.modelo = modelo
    self.companhia_aeronave = companhia_aerea
    
  def detalhes_aviao(self):
    return (f"{self.detalhes_aeroa()}, Modelo: {self.modelo}, Companhia Aérea: {self.companhia_aeronave}")

# Exemplos de uso:
aquatica = Aquatica(200, 30, "Iate")
automovel = Automovel(5, 220, "Asfalto", "Vermelho", 4, "XTR-4598")
aviao = Aviao(180, 900, "Comercial", "Boeing 737", "LATAM")

print(aquatica.detalhes_aquatica())
print(automovel.detalhes_automovel())
print(aviao.detalhes_aviao())


# =======================================================+

# O código que você escreveu define uma hierarquia de classes para diferentes tipos de transportes. Abaixo, vou explicar cada parte do código:

# 1. Superclasse Transporte
# python
# Copiar código
# class Transporte:
#     def __init__(self, capacidade, velocidade_maxima):
#         self.capacidade = capacidade
#         self.velocidade_maxima = velocidade_maxima
    
#     def detalhes_transortes(self):
#         return (f"Capacidade: {self.capacidade} pessoas, velocidade Máxima: {self.velocidade_maxima} km/h")
# Transporte é a superclasse. Ela contém dois atributos principais:
# capacidade: número de pessoas que o transporte pode levar.
# velocidade_maxima: velocidade máxima do transporte em km/h.
# A função detalhes_transortes retorna uma string com as informações sobre a capacidade e velocidade máxima do transporte.
# 2. Subclasse Aquatica
# python
# Copiar código
# class Aquatica(Transporte):
#     def __init__(self, capacidade, velocidade_maxima, tipo_embarcacao):
#         super().__init__(capacidade, velocidade_maxima)
#         self.tipo_embarcação = tipo_embarcacao
    
#     def detalhes_aquatica(self):
#         return (f"{self.detalhes_transortes()}, Tipo de Embarcação: {self.tipo_embarcação}")
# Aquatica é uma subclasse de Transporte, específica para transportes aquáticos.
# Ela adiciona o atributo tipo_embarcacao, que descreve o tipo de embarcação (por exemplo, iate, navio, etc.).
# A função detalhes_aquatica retorna as informações básicas de transporte junto com o tipo de embarcação.
# 3. Subclasse Terrestre
# python
# Copiar código
# class Terrestre(Transporte):
#     def __init__(self, capacidade, velocidade_maxima, numero_rodas):
#         super().__init__(capacidade, velocidade_maxima)
#         self.numero_rodas = numero_rodas
    
#     def detalhes_terrestre(self):
#         return(f"{self.detalhes_transortes()}, Quantidade de Rodas: {self.numero_rodas}")
# Terrestre é outra subclasse de Transporte, específica para transportes terrestres.
# Ela adiciona o atributo numero_rodas, que descreve o número de rodas do transporte.
# A função detalhes_terrestre retorna as informações básicas de transporte e o número de rodas.
# 4. Subclasse Automovel
# python
# Copiar código
# class Automovel(Terrestre):
#     def __init__(self, capacidade, velocidade_maxima, numero_rodas, cor, numero_portas, placa):
#         super().__init__(capacidade, velocidade_maxima, numero_rodas)
#         self.cor = cor
#         self.numero_portas = numero_portas
#         self.placa = placa
    
#     def detalhes_automovel(self):
#         return (f"{self.detalhes_terrestre()}, Cor: {self.cor}, Número de portas: {self.numero_portas}, Número da Placa é: {self.placa}")
# Automovel é uma subclasse de Terrestre, focada em veículos como carros.
# Ela adiciona três novos atributos:
# cor: a cor do automóvel.
# numero_portas: o número de portas do automóvel.
# placa: o número da placa do automóvel.
# A função detalhes_automovel retorna as informações de um transporte terrestre junto com a cor, número de portas e placa do automóvel.
# 5. Subclasse Aereo
# python
# Copiar código
# class Aereo(Transporte):
#     def __init__(self, capacidade, velocidade_maxima, tipo_aeronave):
#         super().__init__(capacidade, velocidade_maxima)
#         self.tipo_aeronave = tipo_aeronave
        
#     def detalhes_aeroa(self):
#         return (f"{self.detalhes_transortes()}, Tipo de Aeronave: {self.tipo_aeronave}")
# Aereo é uma subclasse de Transporte, focada em transportes aéreos.
# Ela adiciona o atributo tipo_aeronave, que descreve o tipo de aeronave (por exemplo, jato, helicóptero).
# A função detalhes_aeroa retorna as informações de um transporte aéreo junto com o tipo de aeronave.
# 6. Subclasse Aviao
# python
# Copiar código
# class Aviao(Aereo):
#     def __init__(self, capacidade, velocidade_maxima, tipo_aeronave, modelo, companhia_aerea):
#         super().__init__(capacidade, velocidade_maxima, tipo_aeronave)
#         self.modelo = modelo
#         self.companhia_aeronave = companhia_aerea
    
#     def detalhes_aviao(self):
#         return (f"{self.detalhes_aeroa()}, Modelo: {self.modelo}, Companhia Aérea: {self.companhia_aeronave}")
# Aviao é uma subclasse de Aereo, específica para aviões.
# Ela adiciona dois novos atributos:
# modelo: o modelo do avião (por exemplo, Boeing 737).
# companhia_aerea: a companhia aérea que opera o avião (por exemplo, LATAM).
# A função detalhes_aviao retorna as informações de um transporte aéreo junto com o modelo e a companhia aérea do avião.
# 7. Exemplos de Uso
# python
# Copiar código
# aquatica = Aquatica(200, 30, "Iate")
# automovel = Automovel(5, 220, "Asfalto", "Vermelho", 4, "XTR-4598")
# aviao = Aviao(180, 900, "Comercial", "Boeing 737", "LATAM")

# print(aquatica.detalhes_aquatica())
# print(automovel.detalhes_automovel())
# print(aviao.detalhes_aviao())
# Aqui, três instâncias diferentes são criadas, representando um transporte aquático (Aquatica), um automóvel (Automovel), e um avião (Aviao).
# Cada objeto é inicializado com atributos específicos e, em seguida, os detalhes de cada um são impressos usando os métodos correspondentes (detalhes_aquatica, detalhes_automovel, detalhes_aviao).