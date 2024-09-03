#solicite um caractere
caractere = input("digite um caractere: ")

#verificar se o caractere é vogal
if caractere.lower() in 'aeiou':
    print(f"O caractere {caractere} é uma vogal!")
#verifica se o caractere é uma consoante
elif caractere.isalpha():
    print(f"O caractere {caractere} é uma consoante!")
#se o caractere não é uma letra do alfabeto
else:
    print(f" o caractere {caractere} não é uma letra do alfabeto!")