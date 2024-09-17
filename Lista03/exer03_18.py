# 18. Escreva um algoritmo que leia certa quantidade de 
# números e imprima o maior deles. A 
# quantidade de números a serem lidos deve será fornecida 
# pelo usuário.
quant = int(input("DIGITE A GUANTIDADE DE NUMEROS A SEREM LIDOS: "))
maior = 0
i = 0
while i < quant:
    num = int(input("DIGITE UM NÚMERO: "))
    if num > maior:
        maior = num
    i = i + 1
print("MAIOR: ", maior)