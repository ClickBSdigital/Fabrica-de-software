salario = float(input("Digite o valor do Salário: $"))
emprestimo = float(input("Digite o valor do empréstimo: $"))
prestacao = int(input("Digite o numero de Prestações: ")) 

limete = 0.20 * salario
valor_prestacao = emprestimo / prestacao
valor_aprovado = (salario * valor_prestacao)/100

if valor_prestacao > limete:
    print(f"O valor do empréstimo {emprestimo} não concedido!")
else:
    print(f"Empréstimo Concedido em {prestacao} no valor de {emprestimo}")