# 45. O funcionário chamado Carlos tem um colega chamado João que recebe um salário que é 
# equivale a um terço do seu salário. Carlos gosta de fazer aplicações na caderneta de poupança
# e vai aplicar seu salário integralmente nela, pois está rendendo 2% ao mês. João irá aplicar seu 
# salário integralmente no fundo de renda fixa, que está rendendo 5% ao mês. Construa um 
# programa que deverá calcular e mostrar a quantidade de meses necessários para que o valor 
# pertencente a João iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores 
# para as taxas
# carlos > joao 
# joao recebe 1/3 do salario do carlos

# carlos vai aplicar 100% do seu salario em um rendimento de 2% ao mês
# joao vai aplicar 100% do seu salario em um rendimento de 5% ao mês

salarioCarlos = float(input("Digite o valor do salario de Carlos: "))
salarioJoao = salarioCarlos / 3

print(f"Salario de Joao: {salarioJoao}")
print(f"Salario de Carlos: {salarioCarlos}")

mes = 0
while(salarioJoao <= salarioCarlos):
    rendimentoMesJoao = salarioJoao * 0.05
    rendimentoMesCarlos = salarioCarlos * 0.02

    salarioJoao += rendimentoMesJoao
    salarioCarlos += rendimentoMesCarlos

    mes += 1

print(f"Salario do carlos em {mes} meses: {salarioCarlos:.2f}")
print(f"Salario do joao em {mes} meses: {salarioJoao:.2f}")

print(f"Em {mes} meses o joão terá um salario maior que o de Carlos")