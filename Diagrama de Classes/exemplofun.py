###4 PARAMETROS OBRIGATÓRIOS, A NAO SER QUE TENHA PARAMETRO DEFAULT
# def soma(x,y,z,t=0):
#     s = x + y + z + t
#     return s

# res = soma(12,12,12,125)
# print(res)

### *ARGS é uma lista de parametros
def somar(num,*args):
    s = num
    for i in args:
        s += i
    return s

res = somar(11,12,13,33)
print(res)

