# 29. Crie um programa que calcule o menor número divisível por 
# cada um dos números de 1 a 20? 
# Ex: 2520 e o menor número que pode ser dividido por cada 
# um dos números de 1 a 10, sem 
# sobrar resto
# num = int(input("Digite um numero inteiro: "))
# numDivisiveis = []
# i = 1

# while(i <= 20):
#     if(num % i == 0):
#         numDivisiveis.append(i)
#         i+=1
#     else:
#         i+=1

# print(numDivisiveis)

#===================================

import math

def calcula_mmc(a, b):
    # Calcula o MMC de dois números a e b
    return abs(a * b) // math.gcd(a, b)

def mmc_de_1_a_n(n):
    # Inicializa o MMC com o primeiro número
    mmc = 1
    # Itera sobre todos os números de 1 até n
    for i in range(1, n + 1):
        # Calcula o MMC progressivamente
        mmc = calcula_mmc(mmc, i)
    return mmc

# Calcula o MMC de 1 a 20
resultado = mmc_de_1_a_n(20)

# Exibe o resultado
print("O menor número divisível por cada um dos números de 1 a 20 é:", resultado)
