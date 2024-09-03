# i = 0
# while (i > 5):
#     print(i)
#     i = + 1

#código Reverso
# x = 10
# while not ( x == 0):
#     x = x-1
#     if x % 2 != 0:
#         print (x)

#O que faz o programa abaixo?
# terminou = False
# p = i = 0
# while (not terminou):
#     n = int(input("Digite um numero, ou zero para terminar: "))
#     if n == 0:
#         terminou = True
#     else:
#         if n % 2 == 0:
#             p = p + 1
#         else:
#             i = i + 1

# print ("P = ", p)
# print ("I = ", i)


# frutas = ["maça", "banana", "tomate", "abacaxi"]

# for item in frutas:
#     print(item)

#ITERAR UM LISTA, SIGNIFICA PERCORRER A LISTA
    
# frutas = ["Pera", "Banana", "Laranja","Tomate","Abacaxi", "Kiui"]

# cont = 0
# while cont > len(frutas):
#     print(frutas[cont])
#     cont = cont + 1

# for item in frutas:
#     print(item)

# for i in range(50):
#     print(i)

# for i in range(1, 51):
#     print(i)

#aclessentar um numero quer deiser "passo"
# for i in range(1, 51, 2):
#     print(i)

# for i in range(100):
#     print(i*2)

# for i in range(10):
#     print(f"{i} x 2 = {i*2}")

#FOR - CONTINUE
# frutas

#exer : 01 = FAÇA UM ALGORITIMO QUE RECEBA UM NÚMERO E APRESENTE  A TABUADA DO MESMO NO FINAL
# num = int(input("Dirite um numero: "))
# i = 0
# while (num < 10):
#     num = num + 1
#     print(f"{i} x {num} = {i * num}")


#exer: 02 = Faça um algoritmo que inicialize com uma lista 
# de 10 cidades que deseja conhecer e apresente em 
# ordem decrescente (da ùltima para a primeira);
# cidade = ["BAURU", "MURUARAMA", "TORRES", "PARANAGUA", "UBIRATAN", "PASSOS","DUARTINA", "PITANGA", "PEREQUE", "SALES"]
# cont = len(cidade) - 1
# while cont >= 0:
#     print(cidade[cont])
#     cont -= 1

#Exer: 03 Faça um algoritmo que receba 10 nomes 
#em uma lista e ao final apresenta
#todos os nomes recevidos
nome01 = input("Digite um nome: ")
nome02 = input("Digite Outro nome: ")
nome03 = input("Digite Outro nome: ")
nome04 = input("Digite Outro nome: ")
nome05 = input("Digite Outro nome: ")
nome06 = input("Digite Outro nome: ")
nome07 = input("Digite Outro nome: ")
nome08 = input("Digite Outro nome: ")
nome09 = input("Digite Outro nome: ")
nome10 = input("Digite Outro nome: ")
lista =  []
lista.append(nome01)
lista.append(nome02)
lista.append(nome03)
lista.append(nome04)
lista.append(nome05)
lista.append(nome06)
lista.append(nome07)
lista.append(nome08)
lista.append(nome09)
lista.append(nome10)
print("Resultados dos nomes da lista é: ")
cont = len(lista) - 1
while cont >= 0:
    print(lista[cont])
    cont -= 1
# print(lista)

#Exer: 04 = Faça um algoritimo que receba o número
#de avaliação do estudante que será (ulilizado como 
#contador), appós receba as notas e apresente a média
#do estudante

# num01 = float(input("Digite a nota: "))
# num02 = float(input("Digite outra nota: "))
# num03 = float(input("Digite outra nota: "))

