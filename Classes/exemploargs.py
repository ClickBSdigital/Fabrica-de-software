####OBBRIGATORIO PASSAR OS 4 ARGS
def soma(x,y,z=0,t=0):
    soma = x + y + z + t
    return soma

####ARGUMENTO COM VALOR DEFAULT
# res = soma(45,46,35)
# print(res)

####ARGUMENTOS NAO ESPECIFICADOS
def soma_args(*args):
    return sum(args)

x = soma_args(12,12,24,48,96,128)
print(x)