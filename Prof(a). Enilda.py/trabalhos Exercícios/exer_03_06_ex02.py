# Um algoritmo em que usuário escolha uma opção de acordo com o último número da placa do carro 
# e mostre uma mensagem dizendo em que dia da semana não poderá circular. 
# 0 - 2 “Não Circular 2ª Feira” 
# 3 - 4 “Não Circular 3ª Feira” 
# 5 - 6 “Não Circular 4ª Feira” 
# 6 - 7 “Não Circular 5ª Feira” 
# 8 - 9 “Não Circular 6ª Feira” 

numero = int(input("Digite o último número da placa do carro: "))
opcao01 = ("0 - 2 “Não Circular 2ª Feira”")
opcao02 = ("3 - 4 “Não Circular 3ª Feira”")
opcao03 = ("5 - 6 “Não Circular 4ª Feira”")
opcao04 = ("6 - 7 “Não Circular 5ª Feira”")
opcao05 = ("8 - 9 “Não Circular 6ª Feira”")

if numero >= 0 and numero <= 2:
    print(f"\nSua placa tem o final: {numero}, e o veredito é: {opcao01}")
elif numero >= 3 and numero <= 4:
    print(f"\nSua placa tem o final: {numero}, e o veredito é: {opcao02}")
elif numero >= 5 and numero <= 6:
    print(f"\nSua placa tem o final: {numero}, e o veredito é: {opcao03}")
elif numero >= 6 and numero <= 7:
    print(f"\nSua placa tem o final: {numero}, e o veredito é: {opcao04}")
elif numero >= 8 and numero <= 9:
    print(f"\nSua placa tem o final: {numero}, e o veredito é: {opcao05}")
else:
    print("\n**OPÇÃO INVÁLIDA**")