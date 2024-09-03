nota01 = float(input("digite a primeira nota do aluno: "))
nota02 = float(input("digite a segunda nota do aluno: "))

media = (nota01 + nota02)/2

if media >= 0.0 and media <= 10.0:
    print(f"A {media} das notas são válidadas!")
else:
    print(f"A {media} das notas são inválidadas!")
    print("Programa Finalizado!!")