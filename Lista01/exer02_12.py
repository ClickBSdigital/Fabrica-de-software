numero01 = int(input("Digite um número: "))
numero02 = int(input("Digite outro número: "))
diferenca = numero01 % numero02
if numero01 > numero02:
    print(f"O numero {numero01} é maior que {numero02} e sua diferença é de {diferenca}.")
else:
    print(f"O numero {numero02} é maior que {numero01} e sua diferença é de {diferenca}.")