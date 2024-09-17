# 21. Crie um programa que receba dois números. Calcule e mostre:
# • a soma dos números pares desse intervalo de números, incluindo 
# os números digitados;
# • a multiplicação dos números ímpares desse intervalo, incluindo 
# os digitados;
num01 = int(input("Digite um numero: "))
num02 = int(input("Digite outro numero: "))

menor = min(num01, num02)
maior = max(num01, num02)

soma = 0
mult = 1 

cont = menor

par = 0
impar = 0



while cont <= maior:
    if cont % 2 == 0:
        soma += cont
        par = 1
    else:
        mult *= cont
        impar = 1
    cont += 1
    
print("A quantidade de números pares: ",par)
print("A soma dos números pares é : ", soma)

print("A quantidade de numeros mpares: ", impar)
print("A multiplicação dos números ímpares é: ", mult)  