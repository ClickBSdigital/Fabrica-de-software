try:
    numero = int(input("Digte um numero: "))
except:
        print("Entrada inválida!!!!!")
if numero >= 10:
    print(f"O número {numero} é mairo que 10.")
else:
    print(f"O número {numero} é menor que 10")