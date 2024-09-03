valor_hora_trabalho = float(input("Digite o valor da hora trabalhada: $ "))
horas_trabalhada_mes = float(input("Digite o número de horas trabalhadas no mês: "))

valor_ser_pago = valor_hora_trabalho * horas_trabalhada_mes
acrecimo = valor_ser_pago * 0.10

valor_total = valor_ser_pago + acrecimo

print("O valor a ser pago ao funcionário é de: $", valor_total )