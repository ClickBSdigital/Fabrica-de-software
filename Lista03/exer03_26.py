# 26. Elabore um algoritmo para fazer cálculo de potenciação. 
# Ou seja, x^y. (Exemplo: 3^4 = 3 x 3 x 3 x 3). 
# Seu algoritmo deverá solicitar que o usuário entre 
# com o valor da base (x) e do expoente (y) 
# e apresentar o resultado do cálculo sem utilizar 
# os operadores (por exemplo **). 
# Para resolver o problema utilize estrutura de repetição.
flag = True

while(flag):
    try:
        base = int(input("Digite o valor da Base: "))
        expoente = int(input("Digite o valor do Expoente: "))
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        continue

    resultado = 0
    if(expoente == 0):
        print("O resultado é: 1")
    elif(expoente == 1):
        print(f"O resultado é: {base}")
    else:
        resultado = base ** expoente
        print(f"O resultado é: {resultado}")
    
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        flag = False