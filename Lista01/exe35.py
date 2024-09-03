produto = float(input("Digite o valor do produto: $"))
desconto = 12

valor_desconto = produto * desconto/100
valor_final = produto - valor_desconto

print("O valor com desconto é: $ ", valor_final)
