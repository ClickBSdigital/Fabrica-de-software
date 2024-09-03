# 12. Crie um programa que leia um número inteiro positivo N 
# e imprima todos os números naturais 
# de 0 até N em ordem crescente.
num = int(input("DIGITE UM NÚMERO: "))
cont = 0
while cont <= num:
    print(num)
    num -= 1