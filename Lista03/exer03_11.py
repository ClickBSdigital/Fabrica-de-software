# Considerando o intervalo de 0 a 100. Crie um programa que 
# calcule e mostre a soma dos 50 primeiros números pares
# num = 2 
# soma = 0
# count = 0
# while count < 50:
#     soma += num
#     num += 2
#     count += 1
# print(soma)
cont = 0
lista = []
while cont <= 100:
    cont = cont + 1
    if cont % 2 == 0:
        lista.append(cont)
print(lista)
print(sum(lista))