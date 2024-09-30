# Crie uma função para calcular a
# exponenciação, que necessite dois argumentos
# e apresente como resultado a potência. Sendo
# base elevado ao expoente.
def pot(x,y):
    res = x ** y
    return res
print("CALCULE POTÊNCIA!!!")
base = int(input("DIGITE A BASE: "))
exp = int(input("DIGITE O EXPOENTE: "))

x = pot(base,exp)
print(x)