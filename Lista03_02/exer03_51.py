# 51. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de 
# código. Os códigos utilizados são:
# 1 , 2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2-
# João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# • O total de votos para cada candidato;
# • O total de votos nulos;
# • O total de votos em branco;
# • A percentagem de votos nulos sobre o total de votos;
# • A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de 
# votos tem-se o valor zero
candidato1 = []
candidato2 = []
candidato3 = []
candidato4 = []
votosNulos = 0
votosBrancos = 0

while(True):
    print("-(Opção 1) Candidato1 \n-(Opção 2) Candidato2 \n-(Opção 3) Candidato3 \n-(Opção 4) Candidato4 \n-(Opção 5) Voto Nulo \n-(Opção 6) Voto em Branco \n-(Opção 0) Finalizar \n")
    voto = 1

    opcaoCandidato = int(input("Digite seu voto: "))

    if(opcaoCandidato == 1):
        candidato1.append(voto)
        print("Voto para o candidato 1\n")

    elif(opcaoCandidato == 2):
        candidato2.append(voto)
        print("Voto para o candidato 2\n")

    elif(opcaoCandidato == 3):
        candidato3.append(voto)
        print("Voto para o candidato 3\n")

    elif(opcaoCandidato == 4):
        candidato4.append(voto)
        print("Voto para o candidato 4\n")

    elif(opcaoCandidato == 5):
        votosNulos += 1
        print("Voto Nulo\n")

    elif(opcaoCandidato == 6):
        votosBrancos += 1
        print("Voto em branco\n")

    elif(opcaoCandidato == 0):
        print("Votação finalizada\n")
        break

    else:
        print("Opção inválida\n")

print(f"Votos para o candidato 1: {sum(candidato1)}")
print(f"Votos para o candidato 2: {sum(candidato2)}")
print(f"Votos para o candidato 3: {sum(candidato3)}")
print(f"Votos para o candidato 4: {sum(candidato4)}")

print(f"Votos nulos: {votosNulos}")
print(f"Votos brancos: {votosBrancos}")