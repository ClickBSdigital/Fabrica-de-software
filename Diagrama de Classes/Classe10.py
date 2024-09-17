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
class NotaFiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produtos, icms, frete, ipi):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0  # Inicializado como 0, será calculado posteriormente

    def obter_numero(self):
        """Retorna o número da Nota Fiscal."""
        return self.numero

    def obter_data_emissao(self):
        """Retorna a data de emissão da Nota Fiscal."""
        return self.data

    def alterar_razao_social(self, nova_razao_social):
        """Altera a razão social da Nota Fiscal."""
        self.razao_social = nova_razao_social
        print(f"Razão Social alterada para: {self.razao_social}")

    def calcular_valor_total(self):
        """Calcula e armazena o valor total da Nota Fiscal."""
        self.valor_total = self.valor_produtos + self.frete + self.icms + self.ipi
        return self.valor_total

    def exibir_informacoes(self):
        """Exibe todas as informações da Nota Fiscal."""
        print(f"Nota Fiscal Nº: {self.numero}")
        print(f"Tipo: {self.tipo}")
        print(f"Série: {self.serie}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Razão Social: {self.razao_social}")
        print(f"Data: {self.data}")
        print(f"Valor dos Produtos: R${self.valor_produtos:.2f}")
        print(f"ICMS: R${self.icms:.2f}")
        print(f"Frete: R${self.frete:.2f}")
        print(f"IPI: R${self.ipi:.2f}")
        print(f"Valor Total: R${self.calcular_valor_total():.2f}")

# Exemplo de uso:
nota_fiscal = NotaFiscal(
    numero=62696270,
    tipo="Saída",
    serie=1,
    cnpj="22.987.696/0001-69",
    razao_social="Click BS Digital.",
    data="13/08/2024",
    valor_produtos=10000.0,
    icms=1800.0,
    frete=500.0,
    ipi=400.0
)

# Exibir informações da Nota Fiscal
nota_fiscal.exibir_informacoes()

# Alterar a razão social e exibir novamente as informações
nota_fiscal.alterar_razao_social("Nova Razão Social Ltda.")
nota_fiscal.exibir_informacoes()

#####################################

# Explicação da Classe NotaFiscal:
# Atributos:

# numero: Armazena o número da Nota Fiscal.
# tipo: Define o tipo da Nota Fiscal (Entrada ou Saída).
# serie: Define a série da Nota Fiscal (1, 2 ou 3).
# cnpj: Armazena o CNPJ da empresa.
# razao_social: Armazena a razão social da empresa.
# data: Armazena a data de emissão da Nota Fiscal.
# valor_produtos: Armazena o valor total dos produtos.
# icms: Armazena o valor do ICMS.
# frete: Armazena o valor do frete.
# ipi: Armazena o valor do IPI.
# valor_total: Armazena o valor total da Nota Fiscal, que será calculado.
# Métodos:

# obter_numero(): Retorna o número da Nota Fiscal.
# obter_data_emissao(): Retorna a data de emissão da Nota Fiscal.
# alterar_razao_social(nova_razao_social): Altera a razão social da Nota Fiscal.
# calcular_valor_total(): Calcula o valor total da Nota Fiscal, somando o valor dos produtos, frete e impostos (ICMS e IPI), e armazena o resultado em valor_total.
# Exibir Informações:

# O método exibir_informacoes() exibe todas as informações da Nota Fiscal, incluindo o valor total calculado.
# Exemplo de Uso:
# No exemplo, uma instância da NotaFiscal é criada com dados fictícios. Em seguida, são exibidas as informações da Nota Fiscal. Posteriormente, a razão social é alterada, e as informações são exibidas novamente.