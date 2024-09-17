# 49. Faça um programa que leia vários números, calcule e mostre:
# (a) A soma dos números digitados
# (b) A quantidade de números digitados
# (c) A média dos números digitados
# (d) O maior número digitado
# (e) O menor número digitado
# (f) A média dos números pares
# Finalize a entrada de dados caso o usuário informe o valor 0.
# Inicialização das variáveis
soma = 0
quantidade = 0
maior = None
menor = None
soma_pares = 0
quantidade_pares = 0

while True:
    numero = int(input("Digite um número (0 para finalizar): "))
    
    if numero == 0:
        break
    
    # Atualização da soma e quantidade
    soma += numero
    quantidade += 1
    
    # Verificação do maior e menor número
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
    
    # Atualização da soma e quantidade dos números pares
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1

# Cálculo das médias
media = soma / quantidade if quantidade > 0 else 0
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0

# Exibição dos resultados
print(f"Soma dos números digitados: {soma}")
print(f"Quantidade de números digitados: {quantidade}")
print(f"Média dos números digitados: {media}")
print(f"Maior número digitado: {maior}")
print(f"Menor número digitado: {menor}")
print(f"Média dos números pares: {media_pares}")
# #==========================================
# Explicação do Código
# Inicialização das Variáveis

# python
# Copiar código
# soma = 0
# quantidade = 0
# maior = None
# menor = None
# soma_pares = 0
# quantidade_pares = 0
# soma: Armazena a soma dos números digitados.
# quantidade: Conta a quantidade de números digitados.
# maior: Armazena o maior número digitado.
# menor: Armazena o menor número digitado.
# soma_pares: Armazena a soma dos números pares digitados.
# quantidade_pares: Conta a quantidade de números pares digitados.
# Loop while para Leitura dos Números

# python
# Copiar código
# while True:
#     numero = int(input("Digite um número (0 para finalizar): "))
    
#     if numero == 0:
#         break
# O loop continua indefinidamente até que o usuário digite 0.
# O número digitado pelo usuário é lido e armazenado na variável numero.
# Se o número for 0, o loop é interrompido com break.
# Atualização da Soma e Quantidade

# python
# Copiar código
# soma += numero
# quantidade += 1
# A variável soma é atualizada com o valor do número digitado.
# A variável quantidade é incrementada em 1.
# Verificação do Maior e Menor Número

# python
# Copiar código
# if maior is None or numero > maior:
#     maior = numero
# if menor is None or numero < menor:
#     menor = numero
# Se maior for None (inicialização) ou o número atual for maior que maior, atualiza maior.
# Se menor for None (inicialização) ou o número atual for menor que menor, atualiza menor.
# Atualização da Soma e Quantidade dos Números Pares

# python
# Copiar código
# if numero % 2 == 0:
#     soma_pares += numero
#     quantidade_pares += 1
# Se o número for par (resto da divisão por 2 igual a 0), atualiza soma_pares e incrementa quantidade_pares.
# Cálculo das Médias

# python
# Copiar código
# media = soma / quantidade if quantidade > 0 else 0
# media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
# A média geral é calculada dividindo soma por quantidade, garantindo que quantidade seja maior que 0.
# A média dos números pares é calculada dividindo soma_pares por quantidade_pares, garantindo que quantidade_pares seja maior que 0.
# Exibição dos Resultados

# python
# Copiar código
# print(f"Soma dos números digitados: {soma}")
# print(f"Quantidade de números digitados: {quantidade}")
# print(f"Média dos números digitados: {media}")
# print(f"Maior número digitado: {maior}")
# print(f"Menor número digitado: {menor}")
# print(f"Média dos números pares: {media_pares}")
# Os resultados são exibidos ao usuário com mensagens descritivas.