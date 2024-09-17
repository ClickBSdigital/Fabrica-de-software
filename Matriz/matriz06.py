# 4. Crie um programa que leia uma lista de 9 posições e 
# converta em uma matriz de 3x3:
# ENTRADA: 
# numeros = [10,20,30,10,20,30,10,20,30]
# SAÍDA:
# [10,20,30]
# [10,20,30]
# [10,20,30]
numero = []
print("DIGITE 9 NÚMEROS PARA A LISTA: ")
i = 0
while i < 9:
    num = int(input(f"DIGITE O NÚMERO NA POSIÇÃO {i}: "))
    numero.append(num)
    i += 1

matriz = []
i = 0
while i < 3:
    linha = []
    j = 0
    while j < 3:
        linha.append(numero[i * 3 + j])
        j += 1
    matriz.append(linha)
    i += 1

print("MATRIS 3X3")
x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1

#     ESTUDOS:
# Vamos criar um programa que leia uma lista de 9 posições e a converta em uma matriz de 3x3 utilizando a estrutura de repetição while. Em seguida, explicarei o código.

# Código
# python
# Copiar código
# # Leitura da lista de 9 posições
# numeros = []
# print("Digite 9 números para a lista:")
# i = 0
# while i < 9:
#     num = int(input(f"Digite o número na posição {i}: "))
#     numeros.append(num)
#     i += 1

# # Conversão da lista em uma matriz 3x3
# matriz = []
# i = 0
# while i < 3:
#     linha = []
#     j = 0
#     while j < 3:
#         linha.append(numeros[i * 3 + j])
#         j += 1
#     matriz.append(linha)
#     i += 1

# # Impressão da matriz
# print("Matriz 3x3:")
# i = 0
# while i < 3:
#     print(matriz[i])
#     i += 1
# Explicação
# Leitura da lista de 9 posições:

# Inicializamos a lista numeros como uma lista vazia.
# Utilizamos um loop while para iterar 9 vezes (while i < 9), solicitando que o usuário insira um número em cada iteração.
# Cada número inserido pelo usuário é adicionado à lista numeros.
# Conversão da lista em uma matriz 3x3:

# Inicializamos a lista matriz como uma lista vazia.
# Utilizamos um loop while externo (while i < 3) para iterar 3 vezes, criando as linhas da matriz.
# Dentro do loop externo, inicializamos a lista linha como uma lista vazia para armazenar os elementos de cada linha.
# Utilizamos um loop while interno (while j < 3) para iterar 3 vezes, adicionando elementos da lista numeros à linha. O índice para acessar os elementos da lista numeros é calculado como i * 3 + j, o que garante que os elementos corretos sejam adicionados em cada linha.
# Após completar uma linha, adicionamos essa linha à matriz.
# Impressão da matriz:

# Utilizamos um loop while (while i < 3) para iterar sobre as linhas da matriz e imprimi-las.
# Exemplo de entrada e saída:
# Entrada:
# css
# Copiar código
# Digite 9 números para a lista:
# 10
# 20
# 30
# 10
# 20
# 30
# 10
# 20
# 30
# Saída:
# csharp
# Copiar código
# Matriz 3x3:
# [10, 20, 30]
# [10, 20, 30]
# [10, 20, 30]
# Este programa lê uma lista de 9 números fornecidos pelo usuário, converte essa lista em uma matriz 3x3 e imprime a matriz resultante, utilizando a estrutura de repetição while.

# explique isso e de exemplos: Utilizamos um loop while interno (while j < 3) para iterar 3 vezes, adicionando elementos da lista numeros à linha. O índice para acessar os elementos da lista numeros é calculado como i * 3 + j, o que garante que os elementos corretos sejam adicionados em cada linha.
# ChatGPT
# Claro! Vou explicar em detalhes a lógica por trás do uso do índice i * 3 + j dentro do loop while interno, e fornecer alguns exemplos.

# Explicação
# Estrutura da Lista e da Matriz
# Quando temos uma lista de 9 elementos, por exemplo:

# css
# Copiar código
# numeros = [10, 20, 30, 10, 20, 30, 10, 20, 30]
# Queremos converter essa lista em uma matriz 3x3:

