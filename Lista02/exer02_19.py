numero = int(input("DIGITE UM NUMERO COM 3 DIGITOS"))

if numero < 0:
    print("NUMERO INVÁLIDO")
else:
    aux = str(numero)
    soma = int(aux[0]) + int(aux[1]) + int(aux[2])
    print(soma)