# 24. Crie um programa que some todos os números naturais abaixo 
# de 1000 que são múltiplos de 3 ou 5.
# Inicializa a variável para acumular a soma e o contador
soma = 0
numero = 1

# Loop while para iterar por todos os números de 1 a 999
while numero < 1000:
    # Verifica se o número é múltiplo de 3 ou 5
    if numero % 3 == 0 or numero % 5 == 0:
        soma += numero
    # Incrementa o contador
    numero += 1

# Exibe a soma total
print("A soma de todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5 é:", soma)
cont = 0
soma = 0

while(cont < 1000):
    if(cont % 3 == 0 or cont % 5 == 0):
        soma += cont
        cont += 1
    else:
        cont+=1

print(soma)