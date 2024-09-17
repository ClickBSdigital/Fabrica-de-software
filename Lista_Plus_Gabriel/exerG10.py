# Faça um programa que simule uma máquina registradora básica. O 
# programa deve solicitar ao usuário que digite o preço de vários itens. Quando 
# o usuário terminar de digitar os preços, o programa deve calcular e imprimir o 
# total da compra. Além disso, o programa deve perguntar se o usuário deseja 
# continuar adicionando itens à compra


print("Bem Vindo!")

lista = []

while(True):
    num = int(input("Digite o valor do produto: "))
    
    lista.append(num)

    opcao = input("Deseja continuar? S/N")

    if(opcao == 'n' or opcao == 'N'):
        break

soma = sum(lista)

print(f"O valor total do produto é R$:{soma}")