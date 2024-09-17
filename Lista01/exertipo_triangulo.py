# Solicita ao usuário que insira os comprimentos dos lados do triângulo
lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

# Verifica se é um triângulo válido
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Verifica se é um triângulo equilátero (todos os lados são iguais)
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    # Verifica se é um triângulo isósceles (dois lados são iguais)
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles.")
    # Se não é equilátero nem isósceles, então é escaleno (todos os lados são diferentes)
    else:
        print("O triângulo é escaleno.")
else:
    print("As medidas fornecidas não formam um triângulo.")