#temporisador  do microondas
try:
    contador = int(input("Digite o tempo no microondas: "))
except:
    print("ENTRADA INVÁLIDA!!!!!")
while (contador > 0):
    print(contador)
    contador = contador - 1

print("Rango Pronto!!!")