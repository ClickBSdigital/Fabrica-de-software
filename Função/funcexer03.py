# Crie uma função que imprima a
# quantidade de dígitos de um determinado
# número inteiro informado.

# def  num (n1):

#     num = n1
#     return num
# num = int(input("DIGITE UM NUMERO INTEIRO: "))
# x = len(num)
# print(x)

def quantidade_digitos(numero):
    # Converte o número para string e conta o número de caracteres
    digitos = len(str(abs(numero)))
    print(f"O número {numero} tem {digitos} dígitos.")

# Exemplo de uso da função
numero = int(input("Informe um número inteiro: "))
quantidade_digitos(numero)