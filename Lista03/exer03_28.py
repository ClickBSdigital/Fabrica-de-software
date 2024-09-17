# mprimindo números de 1 a 100 usando loop while
# soma = 0
# denominador = 1
# numerador = 1

# while denominador <= 50:
#     soma += numerador / denominador
#     numerador += 2
#     denominador += 1

# print(soma)

#=================================

# def calcular_S(n):
#     S = 0
#     i = 1
#     while i <= n:
#         S += i / (i + 1)
#         i += 1
#     return S

# # Solicitando o valor de n ao usuário
# n = int(input("Digite o valor de n: "))

# # Calculando e imprimindo o valor de S
# resultado_S = calcular_S(n)
# print(f"O valor de S para n = {n} é: {resultado_S}")

# ===================================

# 28. Escreva um programa que calcule e escreva o valor de S
soma = 0
cont = 1
numerador = 1

while cont <= 50:
    soma += numerador / cont
    print(f"Loop {cont} Valor: {soma}")
    numerador += 2
    cont += 1

print(f"TOTAL;{soma:.2f}")