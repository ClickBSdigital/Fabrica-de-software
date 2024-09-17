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
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data_emissao, valor_produtos, icms, frete, ipi):
        self.numero = numero               # Número da nota fiscal
        self.tipo = tipo                   # Tipo: 'Entrada' ou 'Saída'
        self.serie = serie                 # Série: 1, 2 ou 3
        self.cnpj = cnpj                   # CNPJ do cliente/fornecedor
        self.razao_social = razao_social   # Razão Social do cliente/fornecedor
        self.data_emissao = data_emissao   # Data de emissão da nota fiscal
        self.valor_produtos = valor_produtos # Valor dos produtos
        self.icms = icms                   # Valor do ICMS
        self.frete = frete                 # Valor do frete
        self.ipi = ipi                     # Valor do IPI
        self.valor_total = 0               # Valor total inicializado em 0

    # Método para obter o número da nota fiscal
    def obterNumero(self):
        return self.numero

    # Método para obter a data de emissão da nota fiscal
    def obterDataEmissao(self):
        return self.data_emissao

    # Método para alterar a razão social
    def alterarRazaoSocial(self, nova_razao_social):
        self.razao_social = nova_razao_social

    # Método para calcular o valor total da nota fiscal
    def calcularValorTotal(self):
        self.valor_total = self.valor_produtos + self.frete + self.icms + self.ipi
        return self.valor_total

# Exemplo de utilização da classe Nota_Fiscal

# Criando uma instância de Nota_Fiscal
nf1 = Nota_Fiscal(
    numero=1234,
    tipo="Saída",
    serie=1,
    cnpj="12.345.678/0001-99",
    razao_social="Empresa Exemplo Ltda",
    data_emissao="01/09/2024",
    valor_produtos=10000,
    icms=500,
    frete=200,
    ipi=300
)

# Obtendo o número da nota fiscal
print("Número da Nota Fiscal:", nf1.obterNumero())

# Obtendo a data de emissão
print("Data de Emissão:", nf1.obterDataEmissao())

# Alterando a razão social
nf1.alterarRazaoSocial("Nova Razão Social Ltda")
print("Razão Social Atualizada:", nf1.razao_social)

# Calculando o valor total da nota fiscal
valor_total = nf1.calcularValorTotal()
print("Valor Total da Nota Fiscal:", valor_total)


# ===============================================>

# Explicação:
# Atributos:

# numero: O número da nota fiscal.
# tipo: Indica se a nota é de "Entrada" ou "Saída".
# serie: Série da nota fiscal (1, 2 ou 3).
# cnpj: O CNPJ do cliente ou fornecedor.
# razao_social: A razão social da empresa envolvida.
# data_emissao: A data em que a nota fiscal foi emitida.
# valor_produtos: O valor total dos produtos incluídos na nota fiscal.
# icms: Valor do ICMS (Imposto sobre Circulação de Mercadorias e Serviços).
# frete: Valor do frete.
# ipi: Valor do IPI (Imposto sobre Produtos Industrializados).
# valor_total: O valor total da nota fiscal, calculado somando o valor dos produtos, impostos e frete.
# Métodos:

# obterNumero(): Retorna o número da nota fiscal.
# obterDataEmissao(): Retorna a data de emissão da nota fiscal.
# alterarRazaoSocial(): Permite alterar a razão social da empresa.
# calcularValorTotal(): Calcula e retorna o valor total da nota, somando o valor dos produtos, frete, ICMS e IPI.
# Exemplo de Saída:
# .....
# Número da Nota Fiscal: 1234
# Data de Emissão: 01/09/2024
# Razão Social Atualizada: Nova Razão Social Ltda
# Valor Total da Nota Fiscal: 11000
# Essa classe oferece a estrutura básica para uma Nota Fiscal. Pode ser facilmente expandida conforme necessário, adicionando mais atributos ou métodos, dependendo das especificidades do sistema fiscal em que será utilizada.