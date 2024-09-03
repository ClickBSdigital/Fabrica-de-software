#exer : 01 = FAÇA UM ALGORITIMO QUE RECEBA UM NÚMERO E APRESENTE  A TABUADA DO MESMO NO FINAL
# num = int(input("Dirite um numero: "))
# i = 0
# while (num < 10):
#     num = num + 1
#     print(f"{i} x {num} = {i * num}")

numero = int(input("Digite o numero: "))
for i in range (1 , 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")