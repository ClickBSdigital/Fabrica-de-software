# 3. Faça um programa que leia uma matriz de 3 x 3 elementos, multiplique cada elemento 
# de cada linha por 5 e armazene a multiplicação em uma nova matriz. Exemplo:

# matriz = [[1,2,3],[4,5,6],[7,8,9]]
# nova_matriz = []

# print(matriz[0])
# print(matriz[1])
# print(matriz[2])

# print(nova_matriz[0])
# print(nova_matriz[1])
# print(nova_matriz[2])

# ENTRADA:
# [1,2,3]
# [4,5,6]
# [7,8,9]

# SAÍDA:
# [5,10,15]
# [20,25,30]
# [35,40,45]

matriz = []
print("DIGITE OS ELEMENTOS DA MATRIZ 3X3:")

i = 0
while i < 3:
    linha = []
    j = 0
    while j < 3:
        num = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(num)
        j += 1
    matriz.append(linha)
    i += 1
    
nova_matriz = []

i = 0
while i < 3:
    nova_linha = []
    j = 0
    while j < 3:
        valor_novo = matriz[i][j] * 5
        nova_linha.append(valor_novo)
        j += 1
    nova_matriz.append(nova_linha)
    i += 1

print("MATRIZ ORIGINAL")
print()

x = 0
while x < 3:
    print(matriz[x])
    x += 1
print()
print("NOVA MATRIZ MULTIPLICADA POR 5:")
print()

x = 0
while x < 3:
    print(nova_matriz[x])
    x += 1