# Faça um programa que leia números do usuário até que ele digite um número
# negativo. Ao final, o programa deve imprimir o maior número digitado.


flag = True
lista = []

while(flag):
    num = int(input("Digite um numero inteiro para adicionar ou um numero negativo para finalizar: "))

    if(num < 0):
        flag= False
    else:
        lista.append(num)

print(f"O maior numero digitado foi: {max(lista)}")