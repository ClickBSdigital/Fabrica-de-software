# 9. Escreva um programa que leia 10 números e escreva o 
# menor valor lido e o maior valor lido.
# lista = []
# cont = 0

# while cont <= 4:
#     num = int(input("DIGITE UM NUMERO: "))
#     lista.append(num)
#     cont = cont + 1
# print(sorted(lista))
# print(cont)
# print(lista)
# print(len(lista))
# print("O menor é: ", min(lista), "e o maior é: ", (max(lista)))
num = int(input("DIGITE UM NUMERO: "))
cont = 0
maior = num
menor = num

while cont < 4:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont = cont + 1
    num = int(input("DIGITE UM NUMERO: "))
print("O número maior é: ", maior)
print("O número memor é : ", menor)