# 48. Dada uma sequência de 3 números inteiros, determinar o número de vezes que cada um deles 
# ocorre em uma lista. Comparar se os digitados aparecem na lista. Para exemplificar, considere:
# Lista: [1, 1, 4, 5, 6, 7, 3, 2, 2, -1]
# Entrada: 1, 2 e 3
# Saída:
# 1: ocorreu 2 vezes
# 2: ocorreu 2 vezes
# 3: ocorreu 1 vez
# Lista predefinida
lista = [1, 1, 4, 5, 6, 7, 3, 2, 2, -1]

# Solicita ao usuário três números inteiros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Lista para armazenar os números digitados
numeros_digitados = [num1, num2, num3]

# Dicionário para armazenar as contagens
contagem = {num1: 0, num2: 0, num3: 0}

# Inicializa o índice para o loop while
i = 0

# Loop while para contar as ocorrências na lista
while i < len(lista):
    numero = lista[i]
    if numero in contagem:
        contagem[numero] += 1
    i += 1

# Exibe os resultados
i = 0
while i < len(numeros_digitados):
    numero = numeros_digitados[i]
    print(f"{numero}: ocorreu {contagem[numero]} vezes")
    i += 1

# Comparação se os números aparecem na lista
i = 0
while i < len(numeros_digitados):
    numero = numeros_digitados[i]
    if numero in lista:
        print(f"{numero}: aparece na lista")
    else:
        print(f"{numero}: não aparece na lista")
    i += 1
#===================================
# Explicação do Código
# Definição da Lista Predefinida

# python
# Copiar código
# lista = [1, 1, 4, 5, 6, 7, 3, 2, 2, -1]
# lista: A lista na qual verificaremos as ocorrências dos números fornecidos pelo usuário.
# Entrada do Usuário

# python
# Copiar código
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))
# Solicita ao usuário que digite três números inteiros.
# Inicialização das Estruturas para Armazenar os Números e suas Contagens

# python
# Copiar código
# numeros_digitados = [num1, num2, num3]
# contagem = {num1: 0, num2: 0, num3: 0}
# numeros_digitados: Uma lista que armazena os três números fornecidos pelo usuário.
# contagem: Um dicionário que inicializa as contagens de cada número fornecido como zero.
# Contagem das Ocorrências na Lista com Loop while

# python
# Copiar código
# i = 0
# while i < len(lista):
#     numero = lista[i]
#     if numero in contagem:
#         contagem[numero] += 1
#     i += 1
# i = 0: Inicializa o índice i para o loop.
# while i < len(lista): O loop continua enquanto i for menor que o comprimento da lista.
# Em cada iteração, verifica se o número atual (lista[i]) está no dicionário contagem.
# Se estiver, incrementa a contagem correspondente.
# Incrementa i em cada iteração.
# Exibição das Contagens com Loop while

# python
# Copiar código
# i = 0
# while i < len(numeros_digitados):
#     numero = numeros_digitados[i]
#     print(f"{numero}: ocorreu {contagem[numero]} vezes")
#     i += 1
# i = 0: Reinicializa o índice i.
# while i < len(numeros_digitados): O loop continua enquanto i for menor que o comprimento de numeros_digitados.
# Em cada iteração, exibe quantas vezes cada número ocorreu na lista.
# Incrementa i em cada iteração.
# Comparação se os Números Aparecem na Lista com Loop while

# python
# Copiar código
# i = 0
# while i < len(numeros_digitados):
#     numero = numeros_digitados[i]
#     if numero in lista:
#         print(f"{numero}: aparece na lista")
#     else:
#         print(f"{numero}: não aparece na lista")
#     i += 1
# i = 0: Reinicializa o índice i.
# while i < len(numeros_digitados): O loop continua enquanto i for menor que o comprimento de numeros_digitados.
# Em cada iteração, verifica se cada número digitado pelo usuário está presente na lista.
# Exibe uma mensagem indicando se o número aparece ou não na lista.
# Incrementa i em cada iteração.
# Exemplo de Execução
# Entrada do Usuário:
# plaintext
# Copiar código
# Digite o primeiro número: 1
# Digite o segundo número: 2
# Digite o terceiro número: 3
# Saída:
# plaintext
# Copiar código
# 1: ocorreu 2 vezes
# 2: ocorreu 2 vezes
# 3: ocorreu 1 vez
# 1: aparece na lista
# 2: aparece na lista
# 3: aparece na lista
# O programa lê três números fornecidos pelo usuário, conta quantas vezes cada número ocorre na lista e verifica se eles aparecem na lista, exibindo os resultados conforme solicitado.