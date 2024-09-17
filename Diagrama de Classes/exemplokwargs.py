def argumentosnomeados(param1,**kwargs):
    imp = kwargs['imposto']
    resultado = param1 * imp / 100
    resultado = resultado + kwargs['valor']
    resultado = resultado + (resultado  * kwargs['porc'] / 100)
    texto = f"{kwargs['nome']} deve {resultado}"
    return texto

x = argumentosnomeados(1000,imposto=20,valor=40,porc=50,nome="Thiago")
print(x)