horas_trab = float(input("Digite quantidade de horas trabalhadas: "))
hora = 40.50
imposto = 11
salario = 2500.00
total_horas = horas_trab * hora
desconto_hora = hora * imposto/100
total_desconto = desconto_hora * horas_trab

if total_horas > salario:
    total = total_desconto * horas_trab
    print(f"O valor so salário é: ${total}")
else:
    total_horas <= salario
    print(f"O valor so salário é: ${total_horas}")

