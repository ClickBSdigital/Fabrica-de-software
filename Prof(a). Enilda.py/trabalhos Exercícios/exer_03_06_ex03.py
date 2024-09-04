# Faça um algoritmo que mostre um Menu com opções de um cardápio 
# de restaurante para uma pessoa (Coloque no mínimo 5 opções e máximo 
# 10 opções de cardápio. Ex: Bife acebolado R$15,00; Lasanha R$25,00).
# A pessoa vai escolher o prato desejado e após escolher o prato, o algoritmo 
# deverá fazer a seguinte pergunta ao usuário, “Aceita pagar a gorjeta do 
# garçom 10% sobre o valor do prato”. Se o usuário aceitar, mostrar o valor 
# final (valor do prato + 10%), caso contrário, mostrar o valor final (somente o valor do prato). 
print("******CONFIRA NOSSO CARDÁPIO**********")
print("===================================\n")
print("Opção 01 = Bife acebolado = R$15,00")
print("Opção 02 =Lasanha = R$25,00")
print("Opção 03 =Estrogonofe = R$35,00")
print("Opção 04 =Prato do dia = R$20,00")
print("Opção 05 =Frango a passarinho = R$15,00")
print("Opção 06 =Parmediana de frango = R$35,00")
print("Opção 07 =Parmediana de carne = $35,00")
print("\n===================================")

opcao01 = 15.00
opcao02 = 25.00
opcao03 = 35.00
opcao04 = 20.00
opcao05 = 15.00
opcao06 = 35.00
opcao07 = 35.00
gorgeta = 10


soma = 0
i = 0
mais = 's'

while mais == 's':

    carrinho = input("Digite a sua escolha do cardápio (1/2/3/4/5/6/7): ")
 
    if carrinho == '1' :
        i = opcao01
   
    elif carrinho == '2':
        i = opcao02
   
    elif carrinho == '3':
        i = opcao03
   
    elif carrinho == '4':
        i = opcao04
   
    elif carrinho == '5':
        i = opcao05
   
    elif carrinho == '6':
        i = opcao06

    elif carrinho == '7':
        i = opcao07

    soma = soma + i
    mais = input("Você quer continuar a adicionar mais itens? (s/n): ")

print(f"O valor total da sua conta é: R${soma}")

print("Aceita pagar a gorjeta do garçom sobre o valor do prato?")
gorgeta_sim = input("\nDigite S - para sim ou N para não.: ")

if gorgeta_sim == 's' or gorgeta_sim == 'S':
    soma_gor = soma * gorgeta/100
    valor_total = soma + soma_gor
    print("caiu if",valor_total)
else:
    print("caiu no else",soma)


# prato = input("Digite a opção do prato (1/2/3/4/5/6/7): ")

# if prato == '1':
#     total = opcao01 
# elif prato == '2':
#     total = opcao02 
# elif prato == '3':
#     total = opcao03
# elif prato == '4':
#     total = opcao04 
# elif prato == '5':
#     total = opcao05
# elif prato == '6':
#     total = opcao06 
# elif prato == '7':
#     total = opcao07



#print("Aceita pagar a gorjeta do garçom sobre o valor do prato?")
# gorgeta_sim = input("\nDigite S - para sim ou N para não.: ")



# valores = [15.00, 25.00, 35.00, 20.00, 15.00, 35.00, 35.00] 

# valores[]


# if gorgeta_sim == "S" or gorgeta_sim == "s":
#     add_gorgeta =  opcao + gorgeta/100

# periodo = input("Digite o turno que estuda M - Matutino ou V - Vespertino ou N - Noturno.:")

# if periodo == "M" or periodo == "m":
#     print("Bom dia!!")
# elif periodo == "V" or periodo == "v":
#     print("Boa tarde!!")
# elif periodo == "N" or periodo == "n":
#     print("Boa tarde!!")
# else:
#     print("VOCÊ NÃO ESTUDA")


#     nome = input("Digite o nome do produto: ")
# valor_entrada = float(input("digite o valor de entrada: $"))
# acressimo01 = 45
# acressimo02 = 30

# total_da_venda01 = valor_entrada * acressimo01/100 
# venda_final_01 = valor_entrada + total_da_venda01

# total_da_venda02 = valor_entrada * acressimo02/100 
# venda_final_02 = valor_entrada + total_da_venda02

# if valor_entrada < 50:
#     print(f"O produto: {nome} tem o valor a venda de: ${venda_final_01}")
# else:
#     print(f"O produto: {nome} tem o valor a venda de: ${venda_final_02}")