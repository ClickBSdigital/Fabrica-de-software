#Exer: 03 Faça um algoritmo que receba 10 nomes 
#em uma lista e ao final apresenta
#todos os nomes recevidos

# nome01 = input("Digite um nome: ")
# nome02 = input("Digite Outro nome: ")
# nome03 = input("Digite Outro nome: ")
# nome04 = input("Digite Outro nome: ")
# nome05 = input("Digite Outro nome: ")
# nome06 = input("Digite Outro nome: ")
# nome07 = input("Digite Outro nome: ")
# nome08 = input("Digite Outro nome: ")
# nome09 = input("Digite Outro nome: ")
# nome10 = input("Digite Outro nome: ")
# lista =  []
# lista.append(nome01)
# lista.append(nome02)
# lista.append(nome03)
# lista.append(nome04)
# lista.append(nome05)
# lista.append(nome06)
# lista.append(nome07)
# lista.append(nome08)
# lista.append(nome09)
# lista.append(nome10)
# print("Resultados dos nomes da lista é: ")
# cont = len(lista) - 1
# while cont >= 0:
#     print(lista[cont])
#     cont -= 1
nomes = []

for i in range(10):
    nome = input("Nome {}:".format(i+1))
    nomes.append(nome)

print("Nome da cidades")
for nome in nomes:
    print(nome)
