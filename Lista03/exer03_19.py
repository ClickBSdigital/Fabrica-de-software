# 19. Escreva um algoritmo que leia um número inteiro entre
# 100 e 9999 e imprima na saída cada um 
# dos algarismos que compõem o número.
#num = int(input("DIGITRE UM NÚMERO: "))
# Função para imprimir cada algarismo de um número

#===================================

# def imprimir_algarismos(numero):
#     numero_str = str(numero)  # Converte o número para string
#     i = 0
    
#     while i < len(numero_str):
#         print(numero_str[i])
#         i += 1

# # Solicita ao usuário que insira um número entre 100 e 9999
# numero = int(input("Digite um número inteiro entre 100 e 9999: "))

# # Verifica se o número está dentro do intervalo especificado
# if 100 <= numero <= 9999:
#     imprimir_algarismos(numero)
# else:
#     print("Número fora do intervalo especificado!")

#============================

nume = True
i = 0
while nume:
    num = int(input(("Digite um numero entre 100 e 9999: ")))

    if(num >= 100 and num <= 9999):
        numString = str(num)
        while(i < len(numString)):
            print(f"Algarismo {i} = {numString[i]}")
            i+= 1


    else:
        print("Numero inválido... Digite um número entre 100 e 9999")