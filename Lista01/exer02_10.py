numero = int(input("Digite um número inteiro: "))

if numero >=0:
    quadrado = (numero + numero) * 2
    raiz = numero ** 2
    print(f"O {numero} ao quadrodo é: {quadrado} e a raiz quadrada é: {raiz}")
else:
    print("Numero inválido")