# 10 - Classe NF: Crie uma classe que modele uma Nota_Fiscal. 
# Esta classe deve possuir os 
# seguintes atributos:
#  Numero; Tipo (Entrada/Saída); Série (1,2 ou 3); CNPJ; 
# Razão Social; Data; Valor Produtos; ICMS; Frete; 
# IPI; Valor total;
#  A classe deve ter o seguintes métodos:
#  obterNumero();
#  obterDataEmissão();
#  alterarRazaoSocial();
#  calcularValorTotal() – somar valor do produto + frete 
# e impostos e armazenar na variável valor_total.

class Nota_Fiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produtos, icms, frete, ipi):
        self.numero = numero               # Número da Nota Fiscal
        self.tipo = tipo                   # Tipo: 'Entrada' ou 'Saída'
        self.serie = serie                 # Série: 1, 2 ou 3
        self.cnpj = cnpj                   # CNPJ da empresa emitente ou destinatária
        self.razao_social = razao_social   # Razão Social da empresa
        self.data = data                   # Data de emissão
        self.valor_produtos = valor_produtos # Valor total dos produtos
        self.icms = icms                   # Valor do ICMS (Imposto sobre Circulação de Mercadorias e Serviços)
        self.frete = frete                 # Valor do frete
        self.ipi = ipi                     # Valor do IPI (Imposto sobre Produtos Industrializados)
        self.valor_total = 0               # Valor total inicializado em 0

    # Método para obter o número da nota fiscal
    def obterNumero(self):
        return self.numero

    # Método para obter a data de emissão da nota fiscal
    def obterDataEmissao(self):
        return self.data

    # Método para alterar a razão social
    def alterarRazaoSocial(self, nova_razao_social):
        self.razao_social = nova_razao_social

    # Método para calcular o valor total da nota fiscal (produtos + frete + impostos)
    def calcularValorTotal(self):
        self.valor_total = self.valor_produtos + self.icms + self.frete + self.ipi
        return self.valor_total

# Exemplo de uso da classe Nota_Fiscal
nf = Nota_Fiscal(
    numero=1001,
    tipo="Saída",
    serie=1,
    cnpj="00.000.000/0001-00",
    razao_social="Empresa ABC Ltda",
    data="01/09/2024",
    valor_produtos=5000,
    icms=300,
    frete=150,
    ipi=200
)

# Exibindo informações da nota fiscal
print("Número da Nota Fiscal:", nf.obterNumero())
print("Data de Emissão:", nf.obterDataEmissao())

# Alterando a razão social
nf.alterarRazaoSocial("Empresa XYZ Ltda")
print("Razão Social Atualizada:", nf.razao_social)

# Calculando e exibindo o valor total da nota fiscal
valor_total = nf.calcularValorTotal()
print("Valor Total da Nota Fiscal:", valor_total)

# ========================================================:

# Explicação:
# Atributos:

# numero: Número da nota fiscal.
# tipo: Tipo da nota (Entrada ou Saída).
# serie: Série da nota (1, 2 ou 3).
# cnpj: CNPJ da empresa relacionada à nota fiscal.
# razao_social: Razão Social da empresa.
# data: Data de emissão da nota fiscal.
# valor_produtos: Valor total dos produtos listados na nota.
# icms: Valor do ICMS.
# frete: Valor do frete.
# ipi: Valor do IPI.
# valor_total: Valor total calculado (soma do valor dos produtos, frete e impostos).
# Métodos:

# obterNumero(): Retorna o número da nota fiscal.
# obterDataEmissao(): Retorna a data de emissão.
# alterarRazaoSocial(): Permite alterar a razão social da empresa associada à nota.
# calcularValorTotal(): Calcula e retorna o valor total somando os valores dos produtos, ICMS, frete e IPI.
# Exemplo de Saída:

# Número da Nota Fiscal: 1001
# Data de Emissão: 01/09/2024
# Razão Social Atualizada: Empresa XYZ Ltda
# Valor Total da Nota Fiscal: 5650
# Essa classe é bastante simples e fácil de expandir. É possível adicionar funcionalidades extras, como verificar a validade dos valores e formatar a saída de forma mais elegante.