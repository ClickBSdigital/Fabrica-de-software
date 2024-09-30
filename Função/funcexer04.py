# Escreva um programa, com uma função
# que necessite de um argumento. A função
# retornar o valor de caractere ‘P’, se seu
# argumento for positivo, e ‘N’, se seu argumento
# for zero ou negativo.

def num_dig(numero):
    
    if numero <= 0:
        return "TÁ MALOCO!!!! **N**"
    # elif numero >= 1
    #     return True
    else: 
        return "TÁ FILÉ!!!! **P**"
print(f"O NÚMERO DIGITATO: ", num_dig(2))