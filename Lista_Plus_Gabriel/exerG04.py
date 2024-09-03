# Faça um programa que leia uma lista de números e imprima o quadrado de
# cada número utilizando um loop for.

lista = []

flag = True

while(flag):
    num = int(input("Digite um numero inteiro a ser adicionado nalista ou digite '0' para finalizar: " ))

    if(num == 0):
        flag = False
    else:
        lista.append(num)

cont = 0
for i in lista:
    quadrado = lista[cont] ** 2
    print(quadrado)
    cont+=1