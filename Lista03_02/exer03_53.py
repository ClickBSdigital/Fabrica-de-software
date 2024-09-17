# 53. Crie um programa para a Academia BemMaisFort. Neste programa você deve receber os dados 
# de 25 pessoas. Sendo: Idade, Sexo, Altura, Peso. No final o programa deve calcular e imprimir: 
# a) a idade da pessoa mais velha 
# b) a idade da pessoa mais nova
# c) a altura do mais alto
# d) altura do mais baixo
# e) o maior peso
# f) a média de Altura e a Média de IMC; 
# g) porcentagem de Sexo Masculino 
# h) porcentagem de Sexo Feminino
# Inicializando as variáveis necessárias
num_pessoas = 25
contador = 0

idades = []
sexos = []
alturas = []
pesos = []

# Coletando os dados das 25 pessoas
while contador < num_pessoas:
    idade = int(input(f"Digite a idade da pessoa {contador + 1}: "))
    sexo = input(f"Digite o sexo da pessoa {contador + 1} (M/F): ").upper()
    altura = float(input(f"Digite a altura da pessoa {contador + 1} (em metros): "))
    peso = float(input(f"Digite o peso da pessoa {contador + 1} (em kg): "))
    
    idades.append(idade)
    sexos.append(sexo)
    alturas.append(altura)
    pesos.append(peso)
    
    contador += 1

# Calculando a idade da pessoa mais velha e mais nova
idade_mais_velha = max(idades)
idade_mais_nova = min(idades)

# Calculando a altura do mais alto e do mais baixo
altura_mais_alta = max(alturas)
altura_mais_baixa = min(alturas)

# Calculando o maior peso
maior_peso = max(pesos)

# Calculando a média de altura
media_altura = sum(alturas) / len(alturas)

# Calculando o IMC de cada pessoa e a média de IMC
imcs = []
for i in range(num_pessoas):
    imc = pesos[i] / (alturas[i] ** 2)
    imcs.append(imc)
media_imc = sum(imcs) / len(imcs)

# Calculando a porcentagem de sexo masculino e feminino
num_masculino = sexos.count('M')
num_feminino = sexos.count('F')
porcentagem_masculino = (num_masculino / num_pessoas) * 100
porcentagem_feminino = (num_feminino / num_pessoas) * 100

# Exibindo os resultados
print(f"\nResultados finais:")
print(f"a) A idade da pessoa mais velha: {idade_mais_velha} anos")
print(f"b) A idade da pessoa mais nova: {idade_mais_nova} anos")
print(f"c) A altura do mais alto: {altura_mais_alta:.2f} metros")
print(f"d) A altura do mais baixo: {altura_mais_baixa:.2f} metros")
print(f"e) O maior peso: {maior_peso:.2f} kg")
print(f"f) A média de altura: {media_altura:.2f} metros")
print(f"f) A média de IMC: {media_imc:.2f}")
print(f"g) Porcentagem de sexo masculino: {porcentagem_masculino:.2f}%")
print(f"h) Porcentagem de sexo feminino: {porcentagem_feminino:.2f}%")

# #==============================================
# Explicação do Código
# Inicialização das Variáveis

# python
# Copiar código
# num_pessoas = 25
# contador = 0
# idades = []
# sexos = []
# alturas = []
# pesos = []
# Inicializa as variáveis necessárias para armazenar os dados das 25 pessoas.
# Coleta de Dados

# python
# Copiar código
# while contador < num_pessoas:
#     idade = int(input(f"Digite a idade da pessoa {contador + 1}: "))
#     sexo = input(f"Digite o sexo da pessoa {contador + 1} (M/F): ").upper()
#     altura = float(input(f"Digite a altura da pessoa {contador + 1} (em metros): "))
#     peso = float(input(f"Digite o peso da pessoa {contador + 1} (em kg): "))
    
#     idades.append(idade)
#     sexos.append(sexo)
#     alturas.append(altura)
#     pesos.append(peso)
    
#     contador += 1
# Usa um loop while para coletar a idade, sexo, altura e peso de cada uma das 25 pessoas.
# Adiciona os dados coletados nas listas correspondentes.
# Cálculos dos Dados Coletados

# Idade da pessoa mais velha e mais nova:
# python
# Copiar código
# idade_mais_velha = max(idades)
# idade_mais_nova = min(idades)
# Altura do mais alto e do mais baixo:
# python
# Copiar código
# altura_mais_alta = max(alturas)
# altura_mais_baixa = min(alturas)
# Maior peso:
# python
# Copiar código
# maior_peso = max(pesos)
# Média de altura:
# python
# Copiar código
# media_altura = sum(alturas) / len(alturas)
# Média de IMC:
# python
# Copiar código
# imcs = []
# for i in range(num_pessoas):
#     imc = pesos[i] / (alturas[i] ** 2)
#     imcs.append(imc)
# media_imc = sum(imcs) / len(imcs)
# Porcentagem de sexo masculino e feminino:
# python
# Copiar código
# num_masculino = sexos.count('M')
# num_feminino = sexos.count('F')
# porcentagem_masculino = (num_masculino / num_pessoas) * 100
# porcentagem_feminino = (num_feminino / num_pessoas) * 100
# Exibição dos Resultados

# python
# Copiar código
# print(f"\nResultados finais:")
# print(f"a) A idade da pessoa mais velha: {idade_mais_velha} anos")
# print(f"b) A idade da pessoa mais nova: {idade_mais_nova} anos")
# print(f"c) A altura do mais alto: {altura_mais_alta:.2f} metros")
# print(f"d) A altura do mais baixo: {altura_mais_baixa:.2f} metros")
# print(f"e) O maior peso: {maior_peso:.2f} kg")
# print(f"f) A média de altura: {media_altura:.2f} metros")
# print(f"f) A média de IMC: {media_imc:.2f}")
# print(f"g) Porcentagem de sexo masculino: {porcentagem_masculino:.2f}%")
# print(f"h) Porcentagem de sexo feminino: {porcentagem_feminino:.2f}%")
# Exibe os resultados calculados.