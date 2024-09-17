# 7. Escreva um programa que leia 
# 10 inteiros e imprima sua média.
cont = 0 ###VARIAVEL AUXILIAR
soma = 0 #AUX
while cont < 5:
    num = int(input("DIGITE UM NUMERO: "))
    soma = soma + num
    cont = cont + 1

print("soma: ",soma)
print("cont: ",cont)
print("A media é: ",soma / cont)