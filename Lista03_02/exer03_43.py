# 43. Faça um programa que gera um número aleatório de 1 a 100. O usuário deve tentar acertar 
# qual o número foi gerado, a cada tentativa o programa deverá informar se o chute e menor ou 
# maior que o número gerado. O programa acaba quando o usuário acerta o número gerado. O 
# programa deve informar em quantas tentativas o número foi descoberto.
import random 

numAleatorio = random.randint(1,100)

while(True):
    userChute = int(input("Advinhe o numero aleatório: "))

    if(userChute > numAleatorio):
        print("o numero aleatório é menor, tente novamente")
    elif(userChute < numAleatorio):
        print("o numero aleatório é maior, tente novamente")
    else:
        print("Você acertou o numero !!!!")
        print(numAleatorio)