# 46. Chico tem 1.70 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.20 metros e cresce 3 
# centímetros por ano. Escreva um programa que calcule e imprima quantos anos serão
# necessários para que Zé seja maior que Chico.
ze = 1.60
chico = 1.70
anos = 0
while ze <= chico:
    chico += 0.02
    ze += 0.03
    anos += 1

print(f"QUANTIDADE DE ANOS: {anos:.2f}")
print("ALTURA FINAL DO ZÉ: ",ze)
print("ALTURA FINAL DO CHICO: ",chico)
