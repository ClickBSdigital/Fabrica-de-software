#defina o intervalo específico
inicio_intervalo = 10
fim_intervalo = 20

#solicite ao usuário que insira um numero
numero = int(input("Digite um número: "))

#verifica se o número esta dentro do intervalo específico
if inicio_intervalo <= numero >= fim_intervalo:
    print(f"O número {numero} está dentro do intervalo de {inicio_intervalo} a {fim_intervalo}")
else:
    print(f"O número {numero} não está dentro do intervalo de {inicio_intervalo} a {fim_intervalo}")