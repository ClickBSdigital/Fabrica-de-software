# 50. Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente 
# os n primeiros naturais que são múltiplos de i ou de j e ou de ambos. Exemplo: Para n = 6, i = 2 
# e j = 3 a saída deverá ser: 0,2,3,4,6,8.
# Leitura dos valores de n, i e j
n = int(input("Digite o valor de n: "))
i = int(input("Digite o valor de i (não pode ser 0): "))
j = int(input("Digite o valor de j (não pode ser 0): "))

# Lista para armazenar os múltiplos encontrados
multiplos = []

# Inicialização da variável contador
contador = 0

while len(multiplos) < n:
    # Verifica se o contador é múltiplo de i ou de j
    if contador % i == 0 or contador % j == 0:
        multiplos.append(contador)
    contador += 1

# Exibição dos n primeiros múltiplos de i ou de j
print("Os primeiros", n, "múltiplos de", i, "ou", j, "são:", ', '.join(map(str, multiplos)))
# #===================================
# Explicação do Código
# Leitura dos Valores de Entrada

# python
# Copiar código
# n = int(input("Digite o valor de n: "))
# i = int(input("Digite o valor de i (não pode ser 0): "))
# j = int(input("Digite o valor de j (não pode ser 0): "))
# O programa solicita ao usuário que forneça os valores de n, i e j.
# n é a quantidade de múltiplos que queremos encontrar.
# i e j são os divisores, e não podem ser zero.
# Inicialização das Estruturas de Dados

# python
# Copiar código
# multiplos = []
# contador = 0
# multiplos: Uma lista vazia para armazenar os múltiplos encontrados.
# contador: Uma variável inicializada em 0 para contar os números naturais.
# Loop while para Encontrar os Múltiplos

# python
# Copiar código
# while len(multiplos) < n:
#     if contador % i == 0 or contador % j == 0:
#         multiplos.append(contador)
#     contador += 1
# O loop continua enquanto o tamanho da lista multiplos for menor que n.
# Em cada iteração, verifica se o valor de contador é múltiplo de i ou j.
# Se for, adiciona o valor de contador à lista multiplos.
# Incrementa contador em cada iteração.
# Exibição dos Resultados

# python
# Copiar código
# print("Os primeiros", n, "múltiplos de", i, "ou", j, "são:", ', '.join(map(str, multiplos)))
# Após encontrar os n primeiros múltiplos, o programa exibe os resultados em ordem crescente.
# A função join é usada para transformar a lista de inteiros em uma string formatada com os múltiplos separados por vírgulas.
# Exemplo de Execução
# Entrada do Usuário:
# plaintext
# Copiar código
# Digite o valor de n: 6
# Digite o valor de i (não pode ser 0): 2
# Digite o valor de j (não pode ser 0): 3
# Saída:
# plaintext
# Copiar código
# Os primeiros 6 múltiplos de 2 ou 3 são: 0, 2, 3, 4, 6, 8
# O programa lê os valores de n, i, e j, e encontra os primeiros n múltiplos de i ou j, exibindo-os em ordem crescente.