# # 44. Crie um programa que apresente um menu de opções para o cálculo das seguintes operações 
# # entre dois números.
# # • adição (opção 1)
# # • subtração (opção 2)
# # • multiplicação (opção 3)
# # • divisão (opção 4).
# # • saída (opção 5)
# O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do 
# resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção
# de saída (opção 5).
def menu(opcao):
    print("-(Opção 1) Adição \n-(Opção 2) Subtração \n-(Opção 3) Multiplicão \n-(Opção 4) divisão \-n(Opção 5) saída ")

def adicao(num1, num2):
    result = num1 + num2
    print(result)

def subtracao(num1, num2):
    result = num1 - num2
    print(result)

def multiplicacao(num1, num2):
    result = num1 * num2
    print(result)

def divisao(num1, num2):
    result = num1 / num2
    print(result)


while(True):
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite um numero: "))
    menu(opcao)
    opcao = int(input("Digite a operação: "))



    if(opcao == 1):
        adicao(num1, num2)

    elif(opcao == 2):
        subtracao(num1, num2)

    elif(opcao == 3):
        multiplicacao(num1, num2)

    elif(opcao == 4):
        divisao(num1, num2)

    elif(opcao == 5):
        break