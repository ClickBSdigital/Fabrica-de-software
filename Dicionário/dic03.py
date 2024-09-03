# Crie um dicionário chamado aluno com informações básicas sobre um estudante (nome, 
# idade, cidade). Utilize um loop para iterar sobre as chaves e valores do dicionário e imprimir 
# cada informação em uma linha.
# Criando o dicionário aluno
aluno = {
    "nome": "Maria Oliveira",
    "idade": 21,
    "cidade": "Porto"
}

# Iterando sobre as chaves e valores do dicionário e imprimindo cada informação
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")

#######################################

# Explicação:
# Dicionário aluno: O dicionário contém três chaves: nome, idade e cidade, com seus respectivos valores.
# Loop for: O loop for chave, valor in aluno.items() itera sobre cada par de chave e valor no dicionário.
# Impressão Formatada: Cada chave é formatada com a primeira letra em maiúscula usando capitalize() e seu valor correspondente é impresso em uma linha.
# Exemplo de Saída:
# makefile
# Copiar código
# Nome: Maria Oliveira
# Idade: 21
# Cidade: Porto
# Este código permite que você organize e exiba de forma clara as informações básicas de um estudante armazenadas em um dicionário.