# 34. Faça um Programa que leia 20 números inteiros e armazene-os em uma LISTA. Armazene os 
# números pares na lista PAR e os números IMPARES na lista ímpar. Imprima os três vetores.
listaInteira = []

listaPar = []

ListaImpar = []

i = 0

while(i < 20):
    num = int(input("Digite um numero a ser adicionado na lista: "))

    listaInteira.append(num)
    if(num % 2 == 0):
        listaPar.append(num)
    else:
        ListaImpar.append(num)
    i += 1

print(f"Numeros digitados: {listaInteira} \nNumeros Par: {listaPar} \nNumeros impar: {ListaImpar}")