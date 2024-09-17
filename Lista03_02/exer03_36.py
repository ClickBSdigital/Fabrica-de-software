# 36. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a 
# média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
aluno1 = []
aluno2 = []
aluno3 = []
aluno4 = []
aluno5 = []
aluno6 = []
aluno7 = []
aluno8 = []
aluno9 = []
aluno10 = []

i = 0
y = 0

while(i <= 40):
    if(i >=0 and i <=4):
        while(y < 4):
            num = int(input(f"digite a nota do aluno 1: "))
            aluno1.append(num)
            y+=1
    elif(i>4 and i <= 8):
        while(y < 8):
            num = int(input(f"digite a nota do aluno 2: "))
            aluno2.append(num)
            y+=1
    elif(i>8 and i<=12):
            num = int(input(f"digite a nota do aluno 3: "))
            aluno3.append(num)
            y+=1
    elif(i>12 and i<=16):
            num = int(input(f"digite a nota do aluno 4: "))
            aluno4.append(num)
            y+=1
    elif(i>16 and i<=20):
            num = int(input(f"digite a nota do aluno 5: "))
            aluno5.append(num)
            y+=1
    elif(i>20 and i<=24):
            num = int(input(f"digite a nota do aluno 6: "))
            aluno6.append(num)
            y+=1
    elif(i>24 and i<=28):
            num = int(input(f"digite a nota do aluno 7: "))
            aluno7.append(num)
            y+=1
    elif(i>28 and i<=32):
            num = int(input(f"digite a nota do aluno 8: "))
            aluno8.append(num)
            y+=1
    elif(i>32 and i<=36):
            num = int(input(f"digite a nota do aluno 9: "))
            aluno9.append(num)
            y+=1
    elif(i>36 and i<=40):
            num = int(input(f"digite a nota do aluno 10: "))
            aluno10.append(num)
            y+=1

    i+= 1


print(f"Nota dos alunos: \nAluno 1:{aluno1} \nAluno 2:{aluno2} \nAluno 3:{aluno3} \nAluno 4:{aluno4} \nAluno 5:{aluno5} \nAluno 6:{aluno6} \nAluno 7:{aluno7} \nAluno 8:{aluno8} \nAluno 9:{aluno9} \nAluno10:{aluno10}")


mediaAluno1 = sum(aluno1) / len(aluno1)
mediaAluno2 = sum(aluno2) / len(aluno2)
mediaAluno3 = sum(aluno3) / len(aluno3)
mediaAluno4 = sum(aluno4) / len(aluno4)
mediaAluno5 = sum(aluno5) / len(aluno5)
mediaAluno6 = sum(aluno6) / len(aluno6)
mediaAluno7 = sum(aluno7) / len(aluno7)
mediaAluno8 = sum(aluno8) / len(aluno8)
mediaAluno9 = sum(aluno9) / len(aluno9)
mediaAluno10 = sum(aluno10) / len(aluno10)
medias = []
medias.append(mediaAluno1, mediaAluno2, mediaAluno3, mediaAluno4, mediaAluno5, mediaAluno6, mediaAluno7, mediaAluno8, mediaAluno9, mediaAluno10)

print(f"A media de cada aluno é \nAluno 1: {mediaAluno1} \nAluno 2: {mediaAluno2} \nAluno 3: {mediaAluno3} \nAluno 4: {mediaAluno4} \nAluno 5: {mediaAluno5} \nAluno 6: {mediaAluno6} \nAluno 7: {mediaAluno7} \nAluno 8: {mediaAluno8} \nAluno 8: {mediaAluno8} \nAluno 10: {mediaAluno10} ", end=',')

i = 0
cont = 0
while(i <= len(medias)):
    if(medias[i] >= 7):
          cont += 1
    i += 1
print(f"{cont} alunos com a media maior ou igual a 7")