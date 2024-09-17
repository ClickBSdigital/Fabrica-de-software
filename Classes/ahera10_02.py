# Classe Transporte: Você deve analisar a 
# hierarquia do transporte tipo Terrestre e da Classe 
# automóvel para criar as subclasses dos tipos de 
# transporte Aéreo e Aquático. Instancie 3 objetos 
# de cada classe e faça os testes nos atributos e 
# métodos específicos de cada subclasse;
#   Crie duas subclasses de Aquático e Aéreo, exemplo: 
#  Lancha e Navio;
#   AviaoMonomotor e AviaoComercial;
#   Verifique os atributos e métodos específicos de cada 
# subclasse

# Superclasse Transporte
class Transporte:
    def __init__(self, capacidade, velocidade_maxima):
        self.capacidade = capacidade
        self.velocidade_maxima = velocidade_maxima
    
    def detalhes_transporte(self):
        return f"Capacidade: {self.capacidade} pessoas, Velocidade Máxima: {self.velocidade_maxima} km/h"

# Subclasse Terrestre
class Terrestre(Transporte):
    def __init__(self, capacidade, velocidade_maxima, numero_rodas):
        super().__init__(capacidade, velocidade_maxima)
        self.numero_rodas = numero_rodas
    
    def detalhes_terrestre(self):
        return f"{self.detalhes_transporte()}, Quantidade de Rodas: {self.numero_rodas}"

# Subclasse Automovel (derivada de Terrestre)
class Automovel(Terrestre):
    def __init__(self, capacidade, velocidade_maxima, numero_rodas, cor, numero_portas, placa):
        super().__init__(capacidade, velocidade_maxima, numero_rodas)
        self.cor = cor
        self.numero_portas = numero_portas
        self.placa = placa
    
    def detalhes_automovel(self):
        return f"{self.detalhes_terrestre()}, Cor: {self.cor}, Número de Portas: {self.numero_portas}, Placa: {self.placa}"

# Subclasse Aquatica
class Aquatica(Transporte):
    def __init__(self, capacidade, velocidade_maxima, tipo_embarcacao):
        super().__init__(capacidade, velocidade_maxima)
        self.tipo_embarcacao = tipo_embarcacao
    
    def detalhes_aquatica(self):
        return f"{self.detalhes_transporte()}, Tipo de Embarcação: {self.tipo_embarcacao}"

# Subclasse Lancha (derivada de Aquatica)
class Lancha(Aquatica):
    def __init__(self, capacidade, velocidade_maxima, tipo_embarcacao, numero_motores):
        super().__init__(capacidade, velocidade_maxima, tipo_embarcacao)
        self.numero_motores = numero_motores
    
    def detalhes_lancha(self):
        return f"{self.detalhes_aquatica()}, Número de Motores: {self.numero_motores}"

# Subclasse Navio (derivada de Aquatica)
class Navio(Aquatica):
    def __init__(self, capacidade, velocidade_maxima, tipo_embarcacao, tonelagem):
        super().__init__(capacidade, velocidade_maxima, tipo_embarcacao)
        self.tonelagem = tonelagem
    
    def detalhes_navio(self):
        return f"{self.detalhes_aquatica()}, Tonelagem: {self.tonelagem} toneladas"

# Subclasse Aereo
class Aereo(Transporte):
    def __init__(self, capacidade, velocidade_maxima, tipo_aeronave):
        super().__init__(capacidade, velocidade_maxima)
        self.tipo_aeronave = tipo_aeronave
    
    def detalhes_aereo(self):
        return f"{self.detalhes_transporte()}, Tipo de Aeronave: {self.tipo_aeronave}"

# Subclasse AviaoMonomotor (derivada de Aereo)
class AviaoMonomotor(Aereo):
    def __init__(self, capacidade, velocidade_maxima, tipo_aeronave, autonomia):
        super().__init__(capacidade, velocidade_maxima, tipo_aeronave)
        self.autonomia = autonomia
    
    def detalhes_aviao_monomotor(self):
        return f"{self.detalhes_aereo()}, Autonomia: {self.autonomia} km"

# Subclasse AviaoComercial (derivada de Aereo)
class AviaoComercial(Aereo):
    def __init__(self, capacidade, velocidade_maxima, tipo_aeronave, companhia_aerea):
        super().__init__(capacidade, velocidade_maxima, tipo_aeronave)
        self.companhia_aerea = companhia_aerea
    
    def detalhes_aviao_comercial(self):
        return f"{self.detalhes_aereo()}, Companhia Aérea: {self.companhia_aerea}"

# Exemplos de uso:

# Instanciando objetos das subclasses Lancha e Navio
lancha = Lancha(10, 80, "Lancha Esportiva", 2)
navio = Navio(1000, 40, "Navio de Carga", 50000)

# Instanciando objetos das subclasses AviaoMonomotor e AviaoComercial
aviao_monomotor = AviaoMonomotor(2, 350, "Monomotor", 1500)
aviao_comercial = AviaoComercial(180, 900, "Comercial", "LATAM")

# Testando os métodos específicos de cada subclasse
print(lancha.detalhes_lancha())
print(navio.detalhes_navio())

print(aviao_monomotor.detalhes_aviao_monomotor())
print(aviao_comercial.detalhes_aviao_comercial())




# =========================================
# Explicação do Código
# Superclasse Transporte:

# É a base para todos os tipos de transportes. Contém atributos como capacidade e velocidade_maxima e um método detalhes_transporte que retorna uma string com esses detalhes.
# Subclasse Terrestre e Automovel:

# Terrestre adiciona o atributo numero_rodas, e Automovel, que herda de Terrestre, inclui atributos como cor, numero_portas, e placa.
# Subclasse Aquatica e suas Subclasses Lancha e Navio:

# Aquatica é específica para transportes aquáticos, com um atributo adicional tipo_embarcacao.
# Lancha herda de Aquatica e adiciona o atributo numero_motores.
# Navio herda de Aquatica e adiciona o atributo tonelagem.
# Subclasse Aereo e suas Subclasses AviaoMonomotor e AviaoComercial:

# Aereo é específica para transportes aéreos, com um atributo adicional tipo_aeronave.
# AviaoMonomotor herda de Aereo e adiciona o atributo autonomia.
# AviaoComercial herda de Aereo e adiciona o atributo companhia_aerea.
# Testando Atributos e Métodos
# O código cria instâncias das subclasses Lancha, Navio, AviaoMonomotor, e AviaoComercial, passando valores específicos para os atributos de cada um.
# Os métodos como detalhes_lancha, detalhes_navio, detalhes_aviao_monomotor, e detalhes_aviao_comercial são chamados para verificar os detalhes específicos de cada instância.