# 31. Um funcionário recebe aumento anual. Em 2019 foi contratado por 4000 reais. Em 2020
# recebeu aumento de 1.5%. A partir de 2021, os aumentos sempre correspondem ao dobro do 
# ano anterior. Faça um programa que determine o salário atual do funcionário
ano_atual = int(input("Digite o ano atual: "))
salario = 4000
ano = 2021
aumento = 0.015

while ano <= ano_atual:
    print(f"Percentual: {aumento} Ano: {ano}")
    salario += salario * aumento
    aumento *= 2
    print("NOVO SALÁRIO: ",salario)
    ano = ano + 1