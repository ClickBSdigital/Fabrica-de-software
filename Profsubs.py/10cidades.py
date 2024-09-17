# exer: 02 = Faça um algoritmo que inicialize com uma lista 
# de 10 cidades que deseja conhecer e apresente em 
# ordem decrescente (da ùltima para a primeira);
# cidades = ["BAURU", "MURUARAMA", "TORRES", "PARANAGUA", "UBIRATAN", "PASSOS","DUARTINA", "PITANGA", "PEREQUE", "SALES"]
# cont = len(cidade) - 1
# while cont >= 0:
#     print(cidades[cont])
#     cont -= 1

cidades = ["Campo Grande", "Itu", "Terenos","Rio de janeiro"]
num_letras_por_cidade = {}
# contando o numero da letra de cada cidade e armazenando no vetor num_letras_por_cidade
for cidade in cidades:
    num_letras = 0
    for letra in cidade:
        num_letras += 1
    num_letras_por_cidade[cidade] = num_letras

cidades_ordem_crescente = []
while num_letras_por_cidade:
    maior_num_letras = -1
    cidade_maior_num_letras = None
    for cidade, num_letras in num_letras_por_cidade.items():
        if num_letras > maior_num_letras:
            maior_num_letras = num_letras
            cidade_maior_num_letras = cidade
    cidades_ordem_crescente.append(cidade_maior_num_letras)
    del num_letras_por_cidade[cidade_maior_num_letras]

for cidade in cidades_ordem_crescente:
    print(cidade)