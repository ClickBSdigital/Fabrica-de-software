#solicite ao usuário que insira a nota do aluno
nota = float(input("Digite a nota do aluno: "))

#classifica o aluno de acordo com a nota
if nota >= 90:
    print("A - Excelente")
elif nota >= 80:
    print("B - Muito bom")
elif nota >= 70:
    print("C - Bom")
elif nota >= 60:
    print("D - Suficiente")
else:
    print("F - Insuficiente")