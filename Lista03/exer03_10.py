# 10. Crie um programa que leia um número inteiro N e 
# depois imprima os N primeiros números
# naturais ímpares.
# num = int(input("Digite um numero inteiro: "))
# cont = 1

# while cont <= num:
#     if cont % 2 == 1:
#         print (cont)
#     cont = cont + 1

num = int(input("Digite um numero inteiro: "))
cont = 1

while cont <= num:
    # if cont % 2 == 1: #se o resto da divisão for igual a 1 é impar
    if cont % 2 != 0: #se o resto da divisão for igual a 0 é par  
        print (cont)
    cont = cont + 1

# def imprimir_impares(N):
#     contagem = 0
#     numero = 1

#     while contagem < N:
#         if numero % 2 != 0:
#             print(numero)
#             contagem += 1
#         numero += 1

# # Solicita ao usuário que insira o valor de N
# N = int(input("Digite um número inteiro N: "))
# imprimir_impares(N)