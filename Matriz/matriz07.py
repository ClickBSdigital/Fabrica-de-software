# 5 - Crie um programa que inicialize uma matriz
# 8 x 8 no formato de uma rifa, preenchida com
# números 1. Em seguida solicite ao usuário a
# entrada da linha e coluna que deseja marcar
# um X e imprima novamente a matriz com a
# alteração realizada. Neste exercício estamos
# simulando a escolha de uma posição em uma
# rifa, caso necessário, você pode alimentar a
# rifa com números em sequência.

l = int(input("DIGITE A QUANTIDADE DE LINHAS DA MATRIZ: "))
c = int(input("DIGITE A QUANTIDADE DE COLUNAS DE MATRIZ: "))

i = 0
matriz = []
while i < l:## criar lista
    linha = []
    j = 0
    while j < c:##preencher as colunas
        linha.append(1)
        j += 1
    matriz.append(linha)
    i += 1 

def imprime_matriz(matriz):
    x = 0
    while x < len(matriz):
        print(matriz[x])
        x += 1

print("MATRIZ INICIAL:")
imprime_matriz(matriz)

linha_usuario = int(input("DIGITE UM NÚMERO DE LINHA ENTRE 0/7: "))
coluna_usuario = int(input("DIGITE UM NÚMERO NA COLUNA ENTRE 0/7: "))
matriz[linha_usuario][coluna_usuario] = 'X'


print("MATRIS 3X3")
x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1

#     ESTUDOS:

#     Vamos criar um programa que inicialize uma matriz 8x8 com números 1, permita ao usuário marcar uma posição com "X" e depois imprima a matriz com a alteração. Utilizaremos a estrutura de repetição while e, em seguida, explicarei o código.

# Código
# python
# Copiar código
# # Inicialização da matriz 8x8 com números 1
# matriz = []
# i = 0
# while i < 8:
#     linha = []
#     j = 0
#     while j < 8:
#         linha.append(1)
#         j += 1
#     matriz.append(linha)
#     i += 1

# # Função para imprimir a matriz
# def imprime_matriz(matriz):
#     i = 0
#     while i < len(matriz):
#         print(matriz[i])
#         i += 1

# # Impressão da matriz inicial
# print("Matriz inicial:")
# imprime_matriz(matriz)

# # Solicitação da entrada do usuário para marcar um "X"
# linha_usuario = int(input("Digite o número da linha (0 a 7) para marcar um 'X': "))
# coluna_usuario = int(input("Digite o número da coluna (0 a 7) para marcar um 'X': "))

# # Marcação do "X" na posição escolhida pelo usuário
# matriz[linha_usuario][coluna_usuario] = 'X'

# # Impressão da matriz alterada
# print("Matriz com a alteração:")
# imprime_matriz(matriz)
# Explicação
# Inicialização da matriz 8x8 com números 1:

# Criamos uma lista vazia matriz que irá armazenar as linhas.
# Utilizamos um loop while externo (while i < 8) para iterar sobre as linhas.
# Dentro do loop externo, criamos uma lista linha vazia para armazenar os elementos da linha.
# Utilizamos um loop while interno (while j < 8) para iterar sobre as colunas, adicionando o número 1 a cada posição da linha.
# Após completar uma linha, adicionamos essa linha à matriz.
# Incrementamos os contadores i e j em cada iteração para garantir que os loops percorram todas as linhas e colunas.
# Função para imprimir a matriz:

# Criamos uma função imprime_matriz que recebe uma matriz como argumento e imprime cada uma das suas linhas.
# Utilizamos um loop while dentro da função para percorrer todas as linhas da matriz e imprimi-las.
# Impressão da matriz inicial:

# Chamamos a função imprime_matriz para imprimir a matriz inicial preenchida com números 1.
# Solicitação da entrada do usuário:

# Pedimos ao usuário para digitar o número da linha e da coluna onde deseja marcar um "X". Os valores devem estar no intervalo de 0 a 7.
# Marcação do "X" na posição escolhida pelo usuário:

# Usamos os índices fornecidos pelo usuário para acessar a posição específica na matriz e alterar o valor para "X".
# Impressão da matriz alterada:

# Chamamos novamente a função imprime_matriz para imprimir a matriz com a alteração feita pelo usuário.
# Exemplo de entrada e saída:
# Entrada:
# java
# Copiar código
# Digite o número da linha (0 a 7) para marcar um 'X': 2
# Digite o número da coluna (0 a 7) para marcar um 'X': 3
# Saída:
# less
# Copiar código
# Matriz inicial:
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]

# Matriz com a alteração:
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 'X', 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]
# Este programa inicializa uma matriz 8x8 com números 1, permite ao usuário marcar uma posição com "X", e imprime a matriz antes e depois da alteração, utilizando a estrutura de repetição while.