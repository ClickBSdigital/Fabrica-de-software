# Escreva um programa com uma função chamada
# somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas
# expressa em porcentagem e custo, que é o custo de um item
# antes do imposto. A função “altera” o valor de custo para
# incluir o imposto sobre vendas. Por fim deve retornar o novo
# valor para o usuário considerando o percentual do imposto.
def soma_Imposto(taxaImposto, custo):
    novo_valor = custo + (custo * taxaImposto / 100)
    return novo_valor


taxaImposto01 = float(input("digite a taxa de inposto (em %): "))
produto = float(input("Digite o valor do custo de produto: "))

taxaImposto = soma_Imposto(taxaImposto01, produto)
print(f"O custo do item incluindo o imposto é: {produto:.2f}")




# def somaImposto(taxaImposto, custo):
    
#     novo_valor = custo + (custo * taxaImposto / 100)
#     return novo_valor

# # Exemplo de uso da função
# taxa = float(input("Informe a taxa de imposto (em %): "))
# custo_inicial = float(input("Informe o custo do item antes do imposto: "))

# custo_final = somaImposto(taxa, custo_inicial)
# print(f"O custo do item incluindo o imposto é: {custo_final:.2f}")


    # Calcula o novo custo de um item incluindo o imposto sobre vendas.

    # Parâmetros:
    # taxaImposto (float): A quantia de imposto sobre vendas expressa em porcentagem.
    # custo (float): O custo de um item antes do imposto.

    # Retorna:
    # float: O novo valor do item incluindo o imposto.