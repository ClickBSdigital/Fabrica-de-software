def valorpadrao(quant,valor):
    lista = []
    for i in range(quant):
        lista.append(int(valor))
    return lista

a = int(input("DIGITE O TAMANHO DA LISTA: "))
b = input("DIGITE O VALOR PADRAO: ")

result = valorpadrao(a,b)
print(result)

# ============================================================

# O código fornecido cria uma função chamada valorpadrao() que recebe dois parâmetros: a quantidade de elementos (quant) e o valor padrão (valor). A função cria uma lista com o tamanho especificado e preenche todos os elementos com o valor fornecido.

# Aqui está uma explicação detalhada do código:

# Função valorpadrao(quant, valor):
# Entrada:

# quant: A quantidade de elementos que a lista deve ter.
# valor: O valor que será atribuído a cada elemento da lista.
# Processamento:

# A função cria uma lista vazia (lista = []).
# Em seguida, usa um laço for para adicionar o valor fornecido à lista, repetindo a operação o número de vezes especificado por quant.
# Saída: Retorna a lista preenchida com o valor padrão.

# Bloco de Execução:
# O usuário é solicitado a inserir o tamanho da lista (a) e o valor padrão para preenchimento (b).
# A função valorpadrao() é chamada com esses valores e a lista resultante é impressa.
# Código:
# python
# Copiar código
# def valorpadrao(quant, valor):
#     lista = []
#     for i in range(quant):
#         lista.append(int(valor))  # Converte o valor para inteiro antes de adicionar à lista
#     return lista

# # Entrada do usuário
# a = int(input("DIGITE O TAMANHO DA LISTA: "))  # Tamanho da lista
# b = input("DIGITE O VALOR PADRAO: ")  # Valor padrão para preencher a lista

# # Chama a função e imprime o resultado
# result = valorpadrao(a, b)
# print(result)
# Explicação:
# Entrada do Usuário:

# O tamanho da lista é lido e convertido em um número inteiro com int(input()).
# O valor padrão é lido como string, mas dentro da função valorpadrao(), é convertido para um número inteiro com int(valor).
# Saída Esperada:

# O resultado será uma lista de tamanho a preenchida com o valor b repetido.
# Exemplo de Execução:
# Suponha que o usuário insira:
# a = 5
# b = 7
# A função retornará e imprimirá:
# csharp
# Copiar código
# [7, 7, 7, 7, 7]
# Observação:
# Se b for inserido como um valor que não pode ser convertido para inteiro, o programa lançará um erro. Para evitar isso, podes melhorar o código com uma validação adicional para garantir que o valor inserido é um número inteiro.

# Se quiseres mais melhorias ou explicações sobre o código, estou à disposição!









