# 17. Escreva um programa que leia um número inteiro positivo 
# n e calcule a soma dos n primeiros 
# números naturais.
num = int(input("DIGITE UM NÚMERO: "))
i = 0
soma = 0
while i <= num:
    soma += num
    i += 1
print(soma)