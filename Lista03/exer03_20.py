# 20. Ler uma sequência de números inteiros e determinar se eles 
# são pares ou não. Deverá ser 
# informado o número de dados lidos e número de valores pares. 
# O processo termina quando for 
# digitado o número 0.
num = int(input("DIGITE UM NUMERO: "))
tillen = 0 #LIDOS
pares = 0
while num != 0:
    tillen += 1
    if num % 2 != 1:
        print(f" {num} É PAR!!!")
        pares += 1
    else:
        print(f" {num} NÃO É PAR!!!")
    num = int(input("DIGITE OUTRO NÚMERO: "))

print("TOTAL DE NUMEROS LIDOS: ", tillen)
print("TOTAL DE NÚMEROS PARES; ",pares)