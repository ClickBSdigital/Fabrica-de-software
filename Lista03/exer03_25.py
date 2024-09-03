# 25. Crie um programa que leia um número indeterminado de 
# idades de indivíduos (pare quando 
# for informada a idade 0), e calcule a idade média desse grupo.

# Inicializa variáveis para acumular a soma das idades e o contador de idades
soma_idades = 0
contador_idades = 0

# Inicializa a variável para a leitura da idade
idade = -1

# Loop while para ler idades até que a idade 0 seja informada
while idade != 0:
    idade = int(input("Digite uma idade (ou 0 para terminar): "))
    
    if idade != 0:
        soma_idades += idade
        contador_idades += 1

# Verifica se pelo menos uma idade válida foi inserida
if contador_idades > 0:
    idade_media = soma_idades / contador_idades
    print(f"A idade média do grupo é: {idade_media:.2f}")
else:
    print("Nenhuma idade válida foi inserida.")