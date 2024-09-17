# 35. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
# Imprima as consoantes.
palavra = input("Escreva uma palavra: ")
plv = str.lower(palavra)

p = 0
for i in palavra:
    if(plv[p] == 'a' or plv[p] =='e' or plv[p] == 'i' or plv[p] == 'o' or plv[p] == 'u'):
        print(f"A letra {plv[p]} é vogal")
    else:
        print(f"A letra {plv[p]} é consoante")
    p += 1