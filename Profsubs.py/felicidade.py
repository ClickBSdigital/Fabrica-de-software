'''
Crie um programa que receba a palavra
FELICIDADE e imprima a posição de cada letra da
palavra e informe qual letra está sendo impressa
na posição x. Após imprima a mensagem que o
programa foi finalizado. Exemplo:
'''
# letra = "FELICIDADE"
# i = 0
# while(1 < 10):
#     print(f"posição {i} da lista {letra}")
#     i =+ 1
# print("programa finalizado.")

palavra = input("Digite uma palavra: ")

print("Posição de cada letra")
for i, letra, in enumerate(palavra):
    print("posição {}: {}".format(i,letra))
print("O programa foi finalizado.")