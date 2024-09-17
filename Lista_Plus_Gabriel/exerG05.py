# Escreva um programa que imprima os primeiros 10 números da sequência de
# Fibonacci utilizando um loop while

lista = [1,]

i = 1
while(i <= 100):
    lista.append(i)
    i+=1

print(lista)
print(lista[8])
x = lista[8] == (lista[7] + lista[6])
print(x)

# i = 0
# fibo = []
# while(i < len(lista)):
#     print(lista[i])
#     if(lista[i] == lista[i-1] + lista[i-2]):
#         fibo.append(i)
#         i+=1
#     else:
#         i+=1
    
# print(fibo)
