#####tempo em minutos

####CRIE UMA FUNÇÃO QUE CALCULE O PREÇO EM REAIS
#### DO CONSUMO MENSAL DE AGUA EM LITROS DE UMA PESSOA
def calcula_kwh(pot,tempo):
    consumo = (pot * (tempo/60) ) / 1000
    return consumo

passarroupa = calcula_kwh(2200,180)
print(f'Consumo: {passarroupa:.2f} KWh')

preco = 0.67 * passarroupa

print("VALOR do banho do Eduardo: ",preco)

