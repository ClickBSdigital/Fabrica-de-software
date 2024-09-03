importancia = 780000
ganhador1 = 46
ganhador2 = 32

valor_ganhador1 = importancia - ganhador1/100
valor_total_g1 = valor_ganhador1 - importancia
valor_ganhador2 = importancia - ganhador2/100
valor_total_g2 = valor_ganhador2 - importancia
valor_ganhador3 = valor_ganhador1 + valor_ganhador2 - importancia

print(f"O primeiro ganhador recebe o valor de: ${valor_total_g1}/n")
print(f"O segundo ganhador recebe o valor de: ${valor_total_g2}/n")
print(f"O terceiro ganhador recebe o valor de: ${valor_ganhador3}/n")