# 8. Escreva um programa que leia 10 inteiros positivos, 
# ignorando não positivos, e imprima sua média.
soma = 0
aux = 0 #AUXILIAR => OBJETIVO NOMES: cont, i , x etc...
while aux < 10:
    num = int(input("DIGITE UM NÚMERO: "))
    if num > 0:
        print("Caiu no IF")
        soma = soma + num
        aux = aux + 1
    else:
        print("VALOR DO CONT: ",aux)
        print("VALOR DA SOMA: ",soma)
        continue

media = soma / aux
print("MÉDIA: ",media)

