# 30. Elabore um programa que faça leitura de vários números inteiros, 
# até que se digite um número
# negativo. O programa tem que retornar o maior e o menor número lido.
# #=================================
# num = int(input("DIGITE UM NUMERO; "))
# maior = num
# menor = num
# while num > 0:
#     if num > maior:
#         mairo = num
#     if num < menor:
#         menor = num
#     num = int(input("DIGITE UM NÚMERO: "))

# print("MAIOR: ", maior)
# print("MENOR: ", menor)
# print("FIM DO CÓDIGO")

#===================================
maior = 0
menor = 9999999999
while True:
    num = int(input("DIGITE UM NUMERO: "))
    if num < 0:
        break
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print("MAIOR: ", maior)
print("MENOR: ", menor)
print("FIM DO CÓDIGO")