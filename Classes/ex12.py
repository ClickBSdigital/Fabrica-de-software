def media(lista):
    med = sum(lista) / len(lista)
    return med

resultado = media([2,9,22,5,78,19,24])
numeros = [99,98,97,96,95,94]

x = media(numeros)

print(x)
print(f'{resultado:.2f}')

# +++++++++++=====================================

# O código fornecido implementa uma função media() que calcula a média dos valores de uma lista de números. Vou explicar o código em detalhes e mostrar o que ele faz:

# Explicação do Código
# Função media(lista):

# Entrada: Recebe uma lista de números como argumento.
# Processamento: A função usa sum(lista) para calcular a soma dos elementos da lista e divide pela quantidade de elementos len(lista) para obter a média.
# Saída: Retorna a média calculada.
# Exemplo de Uso:

# Primeiro, a função media() é chamada com uma lista [2, 9, 22, 5, 78, 19, 24]. O valor da média é armazenado na variável resultado.
# Depois, é chamada novamente com uma lista numeros = [99, 98, 97, 96, 95, 94], e o resultado é armazenado em x.
# Impressão dos Resultados:

# A média calculada de numeros (x) é impressa diretamente.
# A média calculada de resultado é impressa com duas casas decimais usando a formatação :.2f.
# Código:
# python
# Copiar código
# def media(lista):
#     med = sum(lista) / len(lista)
#     return med

# resultado = media([2, 9, 22, 5, 78, 19, 24])
# numeros = [99, 98, 97, 96, 95, 94]

# x = media(numeros)

# print(x)
# print(f'{resultado:.2f}')
# Saída Esperada:
# Para numeros = [99, 98, 97, 96, 95, 94]:

# A média será: 
# (
# 99
# +
# 98
# +
# 97
# +
# 96
# +
# 95
# +
# 94
# )
# /
# 6
# =
# 579
# /
# 6
# =
# 96.5
# (99+98+97+96+95+94)/6=579/6=96.5
# Então a saída será:
# Copiar código
# 96.5
# Para [2, 9, 22, 5, 78, 19, 24]:

# A média será: 
# (
# 2
# +
# 9
# +
# 22
# +
# 5
# +
# 78
# +
# 19
# +
# 24
# )
# /
# 7
# =
# 159
# /
# 7
# ≈
# 22.71
# (2+9+22+5+78+19+24)/7=159/7≈22.71
# A saída formatada será:
# Copiar código
# 22.71
# Saída Completa:
# Copiar código
# 96.5
# 22.71
# O código está correto e funcional. Ele calcula e imprime a média de duas listas de números, com uma das saídas formatada para mostrar duas casas decimais. Se precisares de mais ajuda ou adaptações, estou à disposição!