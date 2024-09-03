# 40. Faça um programa que some os números ímpares contidos em um intervalo definido pelo 
# usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa 
# deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um 
# intervalo inválido (começando por um valor maior que o valor final) deve ser escrito uma 
# mensagem de erro na tela, “Intervalo de valores invalido” e o programa´ termina. Exemplo de 
# tela de saída:
# Digite o valor inicial e valor final: 5
# 10
# Soma dos ímpares neste intervalo: 21
lista = []
while(True):
    num1 = int(input("Digite um numero inteiro: "))
    num2 = int(input("Digite um numero inteiro maior: "))
    i = 0

    if(num1 >= num2):
        print("Intervalo de valores invalido")
    else:
        while(num1 <= num2):
            if(num1 % 2 != 0):
                lista.append(num1)
                num1 += 1
            else:
                num1 +=1

    print(sum(lista))