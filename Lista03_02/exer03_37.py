# # 37. Escreva um programa que receba um número inteiro maior do que 1, e verifique se o número
# # fornecido é primo ou não.
# Numero = int(input("Digite um número inteiro: "))

# # Verifica se o número é 0 ou 1
# while Numero == 0 or Numero == 1:
#     print("O número que você quer verificar se é primo deve ser maior que 1.")
#     Numero = int(input("Digite novamente um número inteiro: "))

# # Verifica se o número é 2
# if Numero == 2:
#     print("O número 2 é primo.")
# else:
#     ContadorDeDivisores = 0
#     Divisor = 1
#     cont = 0

#     # Loop para verificar divisores do número
#     while Divisor <= Numero:
#         if Numero % Divisor == 0:
#             ContadorDeDivisores += 1
#         Divisor += 1

#     # Verifica se o número tem mais de dois divisores (além de 1 e ele mesmo)
#     if ContadorDeDivisores > 2:
#         print(f"O número {Numero} não é primo.")
#     else:
#         print(f"O número {Numero} é primo.")

# #     Explicações do código:

# # Entrada do número: O código começa solicitando ao usuário que digite um número inteiro.

# # Verificação inicial: Um loop while é usado para garantir que o número digitado seja maior 
# # que 1. Se o número for 0 ou 1, uma mensagem é exibida pedindo ao usuário que forneça um número válido.

# # Verificação para o número 2: Se o número digitado for 2, o programa exibe que 2 é primo e encerra a execução.

# # Verificação para outros números: Para números maiores que 2, o programa inicia um contador de divisores 
# # (ContadorDeDivisores) e um divisor (Divisor) inicializado em 1.

# # Loop de verificação de divisores: Um loop while é utilizado para iterar através de todos os números até o 
# # próprio número (Divisor <= Numero). Dentro deste loop:

# # Se o resto da divisão de Numero por Divisor for zero (Numero % Divisor == 0), significa que Divisor é 
#         um divisor 
# # de Numero, então incrementamos ContadorDeDivisores.
# # Incrementamos o Divisor em cada iteração para verificar o próximo número como divisor.
# # Verificação final: Após o término do loop, verificamos se ContadorDeDivisores é maior que 2. Se for, 
# # o número não é primo e uma mensagem correspondente é exibida. Caso contrário, o número é primo e uma 
# # mensagem indicando isso é mostrada.

# # Este código foi simplificado para eliminar redundâncias e corrigir a lógica de verificação dos divisores. 
# # Ele agora verifica corretamente se um número fornecido pelo usuário é primo, conforme as definições 
#         matemáticas padrão de números primos.
i = 2
while(True):
    num = int(input("Digite um numero inteiro: "))
    
    if(num > 3):
        while(True):
            if(num % 2 == 0 or num % 3 == 0):
                print(f"Numero não é primo")
                break
            else:
                print("Numero Primo")
                break
    elif(num == 0):
        print("O numero é 0, por favor digite outro numero")
    elif(num == 1):
        print("O numero é 1, por favor digite outro numero")
    elif(num == 2):
        print("O numero é primo")
    elif(num == 3):
        print("O numero é primo")
    else:
        print("O numero é negativo, por favor digite um numero positivo")