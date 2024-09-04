# Um algoritmo para uma calculadora, o usuário digita o primeiro número, 
# a operação que deseja executar e o segundo número. Dependendo do que o usuário informar como operador, 
# o algoritmo executará um cálculo diferente (soma, subtração, multiplicação ou divisão).  
def adicao (x, y): 
    return  x + y 

def subtracao (x, y): 
    return x - y
def multiplicacao(x, y): 
    return x * y 

def divisao(x, y): 
    return x // y

print('**********Python Calculator**********') 

print("\nSelecione o número da opção desejada: \n") 

print("1 - Soma") 
print("2 - Subtração") 
print("3 - Multiplicação") 
print("4 - Divisão")

opcao = int(input("\nDigite a opção (1/2/3/4): "))

if opcao <= 0 or opcao > 4:
    print("\nOpção inválida!\n")
    exit(0)

numero01 = int(input("\nDigite o primeiro número: "))
numero02 = int(input("\nDigite o segundo número: "))

if opcao == 1:
    print(numero01, "+", numero02, "=", adicao(numero01, numero02))
elif opcao == 2:
    print(numero01, "-", numero02, "=", subtracao(numero01, numero02))
elif opcao == 3:
    print(numero01, "*", numero02, "=", multiplicacao(numero01, numero02))
elif opcao == 4:
    print(numero01, "/", numero02, "=", divisao(numero01, numero02))