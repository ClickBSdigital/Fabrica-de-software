# Modifique o dicionário produto do exercício anterior para aumentar a quantidade em 
# estoque em 10 unidades. Em seguida, imprima a quantidade atualizada.
# Aumentando a quantidade em estoque em 10 unidades
# Dicionário produto original
produto = {
    "nome": "Caneta",
    "preço": 2.50,
    "quantidade_estoque": 100
}

# Aumentando a quantidade em estoque em 10 unidades
produto["quantidade_estoque"] += 10

# Imprimindo a quantidade atualizada em estoque
print(f"Quantidade atualizada em estoque: {produto['quantidade_estoque']} unidades")

# Explicação:
# O dicionário produto inicialmente tem 100 unidades em estoque.
# Utilizamos produto["quantidade_estoque"] += 10 para adicionar 10 unidades ao valor atual da chave quantidade_estoque.
# Finalmente, imprimimos a nova quantidade em estoque, que será 110 unidades.