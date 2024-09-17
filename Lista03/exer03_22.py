# 22. Escreva um programa que permita a qualquer aluno introduzir, 
# pelo teclado, uma sequência de 
# notas (válidas no intervalo de 0 a 10) e que mostre na tela, 
# como resultado, a correspondente 
# média aritmética. O número de notas com que o aluno pretenda 
# efetuar o cálculo não
# fornecido ao programa, o qual terminará quando for introduzido 
# um valor que não seja válido
# como nota de aprovação.
# Inicializa variáveis para o cálculo da média
soma_notas = 0
contador_notas = 0

while True:
    # Solicita ao usuário que insira uma nota
    nota = float(input("Digite uma nota (entre 0 e 10, ou um valor inválido para terminar): "))

    # Verifica se a nota é válida (entre 0 e 10)
    if 0 <= nota <= 10:
        soma_notas += nota
        contador_notas += 1
    else:
        # Se a nota for inválida, termina o loop
        break

# Calcula a média aritmética se pelo menos uma nota válida foi inserida
if contador_notas > 0:
    media = soma_notas / contador_notas
    print(f"A média aritmética das notas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
