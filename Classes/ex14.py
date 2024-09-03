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

# # ========================================.

# O código fornecido calcula o consumo de energia elétrica (em kWh) de um aparelho com base na sua potência (em watts) e no tempo de uso (em minutos). A seguir, o código também calcula o custo do consumo de energia baseado em um preço fixo por kWh.

# Explicação do Código:
# Função calcula_kwh(pot, tempo):

# Entrada:
# pot: Potência do aparelho em watts.
# tempo: Tempo de uso do aparelho em minutos.
# Processamento:
# A fórmula para calcular o consumo em kWh é:
# consumo
# =
# pot
# ×
# (
# tempo
# 60
# )
# 1000
# consumo= 
# 1000
# pot×( 
# 60
# tempo
# ​
#  )
# ​
 
# A fórmula converte a potência de watts para kilowatts (dividindo por 1000) e o tempo de minutos para horas (dividindo por 60).
# Saída: Retorna o consumo de energia em kWh.
# Cálculo do Consumo de Energia:

# A função calcula_kwh() é chamada com os parâmetros:
# Potência (2200 watts) e
# Tempo (180 minutos), que é o tempo de uso do ferro de passar roupa.
# O consumo resultante é armazenado na variável passarroupa.
# Cálculo do Preço do Consumo:

# O custo do consumo é calculado multiplicando o consumo (passarroupa) por uma tarifa de energia elétrica de 0.67 reais por kWh.
# Exibição dos Resultados:

# O consumo de energia é formatado e exibido com duas casas decimais.
# O valor total do consumo de energia também é exibido.
# Código:
# python
# Copiar código
# def calcula_kwh(pot, tempo):
#     consumo = (pot * (tempo / 60)) / 1000
#     return consumo

# # Cálculo do consumo de energia do ferro de passar roupa
# passarroupa = calcula_kwh(2200, 180)
# print(f'Consumo: {passarroupa:.2f} KWh')

# # Cálculo do preço do consumo de energia
# preco = 0.67 * passarroupa

# # Exibição do preço total
# print("VALOR do banho do Eduardo: ", preco)
# Saída Esperada:
# O consumo de energia em kWh será calculado para um ferro de passar roupa com potência de 2200 watts utilizado por 180 minutos (3 horas).

# Consumo:
# 2200
# ×
# (
# 180
# 60
# )
# 1000
# =
# 2200
# ×
# 3
# 1000
# =
# 6.6
#  
# kWh
# 1000
# 2200×( 
# 60
# 180
# ​
#  )
# ​
#  = 
# 1000
# 2200×3
# ​
#  =6.6kWh
# O consumo resultante será 6.60 kWh.
# O custo será calculado como:

# 6.6
# ×
# 0.67
# =
# 4.422
#  
# reais
# 6.6×0.67=4.422reais
# Portanto, a saída será:

# vbnet
# Copiar código
# Consumo: 6.60 KWh
# VALOR do banho do Eduardo:  4.422
# Observações:
# O nome da variável preco sugere que o cálculo se refere ao "banho do Eduardo", mas parece que o código está calculando o custo do uso do ferro de passar roupa. Se o cálculo deveria ser para outro aparelho, o nome das variáveis e o valor da potência podem precisar ser ajustados.
# Para garantir que os valores são sempre exibidos com duas casas decimais, podes formatar o valor do preço como:
# python
# Copiar código
# print(f"VALOR do banho do Eduardo: {preco:.2f}")
# Isso exibirá o custo como 4.42 em vez de 4.422.