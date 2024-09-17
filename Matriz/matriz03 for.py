# 1. Utilizando a estrutura de repetição While crie uma matriz 3 x 3 com os seguintes valores, 
# após reescreva o código utilizando for.
# [1,2,3]
# [4,5,6]
# [7,8,9]
# l = int(input("DIGITE A QUANTIDADE DE LINHAS DA MATRIZ: "))
# c = int(input("DIGITE A QUANTIDADE DE COLUNAS DE MATRIZ: "))

# i = 0
# matriz = []
# while i < l:## criar lista
#     linha = []
#     j = 0
#     while j < c:##preencher as colunas
#         valor = int(input("DIGITE UM NÚMERO: "))
#         linha.append(valor)
#         j += 1
#     matriz.append(linha)
#     i += 1 
# print(matriz)    

# print(matriz[0])
# print(matriz[1])
# print(matriz[2])

# l = int(input("DIGITE A QUANTIDADE DE LINHAS DA MATRIZ: "))
# c = int(input("DIGITE A QUANTIDADE DE COLUNAS DA MATRIZ: "))

# matriz = []
# for i in range(c):
#     linha = []
#     for j in range(c):
#         num = int(input("DIGITE UM NUMERO: "))
#         linha.append(num)
#     matriz.append(linha)

# for item in matriz:
#     print(item)

#============================

l = int(input("DIGITE A QUANTIDADE DE LINHAS DA MATRIZ: "))
c = int(input("DIGITE A QUANTIDADE DE COLUNAS DE MATRIZ: "))

matriz =[]
for i in range(c):
    linha = []
    for j in range(l):
        linha.append(i * 3 + j + 1)
    matriz.append(linha)
print(matriz)

print(matriz[0])
print(matriz[1])
print(matriz[2])
print()
x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1


# estudos:

# matriz = []

# for i in range(3):
#     linha = []
#     for j in range(3):
#         linha.append(i * 3 + j + 1)  # Adiciona valores de 1 a 9 na matriz
#     matriz.append(linha)

# print(matriz)

# Inicialização: matriz é uma lista vazia.
# Loop externo (for i in range(3)): Este loop controla a criação das 3 linhas da matriz.
# Criação de uma linha vazia: linha é uma lista vazia que será preenchida com os valores.
# Loop interno (for j in range(3)): Este loop controla a adição de 3 elementos em cada linha.
# Adição de valores: linha.append(i * 3 + j + 1) adiciona o valor calculado à linha. O cálculo i * 3 + j + 1 garante que os valores serão de 1 a 9.
# Adição da linha à matriz: Após o loop interno, a linha completa é adicionada à matriz.
# Impressão da matriz: print(matriz) exibe a matriz resultante.
# Comparação
# Loop externo: No código com while, o loop externo é controlado pela variável i que é incrementada manualmente. No código com for, o loop externo é controlado automaticamente pelo range(3).
# Loop interno: No código com while, o loop interno é controlado pela variável j que é incrementada manualmente. No código com for, o loop interno é controlado automaticamente pelo range(3).
# Cálculo dos valores: Ambos os códigos usam a expressão i * 3 + j + 1 para calcular e adicionar os valores corretos à matriz.
# Legibilidade: O código com for é mais conciso e fácil de entender, pois elimina a necessidade de inicializar e incrementar manualmente as variáveis de controle dos loops.
# Ambos os métodos resultam na mesma matriz 3 x 3 com valores de 1 a 9, mas o uso de for é geralmente preferido por ser mais direto e menos propenso a erros.