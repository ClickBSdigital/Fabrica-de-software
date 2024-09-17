# 33. Escreva um algoritmo que leia um vetor com 10 posições de números inteiros. Em seguida 
# receba um novo valor do usuário e verifique se este valor se encontra no vetor.
lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
i = 0 

while(True):
    num = int(input("Digite um numero para a verificação: "))

    while(i < len(lista)):
        if(lista[i] == num):
            print(f"O seu numero está na lista, na posição {i}")
            break
        else:
            print(f"Posição {i} verificaada... Numero não encontrado")
        i += 1