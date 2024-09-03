# 32. Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório 
# desses números na tela. Após exibir a soma, o programa deve mostrar também os números que 
# o usuário digitou, um por linha.
salario2019 = 4000

aumento = 0

print(f"Salario em 2020: R${salario2019 * 1.015:.2f}")

salario2021 = salario2019 * 1.015

anoAtual= int(input("Digite o ano atual: "))
contAno = 2021
i = 2021

while(i <= anoAtual):
    aumento = (0.015 * 2 ) + aumento
    print(f"Salario no ano de {contAno}: {(salario2021 * aumento) + salario2021:.2f}")
    contAno += 1
    i += 1