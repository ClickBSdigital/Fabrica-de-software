# 47. Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 
# números naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez primeiros números 
# naturais e,
# 12 + 22 + ... + 102 = 385
# O quadrado da soma dos dez primeiros números naturais é,
# (1 + 2 + ... + 10)2 = 552 = 3025
# A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da 
# soma e 3025-385 = 2640.
listaSomaQuadrado = []
listaQuadradoSoma = []


x = 1
i = 0
while(i < 100):
    somaQuadrado = x ** 2
    listaSomaQuadrado.append(somaQuadrado)
    x += 1
    i += 1
print(sum(listaSomaQuadrado))


i = 0
x = 0
while(i < 100):
    x += 1
    listaQuadradoSoma.append(x)
    i+= 1


somaLista = sum(listaQuadradoSoma)
somaLista = somaLista**2

print(somaLista)