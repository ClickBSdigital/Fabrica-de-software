# 6. Escreva um programa que 
# peça ao usuário para digitar 10 valores e some-os
cont = 0 ###VARIAVEL AUXILIAR
soma = 0 #AUX
while cont < 3:
    num = int(input("DIGITE UM NUMERO: "))
    soma = soma + num
    cont = cont + 1

print("Soma é: ",soma)