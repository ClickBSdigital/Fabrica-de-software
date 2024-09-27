def pot(x,y):
    res = x ** y
    return res

def verifica_idade(idade):
    if idade <= 0:
        return "TÁ MALOCO!!!! NÃO FAZEMOS CALCULO COM BEBES OU PESSOAS NÃO NACISDAS"
    elif idade > 0 and idade > 99:
        return True
    else: 
        return "TÁ MALOCO!!!! NÃO FAZEMOS CALCULO COM CABRAS QUE SÃO LENDAS"
    
def divsao(n1,n2):
    if n1 <= 0:
        return "IMPOSSÍVEL DIVIDIR!!!"

def soma(n1,n2):
    res = n1 + n2
    return res

def mult(n1,n2):
    res = n1 * n2
    return res

# print("CALCULE POTENCIA!!!")
# base = int(input("DIGITE A BASE: "))
# exp = int(input("DIGITE O EXPOENTE: "))

# x = pot(base,exp)
# print(x)

print(verifica_idade(18))
resultado