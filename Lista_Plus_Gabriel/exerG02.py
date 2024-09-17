# Crie um programa que solicite um número ao usuário e imprima todos os
# números pares de 0 até esse número utilizando um loop while.

flag = True
i = 0
while(flag):
    num = int(input("Digite um numero inteiro: "))

    while(i <= num):
        if(i % 2 == 0):
            print(f"Par: {i}")
            i+=1
        else:
            i+=1
    i = 0