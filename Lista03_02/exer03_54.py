# 54. Leia um número positivo digitado pelo usuário, então, calcule e imprima a sequência Fibonacci 
# até o primeiro número superior ao número lido. Exemplo: se o usuário informou o número 30, 
# a sequência a ser impressa será: 0 1 1 2 3 5 8 13 21 34.
# Solicitando ao usuário que digite um número positivo
numero = int(input("Digite um número positivo: "))

# Inicializando os primeiros dois termos da sequência Fibonacci
a, b = 0, 1

# Imprimindo os primeiros dois termos da sequência Fibonacci
print(a, end=" ")
print(b, end=" ")

# Calculando e imprimindo os próximos termos da sequência até o primeiro número superior ao número lido
while True:
    c = a + b
    if c > numero:
        break
    print(c, end=" ")
    a, b = b, c

print()  # Adiciona uma nova linha ao final da sequência
# #===================================

# Explicação do Código
# Solicitação do Número ao Usuário

# python
# Copiar código
# numero = int(input("Digite um número positivo: "))
# O programa solicita ao usuário que digite um número positivo.
# Inicialização dos Primeiros Termos da Sequência Fibonacci

# python
# Copiar código
# a, b = 0, 1
# Os primeiros termos da sequência Fibonacci são inicializados com 0 e 1.
# Impressão dos Primeiros Termos da Sequência Fibonacci

# python
# Copiar código
# print(a, end=" ")
# print(b, end=" ")
# Os primeiros termos da sequência Fibonacci são impressos.
# Cálculo e Impressão dos Próximos Termos da Sequência Fibonacci

# python
# Copiar código
# while True:
#     c = a + b
#     if c > numero:
#         break
#     print(c, end=" ")
#     a, b = b, c
# Um loop while é utilizado para calcular e imprimir os próximos termos da sequência Fibonacci até que o próximo termo seja superior ao número digitado pelo usuário.
# O loop é encerrado com a instrução break quando o próximo termo da sequência Fibonacci (c) for superior ao número informado pelo usuário.
# Os valores de a e b são atualizados a cada iteração para gerar o próximo termo da sequência Fibonacci.
# Adição de uma Nova Linha ao Final da Sequência

# python
# Copiar código
# print()
# Uma nova linha é adicionada ao final da sequência para melhorar a formatação da saída.
# Este programa garante que a sequência Fibonacci seja calculada e impressa corretamente até o primeiro número superior ao número digitado pelo usuário.