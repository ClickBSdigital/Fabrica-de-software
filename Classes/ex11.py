def imprimir(lista):
    cont = 1
    for item in lista:
        print(f' {cont}, {item}')
        cont += 1

def imprimircomwhile(lista):
    i = 0
    while i < len(lista):
        print(f'\n {i+1}, {lista[i]}')
        i += 1

frutas = ['ABACAXI','MAMAO','MELANCIA','PERA','UVA']
imprimir(frutas)
imprimircomwhile(frutas)


# # +===================================
# O código fornecido define duas funções, imprimir() e imprimircomwhile(), para exibir elementos de uma lista com os seus respectivos números de ordem. A diferença entre elas é que uma usa o loop for e a outra usa o loop while. A lista de frutas frutas é usada como exemplo para testar essas funções.

# Aqui está uma explicação detalhada:

# Funções:
# Função imprimir(lista):

# Utiliza um loop for para iterar sobre cada item da lista.
# Em cada iteração, imprime o índice (começando em 1) seguido do item correspondente da lista.
# O contador cont é incrementado a cada iteração para manter a contagem correta.
# Função imprimircomwhile(lista):

# Usa um loop while para percorrer a lista.
# A variável i começa em 0 e é usada para acessar os elementos da lista com lista[i].
# O índice i+1 é impresso junto com o item correspondente, e o valor de i é incrementado a cada iteração até que i seja igual ao comprimento da lista.
# Código:
# python
# Copiar código
# def imprimir(lista):
#     cont = 1
#     for item in lista:
#         print(f' {cont}, {item}')
#         cont += 1

# def imprimircomwhile(lista):
#     i = 0
#     while i < len(lista):
#         print(f'\n {i+1}, {lista[i]}')
#         i += 1

# frutas = ['ABACAXI', 'MAMAO', 'MELANCIA', 'PERA', 'UVA']
# imprimir(frutas)
# imprimircomwhile(frutas)
# Saída Esperada:
# Para a função imprimir(lista) com for:

# Copiar código
#  1, ABACAXI
#  2, MAMAO
#  3, MELANCIA
#  4, PERA
#  5, UVA
# Para a função imprimircomwhile(lista) com while:

# Copiar código
#  1, ABACAXI

#  2, MAMAO

#  3, MELANCIA

#  4, PERA

#  5, UVA
# Diferenças:
# A função imprimir() imprime os elementos de forma contínua, linha após linha, enquanto a função imprimircomwhile() adiciona uma linha em branco antes de cada impressão por conta do \n incluído na string de impressão.
# Se quiseres que o comportamento das duas funções seja mais consistente (sem linhas em branco na versão while), basta remover o \n na função imprimircomwhile():

# python
# Copiar código
# def imprimircomwhile(lista):
#     i = 0
#     while i < len(lista):
#         print(f' {i+1}, {lista[i]}')
#         i += 1
# Com essa alteração, ambas as funções produzirão a mesma saída.