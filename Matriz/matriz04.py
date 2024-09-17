# Utilizando a estrutura de repetição While crie um programa que inicialize uma
# matriz 4 x 4, o usuário deve digitar os dados de entrada de cada elemento da
# matriz. Durante a execução o programa deve informar qual linha e coluna o usuário
# está preenchendo. Ao final imprima a matriz preenchida pelo usuário.
# entrada:
# lin-0 col-2:10
# entrada de dados
# lin-0 col-3:32
# entrada de dados
# lin-1 col-0:40
# entrada de dados
# lin-1 col-1:50
# entrada de dados
# lin-1 col-2:...
# ================
# saída:
# ['12', '11', '10', '32']
# ['40', '50', '44', '10']
# ['99', '12', '15', '16']
# ['18', '19', '20', '22']
l = int(input("DIGITE A QUANTIDADE DE LINHAS DA MATRIZ: "))
c = int(input("DIGITE A QUANTIDADE DE COLUNAS DE MATRIZ: "))

matriz = []
i = 0

while i < l:
    linha = []
    j = 0
    while j < c:
        valor = int(input(f"linha: {i} Coluna; {j} : "))
        linha.append(valor)
        j += 1
    matriz.append(linha)
    i += 1
    #print(f"linha: {linha} Coluna; {c}")

print(matriz)
print()

x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1