# 6 - Classe Agenda: crie uma classe que represente uma agenda de tarefas. Esta classe 
# deve possuir os seguintes atributos:
#  Dia;
#  Mês;
#  Ano;
#  Anotação;
#  A classe deve ter os seguintes métodos:
#  validar_data();
#  anotar_tarefa();
#  Mostrar_anotação();
import datetime

class Agenda:
    def __init__(self, dia, mes, ano, anotacao=""):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validar_data(self):
        """Verifica se a data fornecida é válida."""
        try:
            data = datetime.date(self.ano, self.mes, self.dia)
            return True
        except ValueError:
            return False

    def anotar_tarefa(self, anotacao):
        """Adiciona uma anotação à data especificada."""
        if self.validar_data():
            self.anotacao = anotacao
            print(f"Anotação para {self.dia}/{self.mes}/{self.ano} salva com sucesso.")
        else:
            print("Data inválida. Anotação não salva.")

    def mostrar_anotacao(self):
        """Exibe a anotação para a data especificada."""
        if self.validar_data():
            if self.anotacao:
                print(f"Anotação para {self.dia}/{self.mes}/{self.ano}: {self.anotacao}")
            else:
                print(f"Não há anotações para {self.dia}/{self.mes}/{self.ano}.")
        else:
            print("Data inválida. Não há anotações para exibir.")

# Exemplo de uso:
agenda = Agenda(30, 8, 2024)

if agenda.validar_data():
    agenda.anotar_tarefa("Reunião importante às 14h.")
else:
    print("A data fornecida é inválida.")

agenda.mostrar_anotacao()  # Tenta exibir a anotação, mas a data é inválida


############################

# Explicação da Classe Agenda:
# Atributos:

# dia: Armazena o dia da tarefa.
# mes: Armazena o mês da tarefa.
# ano: Armazena o ano da tarefa.
# anotacao: Armazena a anotação associada à data.
# Métodos:

# validar_data(): Verifica se a data fornecida (dia, mês, ano) é válida usando o módulo datetime. Retorna True se a data for válida e False caso contrário.
# anotar_tarefa(anotacao): Adiciona uma anotação à data, se a data for válida. Se a data for inválida, uma mensagem de erro é exibida.
# mostrar_anotacao(): Exibe a anotação para a data, se a data for válida. Se não houver anotação ou a data for inválida, uma mensagem apropriada é exibida.
# Exemplo de Uso:
# No exemplo de uso, criamos uma instância da classe Agenda com uma data (30 de fevereiro de 2024) e tentamos validar a data. Como a data é inválida (não existe 30 de fevereiro), a anotação não é salva, e uma mensagem de erro é exibida quando tentamos mostrar a anotação.

# Observações:
# Módulo datetime: O módulo datetime é utilizado para verificar a validade da data. Se a data não for válida, o Python lançará uma exceção ValueError, que é capturada para retornar False.
# Validação de Data: A validação de data é importante para garantir que a agenda não armazene anotações em datas inexistentes.