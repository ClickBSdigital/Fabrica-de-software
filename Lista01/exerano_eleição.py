#solicite ao usuário que insira o ano
ano = int(input("Digite o ano: "))

#verifica se o ano é divisivel por 4
if ano % 4 == 0:
    print(f"O ano {ano} é um ano de eleição.")
else:
    print(f"O ano {ano} não é um ano de eleição.")