# csharp
# Copiar código
# [
#  [10, 20, 30],
#  [10, 20, 30],
#  [10, 20, 30]
# ]
# Lógica do Índice i * 3 + j
# Para distribuir corretamente os elementos da lista numeros em uma matriz 3x3, usamos dois loops while aninhados. O loop externo (while i < 3) itera sobre as linhas da matriz, enquanto o loop interno (while j < 3) itera sobre as colunas de cada linha.

# i representa o índice da linha atual.
# j representa o índice da coluna atual dentro da linha.
# O índice para acessar os elementos da lista numeros é calculado como i * 3 + j. Este cálculo funciona da seguinte forma:

# Quando i = 0 (primeira linha):

# j = 0: índice na lista numeros é 0 * 3 + 0 = 0 (primeiro elemento da lista)
# j = 1: índice na lista numeros é 0 * 3 + 1 = 1 (segundo elemento da lista)
# j = 2: índice na lista numeros é 0 * 3 + 2 = 2 (terceiro elemento da lista)
# Quando i = 1 (segunda linha):

# j = 0: índice na lista numeros é 1 * 3 + 0 = 3 (quarto elemento da lista)
# j = 1: índice na lista numeros é 1 * 3 + 1 = 4 (quinto elemento da lista)
# j = 2: índice na lista numeros é 1 * 3 + 2 = 5 (sexto elemento da lista)
# Quando i = 2 (terceira linha):

# j = 0: índice na lista numeros é 2 * 3 + 0 = 6 (sétimo elemento da lista)
# j = 1: índice na lista numeros é 2 * 3 + 1 = 7 (oitavo elemento da lista)
# j = 2: índice na lista numeros é 2 * 3 + 2 = 8 (nono elemento da lista)
# Assim, todos os elementos da lista numeros são corretamente distribuídos em uma matriz 3x3.

# Exemplo Prático
# Vamos aplicar esta lógica em um exemplo prático com o código completo:

# python
# Copiar código
# # Leitura da lista de 9 posições
# numeros = []
# print("Digite 9 números para a lista:")
# i = 0
# while i < 9:
#     num = int(input(f"Digite o número na posição {i}: "))
#     numeros.append(num)
#     i += 1

# # Conversão da lista em uma matriz 3x3
# matriz = []
# i = 0
# while i < 3:
#     linha = []
#     j = 0
#     while j < 3:
#         linha.append(numeros[i * 3 + j])
#         j += 1
#     matriz.append(linha)
#     i += 1

# # Impressão da matriz
# print("Matriz 3x3:")
# i = 0
# while i < 3:
#     print(matriz[i])
#     i += 1
# Detalhamento do Processo
# Entrada de dados na lista:

# O usuário insere 9 números. Suponhamos que os números sejam: 10, 20, 30, 10, 20, 30, 10, 20, 30.
# Distribuição dos elementos da lista na matriz:

# Para i = 0, linha se torna [10, 20, 30]:

# j = 0: numeros[0 * 3 + 0] = numeros[0] = 10
# j = 1: numeros[0 * 3 + 1] = numeros[1] = 20
# j = 2: numeros[0 * 3 + 2] = numeros[2] = 30
# Para i = 1, linha se torna [10, 20, 30]:

# j = 0: numeros[1 * 3 + 0] = numeros[3] = 10
# j = 1: numeros[1 * 3 + 1] = numeros[4] = 20
# j = 2: numeros[1 * 3 + 2] = numeros[5] = 30
# Para i = 2, linha se torna [10, 20, 30]:

# j = 0: numeros[2 * 3 + 0] = numeros[6] = 10
# j = 1: numeros[2 * 3 + 1] = numeros[7] = 20
# j = 2: numeros[2 * 3 + 2] = numeros[8] = 30
# Impressão da matriz:

# A matriz é impressa linha por linha:
# csharp
# Copiar código
# [10, 20, 30]
# [10, 20, 30]
# [10, 20, 30]
# Essa lógica garante que cada elemento da lista numeros 
#     #seja posicionado corretamente na matriz 3x3.
#     Vou explicar em detalhes a lógica por trás do uso do índice i * 3 + j dentro do loop while interno, e fornecer alguns exemplos.

# Explicação
# Estrutura da Lista e da Matriz
# Quando temos uma lista de 9 elementos, por exemplo:

