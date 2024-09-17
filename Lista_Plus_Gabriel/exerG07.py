# Escreva um programa que simule um jogo de dados simples. O programa
# deve pedir ao usuário para jogar um dado (gerar um número aleatório de 1 a
# 6). O usuário pode continuar jogando quantas vezes quiser. O programa deve
# imprimir o resultado de cada lançamento e perguntar se o usuário deseja
# lançar o dado novamente.

import random

dado = [1, 2, 3, 4, 5, 6]
while(True):
    jogo = input("Deseja jogar o dado? S/N")

    if(jogo == 'N' or jogo == 'n'):
        break
    else:
        numAleatorio = random.choice(dado)
        print(f"O dado sorteou: {numAleatorio}")
print("Jogo Finalizado!!!")