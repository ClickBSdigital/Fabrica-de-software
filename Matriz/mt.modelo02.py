l = int(input("DIGITE A QUANTIDADE DE LINHAS DA MATRIZ: "))
c = int(input("DIGITE A QUANTIDADE DE COLUNAS DE MATRIZ: "))

i = 0
matriz = []
while i < l:## criar lista
    linha = []
    j = 0
    while j < c:##preencher as colunas
        valor = int(input("DIGITE UM NÚMERO: "))
        linha.append(valor)
        j += 1
    matriz.append(linha)
    i += 1 
# print(matriz)    

# print(matriz[0])
# print(matriz[1])
# print(matriz[2])
    
i = 0
while i < len(matriz):
    print(matriz[i])
    i += 1