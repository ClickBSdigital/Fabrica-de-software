#Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor 
#de sua aquisição: Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser 
#vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, Crie um 
#algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.

nome = input("Digite o nome do produto: ")
valor_entrada = float(input("digite o valor de entrada: $"))
acressimo01 = 45
acressimo02 = 30

total_da_venda01 = valor_entrada * acressimo01/100 
venda_final_01 = valor_entrada + total_da_venda01

total_da_venda02 = valor_entrada * acressimo02/100 
venda_final_02 = valor_entrada + total_da_venda02

if valor_entrada < 50:
    print(f"O produto: {nome} tem o valor a venda de: ${venda_final_01}")
else:
    print(f"O produto: {nome} tem o valor a venda de: ${venda_final_02}")