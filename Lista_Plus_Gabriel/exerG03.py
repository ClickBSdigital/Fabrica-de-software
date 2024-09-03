# Escreva um programa que calcule a soma de todos os números ímpares de 1
# a 100 utilizando um loop for.
soma = 0

for i in range(1, 101, 2):
    print(f"Numero impar: {i}")
    soma += i
    print(f"Soma dos impar {soma}")