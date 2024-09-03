def valorpadrao(quant,valor):
    lista = []
    for i in range(quant):
        lista.append(int(valor))
    return lista

a = int(input("DIGITE O TAMANHO DA LISTA: "))
b = input("DIGITE O VALOR PADRAO: ")

result = valorpadrao(a,b)
print(result)