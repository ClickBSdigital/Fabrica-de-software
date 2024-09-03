# Faça um programa que simule o jogo "Adivinha o número". O programa 
# deve gerar um número aleatório entre 1 e 100. Em seguida, o usuário deve 
# tentar adivinhar o número. O programa deve dar dicas se o número fornecido 
# pelo usuário é maior ou menor que o número gerado. O jogo deve continuar 
# até que o usuário acerte o número.

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