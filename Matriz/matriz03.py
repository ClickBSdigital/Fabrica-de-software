# 1. Utilizando a estrutura de repetição While crie uma matriz 3 x 3 com os seguintes valores, 
# após reescreva o código utilizando for.
# [1,2,3]
# [4,5,6]
# [7,8,9]
#===============================
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
# # print(matriz)    

# # print(matriz[0])
# # print(matriz[1])
# # print(matriz[2])
    
# i = 0
# while i < len(matriz):
#     print(matriz[i])
#     i += 1
#===============================
l = 3
c = 3

matriz = []
i = 0
x = 0
while i < l:
    linha = []
    j = 0
    
    while j < c:
        x += 1
        linha.append(x)
        j += 1
    matriz.append(linha)
    i += 1

print('VALOR DE X ANTES DE ENTRAR NO WHILE ',x)
x = 0

print('VALOR DE X NA LINHA 51 ',x)
while x < len(matriz):
    print(matriz[x])
    x += 1