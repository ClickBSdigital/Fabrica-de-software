numero01 = int(input("Digite um numero inteiro: "))
numero02 = int(input("Digite outro numero inteiro: "))
numero03 = int(input("Digite ooutro numero inteiro: "))

if numero01 < numero02 < numero03:
    print(f"Os numeros: {numero01}, {numero02}, {numero03}, estão em ordem crescente.")
else:
    print("Os numeros não está em ordem crescente!")