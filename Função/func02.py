def soma(x,y):
    res = x + y
    print(f"RESULTADO; {res}")

def somar(x,y):
    res = x + y
    return res

soma(10,12)
x = somar(22,22)
print(x)

print(soma(25,25))

if somar(50,51) > 100:
    print("SOMA MAIOR QUE 100")
