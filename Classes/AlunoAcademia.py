class AlunoAcad:
    def __init__(self,nome,idade,peso,altura,mensalidade=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade
    
    def calculaIMC(self):
        imc = self.peso / (self.altura * self.altura)
        return imc
    
    def calculaDesconto(self):
        if self.idade < 18:
            desconto = self.mensalidade - (self.mensalidade * 0.20)
            return desconto
        else:
            return self.mensalidade
    

juju = AlunoAcad("JUAO",99,45,1.60)

juju.calculaIMC()
print(juju.mensalidade)
desc = juju.calculaDesconto()
print(desc)
        