'''27. Escreva um algoritmo que leia um valor inicial A e imprima a 
sequência de valores do cálculo do 
Fatorial: A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120'''

a = int(input("Digite um valor: "))
while a > 0:
    print(a)
    a -= 1
    soma = a * a
    print(f"A soma de {a} é: {soma}")