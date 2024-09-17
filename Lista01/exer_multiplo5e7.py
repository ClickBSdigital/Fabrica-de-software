#solicite ao usuário que insira um número
numero = int(input("Digite um numero: "))

#verificar se o numero é múltiplo de 5 e 7 ao mesmo tempo
if numero % 5 == 0 and numero % 7 == 0:
    print(f"O numero {numero} é múltiplo de 5 e 7 ao mesmo tempo!")
else:
    print(f"O múmero {numero} não é múltiplo de 5 e 7 ao mesmo tempo!")