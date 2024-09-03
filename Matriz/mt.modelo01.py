l = int(input("DIGITE A QUANTIDADE DE LINHAS DA MATRIZ: "))
c = int(input("DIGITE A QUANTIDADE DE COLUNAS DE MATRIZ: "))

i = 0
matriz = []
while i < l:## criar lista
    linha = []
    j = 0
    while j < c:##preencher as colunas
        linha.append(0)
        j += 1
    matriz.append(linha)
    i += 1 
# print(matriz)    

# print(matriz[0])
# print(matriz[1])
# print(matriz[2])
x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1