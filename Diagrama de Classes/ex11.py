def imprimir(lista):
    cont = 1
    for item in lista:
        print(f' {cont}, {item}')
        cont += 1

def imprimircomwhile(lista):
    i = 0
    while i < len(lista):
        print(f'\n {i+1}, {lista[i]}')
        i += 1

frutas = ['ABACAXI','MAMAO','MELANCIA','PERA','UVA']
imprimir(frutas)
imprimircomwhile(frutas)