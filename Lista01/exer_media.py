#programa auto escola RapidCNH
idade = 18
test_psicotecnico = "APROVADO"
prova_teórico = 8.5

if(idade >= 18):
    print("Tem idade para tirar CNH")
    if(test_psicotecnico == "APROVADO" and prova_teórico >= 7.0):
        print("Está apto a aulas práticas!")
    elif(test_psicotecnico == "REPROVADO" or prova_teórico < 7.0):
        print("Não está apto para fazer as aulas práticas")
else:
    print("Não tem idade para tirar CNH")