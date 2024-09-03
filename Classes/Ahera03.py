# 3 - Classe Ingresso: Crie uma super classe que modele um Ingresso. 
# Esta classe deve possuir os seguintes atributos:
# Preco;
# Setor;
# Método:
# alterar_preco() e mostrar_setor();
# Subclasses:
# Defina a subclasse ingressoVIP com os seguintes 
# atributos: camarote, open_bar, open_food, estacionamento -> todos booleanos, True ou False;
# Acrescente os métodos pegar_bebida() e acessar_camarote();
class Ingresso: ###SUPERCLASS
    def __init__(self,preco,setor):
        self._preco = preco #ATRIBUTO PUBLICO
        self.__setor = setor #ATRIBUTO PRIVADO   ->> 2 underlines __
    
    def alterarPreco(self,novo_preco):
        self.preco = novo_preco

    def mostrarSetor(self):
        return self.setor

class IngressoVIP(Ingresso): #SUBCLASS
    def __init__(self, preco, setor, camarote, open_bar, open_food, est):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.openbar = open_bar
        self.openfood = open_food
        self.estacionamento = est

    def pegarBebida(self):
        if self.openbar:
            print("BEBIDA LIBERADA COM SUCEESSOO")
        else:
            print("COMPRAR FICHAS - STATUS OPENBAR: ",self.openbar)
    
    def acessarCamarote(self):
        if self.camarote:
            print("ACESSO LIBERADO")
        else:
            print("VAZAAAA: ",self.camarote)

vip = IngressoVIP(400,"A",False,True,True,True)

vip.pegarBebida()
vip.acessarCamarote()

print(vip._preco)