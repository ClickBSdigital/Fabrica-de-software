# 42. Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e 
# escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada 
# de dados com um valor negativo ou zero.
while(True):
    num = int(input("Digite um numero inteiro: "))

    quadrado = num*2

    cubo = num*3

    raiz = num ** 2

    print(f"Quadrado: {quadrado} \nCubo: {cubo} \nRaiz: {raiz}")