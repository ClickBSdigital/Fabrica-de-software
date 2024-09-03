#  Crie um programa que peça ao usuário para digitar um número e imprima se 
# esse número é par ou ímpar. O programa deve continuar pedindo números 
# até que o usuário digite 0 para sair.
print("Bem Vindo!")

while(True):
    num = int(input("Digite um numero ou digite '0' para sair: "))

    if(num == 0):
        print("Numero Impar")
        break
    elif(num % 2 != 0):
        print("Numero Impar")
    else:
        print("Numero par")
        
print("Programa Finalizado")