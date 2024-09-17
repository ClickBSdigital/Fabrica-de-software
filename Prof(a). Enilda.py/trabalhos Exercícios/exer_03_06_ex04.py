# Calcular quantidade de painéis solares para uma residência. 
# Para implementar as quatro demandas acima, 
# você deverá listar os requisitos necessários para o desenvolvimento, 
# elaborar o diagrama de caso de uso 
# e por fim o algoritmo utilizando o Python. 

#=========================
# Um ponto básico para determinar quantos painéis solares são precisos 
# para alimentar a sua casa é saber qual é a demanda de consumo da 
# sua família. Afinal, um imóvel que gasta 250 kWh por mês precisará 
# de um número de painéis. Já uma casa que gaste 300 kWh por mês, 
# precisará de outra quantidade.
# ========================
# Como calcular a quantidade de placas solares para uma residência?
# Para fazer isso, divida a capacidade do sistema pelo número de 
# watts produzidos por cada placa solar. Isso resultará no número 
# de placas solares necessárias para atender às suas necessidades 
# de energia.
#https://www.aldo.com.br/blog/como-fazer-o-calculo-do-sistema-fotovoltaico-com-eficiencia/#:~:text=Considere%20que%20cada%20painel%20a,44%2C28%20kWh%2Fm%C3%AAs.
# Dessa forma, o cálculo do sistema fotovoltaico se inicia com 
# o levantamento do consumo médio em KWh dos últimos 12 meses do 
# local onde o sistema será instalado.

consumo = float(input("Digite o valor do consumo kWh/mês da sua residencia: "))
painel = 410
irradiacao_solar = 4.5
perda = 0.20
energia_gerada_painel = 1.476
calculo_mensal = energia_gerada_painel * 30
nunero_painel = consumo / calculo_mensal
print(f"Sendo assim, para suprir a demanda de consumo de {consumo}kWh/mês.")
print(f"Pelo menos, {nunero_painel} painéis no sistema fotovoltaico")