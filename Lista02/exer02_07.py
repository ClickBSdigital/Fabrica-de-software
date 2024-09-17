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