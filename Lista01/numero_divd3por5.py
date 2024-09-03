# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))

# Verifica se o número é divisível por 3 ou 5
if numero % 3 == 0 or numero % 5 == 0:
    print("O número", numero, "é divisível por 3 ou 5.")
else:
    print("O número", numero, "não é divisível por 3 ou 5.")