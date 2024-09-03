# Crie um dicionário chamado produto que represente um produto com as seguintes 
# informações: nome, preço e quantidade em estoque. Imprima cada informação do produto 
# em uma linha separada.
# Criando o dicionário produto
produto = {
    "nome": "Caneta",
    "preço": 2.50,
    "quantidade_estoque": 100
}

# Imprimindo cada informação em uma linha separada
print(f"Nome: {produto['nome']}")
print(f"Preço: R${produto['preço']:.2f}")
print(f"Quantidade em estoque: {produto['quantidade_estoque']} unidades")

