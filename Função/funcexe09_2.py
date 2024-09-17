# EXERCÍCIOS FUNÇÕES
# 9 – Adicione na função calcularTempo() do sistema para
# estacionamento o valor dos impostos pago pelo cliente. 
#Considere o PIS: 0,33% , COFINS: 0,20% e ICMS: 17% 
#no valor e imprima o recibo do cliente 
#de acordo com a saída abaixo:
# ===========
# Tempo 4.0 horas
# PIS R$ 0.45
# CONINS R$ 0.27
# IMPOSTOS R$ 3.01
# TOTAL R$ 13.50

def soma_Imposto(taxaImposto, custo):
    novo_valor = custo + (custo * taxaImposto / 100)
    return novo_valor


taxaImposto01 = float(input("digite a taxa de inposto (em %): "))
produto = float(input("Digite o valor do custo de produto: "))

taxaImposto = soma_Imposto(taxaImposto01, produto)
print(f"O custo do item incluindo o imposto é: {produto:.2f}")

