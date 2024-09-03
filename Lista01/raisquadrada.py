x1 = float(input("Digite  a coodenada  de x do primeiro ponto: \n"))
x2 = float(input("Digite  a coodenada  de x do primeiro ponto: \n"))
y1 = float(input("Digite  a coodenada  de y do primeiro ponto: \n"))
y2 = float(input("Digite  a coodenada  de y do primeiro ponto: \n"))

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2)  ** 0.5

if distancia >= 10:
    print("Longe")
else:
    print("Preto")