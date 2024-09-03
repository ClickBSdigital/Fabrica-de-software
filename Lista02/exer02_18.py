h = float(input("Digite a altura: "))
sexo = input("Digite M ou H informando seu gênero: ")

homem = (72.7 * h) - 58
mulher = (62.1 * h) - 44.7

if sexo == "M" or sexo == "m":
    print(f"Você sendo uma Mulher, seu peso idela é de: {mulher}")
elif sexo == "H" or sexo == "h":
    print(f"Você sendo um Homem, seu peso idela é de: {homem}")
else:
    print("GÊNERO NÃO INFORMADO")