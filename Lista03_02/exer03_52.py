# 52. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior 
# nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um 
# programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em 
# sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar 
# o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são 
# informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo 
# abaixo:
# Atleta: Thiago Almeida
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7
# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04
while True:
    # Leitura do nome do atleta
    nome_atleta = input("Digite o nome do atleta: ")
    
    # Leitura das notas dos jurados
    notas = []
    for i in range(7):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)
    
    # Exibição das notas
    for nota in notas:
        print(f"Nota: {nota}")
    
    # Cálculo da melhor e pior nota
    melhor_nota = max(notas)
    pior_nota = min(notas)
    
    # Remoção da melhor e pior nota
    notas.remove(melhor_nota)
    notas.remove(pior_nota)
    
    # Cálculo da média das notas restantes
    media = sum(notas) / len(notas)
    
    # Exibição do resultado final
    print("\nResultado final:")
    print(f"Atleta: {nome_atleta}")
    print(f"Melhor nota: {melhor_nota}")
    print(f"Pior nota: {pior_nota}")
    print(f"Média: {media:.2f}")
    
    # Pergunta ao usuário se deseja continuar
    continuar = input("\nDeseja inserir dados de outro atleta? (s/n): ")
    if continuar.lower() != 's':
        break
#=========================

# Explicação do Código
# Loop Principal while True

# O loop principal permite que o programa continue executando até que o usuário decida parar.
# Leitura do Nome do Atleta

# python
# Copiar código
# nome_atleta = input("Digite o nome do atleta: ")
# O programa solicita ao usuário que insira o nome do atleta.
# Leitura das Notas dos Jurados

# python
# Copiar código
# notas = []
# for i in range(7):
#     nota = float(input(f"Digite a nota {i + 1}: "))
#     notas.append(nota)
# As notas dos sete jurados são lidas e armazenadas em uma lista.
# Exibição das Notas

# python
# Copiar código
# for nota in notas:
#     print(f"Nota: {nota}")
# As notas inseridas são exibidas para o usuário.
# Cálculo da Melhor e Pior Nota

# python
# Copiar código
# melhor_nota = max(notas)
# pior_nota = min(notas)
# As funções max e min são usadas para encontrar a melhor e a pior nota, respectivamente.
# Remoção da Melhor e Pior Nota

# python
# Copiar código
# notas.remove(melhor_nota)
# notas.remove(pior_nota)
# A melhor e a pior nota são removidas da lista.
# Cálculo da Média das Notas Restantes

# python
# Copiar código
# media = sum(notas) / len(notas)
# A média das notas restantes é calculada.
# Exibição do Resultado Final

# python
# Copiar código
# print("\nResultado final:")
# print(f"Atleta: {nome_atleta}")
# print(f"Melhor nota: {melhor_nota}")
# print(f"Pior nota: {pior_nota}")
# print(f"Média: {media:.2f}")
# O nome do atleta, a melhor nota, a pior nota e a média são exibidos.
# Pergunta ao Usuário se Deseja Continuar

# python
# Copiar código
# continuar = input("\nDeseja inserir dados de outro atleta? (s/n): ")
# if continuar.lower() != 's':
#     break
# O programa pergunta ao usuário se ele deseja inserir dados de outro atleta. Se a resposta não for 's' (sim), o loop é interrompido e o programa termina.