produto1 = input("Digite o nome do produto: ")
codigo1 = int(input(f"Digite o código do {produto1}: "))
qtd1 = int(input(f"Digite a quantidade do {produto1}: "))
valor1 = float(input(f"Digite o valor do {produto1}: $"))
produto2 = input("Digite o nome do produto: ")
codigo2 = int(input(f"Digite o código do {produto2}: "))
qtd2 = int(input(f"Digite a quantidade do produto {produto2}: "))
valor2 = float(input(f"Digite o valor do {produto2}: $"))
produto3 = input("Digite o nome do produto: ")
codigo3 = int(input(f"Digite o código do {produto3}: "))
qtd3 = int(input(f"Digite a quantidade do produto {produto3}: "))
valor3 = float(input(f"Digite o valor do {produto3}: $"))

print(f"Saldo atual:\n{produto1} código {codigo1} possui {qtd1} unidades.\n {produto2} código {codigo2} possui {qtd2} unidades.\n {produto3} código {codigo3} possui {qtd3} unidades.\n")
print("Digite os produtos vendidos!")
qtd1_vendidos = int(input(f"Digite a quantidade de {produto1} vendidos: "))
valor1_vendido = float(input(f"Digite o valor de venda do {produto1}: $"))
qtd2_vendidos = int(input(f"Digite a quantidade de {produto2} vendidos: "))
valor2_vendido = float(input(f"Digite o valor de venda do {produto2}: $"))
qtd3_vendidos = int(input(f"Digite a quantidade de {produto3} vendidos: "))
valor3_vendido = float(input(f"Digite o valor de venda do {produto3}: $"))


qtd1 = qtd1 - qtd1_vendidos
qtd2 = qtd2 - qtd2_vendidos
qtd3 = qtd3 - qtd3_vendidos
valor1 = valor1_vendido - valor1
valor2 = valor2_vendido - valor2
valor3 = valor3_vendido - valor3 

venda = qtd1 + qtd2 + qtd3
lucro = valor1 + valor2 + valor3
lucro_total = venda * lucro

print(f"Saldo atual:\n{produto1} código {codigo1} possui {qtd1} unidades e lucor de ${valor1} por cada unidade.\n {produto2} código {codigo2} possui {qtd2} unidades e lucor de ${valor2} por cada unidade.\n {produto3} código {codigo3} possui {qtd3} unidades e lucor de ${valor3} por cada unidade.\n")
print(f"O lucro total neste período foi de ${lucro_total}")