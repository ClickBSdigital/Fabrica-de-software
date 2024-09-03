# def verificaLista(*params):
#     for item in params:
#         print(item)
    
# verificaLista(13,"Rodrigo","Tilen","Fred","Julia",27)

def chamaOEliandro(**kwargs):
    print(f"{kwargs['nome']} tem {kwargs['idade']} e mora em {kwargs['cidade']}")

#####KWARGS PARAMETROS NOMEADOS
def calcula(**kwargs):
    city = kwargs['cidade']
    old = kwargs['idade']
     
    val = kwargs['valor']
    perc = kwargs['porcentagem']
    resultado = val * perc / 100

    chamaOEliandro(nome="Eliandro",idade=old,cidade=city)

    return resultado

x = calcula(idade=39,cidade="CG",valor=1000,porcentagem=25)
print(x)
