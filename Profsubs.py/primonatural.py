# '''
# Receba um número inteiro positivo na entrada e imprima os n
# primeiros números ímpares naturais. Para a saída, siga o
# formato do exemplo abaixo.
# '''
num = int(input("Digite um número inteiro positevo: "))
cont = 0
numero = 1

print("Os", num, "primeiro numeros impares naturais são: ")
while cont < num:
    print(numero)
    numero += 2
    cont += 1