# css
# Copiar código
# numeros = [10, 20, 30, 10, 20, 30, 10, 20, 30]
# Queremos converter essa lista em uma matriz 3x3:

# csharp
# Copiar código
# [
#  [10, 20, 30],
#  [10, 20, 30],
#  [10, 20, 30]
# ]
# Lógica do Índice i * 3 + j
# Para distribuir corretamente os elementos da lista numeros em uma matriz 3x3, usamos dois loops while aninhados. O loop externo (while i < 3) itera sobre as linhas da matriz, enquanto o loop interno (while j < 3) itera sobre as colunas de cada linha.

# i representa o índice da linha atual.
# j representa o índice da coluna atual dentro da linha.
# O índice para acessar os elementos da lista numeros é calculado como i * 3 + j. Este cálculo funciona da seguinte forma:

# Quando i = 0 (primeira linha):

# j = 0: índice na lista numeros é 0 * 3 + 0 = 0 (primeiro elemento da lista)
# j = 1: índice na lista numeros é 0 * 3 + 1 = 1 (segundo elemento da lista)
# j = 2: índice na lista numeros é 0 * 3 + 2 = 2 (terceiro elemento da lista)
# Quando i = 1 (segunda linha):

# j = 0: índice na lista numeros é 1 * 3 + 0 = 3 (quarto elemento da lista)
# j = 1: índice na lista numeros é 1 * 3 + 1 = 4 (quinto elemento da lista)
# j = 2: índice na lista numeros é 1 * 3 + 2 = 5 (sexto elemento da lista)
# Quando i = 2 (terceira linha):

# j = 0: índice na lista numeros é 2 * 3 + 0 = 6 (sétimo elemento da lista)
# j = 1: índice na lista numeros é 2 * 3 + 1 = 7 (oitavo elemento da lista)
# j = 2: índice na lista numeros é 2 * 3 + 2 = 8 (nono elemento da lista)
# Assim, todos os elementos da lista numeros são corretamente distribuídos em uma matriz 3x3.

# Exemplo Prático
# Vamos aplicar esta lógica em um exemplo prático com o código completo:

# python
# Copiar código
# # Leitura da lista de 9 posições
# numeros = []
# print("Digite 9 números para a lista:")
# i = 0
# while i < 9:
#     num = int(input(f"Digite o número na posição {i}: "))
#     numeros.append(num)
#     i += 1

# # Conversão da lista em uma matriz 3x3
# matriz = []
# i = 0
# while i < 3:
#     linha = []
#     j = 0
#     while j < 3:
#         linha.append(numeros[i * 3 + j])
#         j += 1
#     matriz.append(linha)
#     i += 1

# # Impressão da matriz
# print("Matriz 3x3:")
# i = 0
# while i < 3:
#     print(matriz[i])
#     i += 1
# Detalhamento do Processo
# Entrada de dados na lista:

# O usuário insere 9 números. Suponhamos que os números sejam: 10, 20, 30, 10, 20, 30, 10, 20, 30.
# Distribuição dos elementos da lista na matriz:

# Para i = 0, linha se torna [10, 20, 30]:

# j = 0: numeros[0 * 3 + 0] = numeros[0] = 10
# j = 1: numeros[0 * 3 + 1] = numeros[1] = 20
# j = 2: numeros[0 * 3 + 2] = numeros[2] = 30
# Para i = 1, linha se torna [10, 20, 30]:

# j = 0: numeros[1 * 3 + 0] = numeros[3] = 10
# j = 1: numeros[1 * 3 + 1] = numeros[4] = 20
# j = 2: numeros[1 * 3 + 2] = numeros[5] = 30
# Para i = 2, linha se torna [10, 20, 30]:

# j = 0: numeros[2 * 3 + 0] = numeros[6] = 10
# j = 1: numeros[2 * 3 + 1] = numeros[7] = 20
# j = 2: numeros[2 * 3 + 2] = numeros[8] = 30
# Impressão da matriz:

# A matriz é impressa linha por linha:
# csharp
# Copiar código
# [10, 20, 30]
# [10, 20, 30]
# [10, 20, 30]
# Essa lógica garante que cada elemento da lista numeros seja posicionado corretamente na matriz 3x3.