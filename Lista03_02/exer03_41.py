# 41. Crie um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos 
# pelo usuário via teclado. O programa fica pedindo estes valores e calculando até que o usuário
# entre com um valor para resistência igual a zero.
while(True):
    r1 = int(input("Digite o valor de R1: "))
    r2 = int(input("Digite o valor de R2: "))

    r = (r1 * r2) / (r1 + r2)

    if(r == 0):
        print(f"O valor de R: {r} \nPrograma finalizado")
        break
    else:
        print(f"O valor de R: {r}")