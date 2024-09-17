# 23. Escreva um programa que leia um número inteiro e calcule 
# a soma de todos os divisores desse 
# número, com exceção dele próprio. Ex: a soma dos divisores 
# do número 66 é:
# 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
num = int(input("DIGITE UM NÚMERO: "))
i = num
lista = []

while i > 1:
    i = i - 1
    if num % i == 0:
        lista.append(i)

print(sorted(lista))
print(sum(lista))