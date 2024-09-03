# Escreva um programa que solicite ao usuário números inteiros positivos. O
# programa deve somar esses números até que o usuário insira um número
# negativo, então deve imprimir o resultado da soma.

lista = []

while(True):
    num = int(input("Digite um numero positivo para ser adicionado na lista ou digite um numero negativo para finalizar: "))
    
    if(num < 0):
        break
    else:
        lista.append(num)

soma = sum(lista)

print(f"Numeros digitados: {lista} \nSoma dos numeros: {soma}")