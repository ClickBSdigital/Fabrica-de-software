# from datetime import datetime

# Classe Agenda
class Agenda:
    def __init__(self, dia, mes, ano, datetime, anotacao=""):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao
        self.datetime = datetime

    def validar_data(self):
        """Valida se a data fornecida é válida."""
        try:
            self.datetime(self.ano, self.mes, self.dia)
            print("Data válida.")
            return True
        except ValueError:
            print("Data inválida.")
            return False

    def anotar_tarefa(self, anotacao):
        """Anota uma tarefa na agenda."""
        if self.validar_data():
            self.anotacao = anotacao
            print("Tarefa anotada com sucesso.")
        else:
            print("Não foi possível anotar a tarefa devido a uma data inválida.")

    def mostrar_anotacao(self):
        """Exibe a anotação da data especificada."""
        if self.validar_data():
            print(f"Anotação para {self.dia}/{self.mes}/{self.ano}: {self.anotacao}")
        else:
            print("Não há anotação para uma data inválida.")

# Exemplo de uso da classe
agenda1 = Agenda(25, 12, 2024)
agenda1.anotar_tarefa("Comprar presentes de Natal")
agenda1.mostrar_anotacao()

print("\n")

agenda2 = Agenda(31, 2, 2024)  # Data inválida
agenda2.anotar_tarefa("Fazer backup dos arquivos")
agenda2.mostrar_anotacao()

# =========================================

# Explicação do Código:
# Atributos:

# dia: Representa o dia do mês.
# mes: Representa o mês do ano.
# ano: Representa o ano.
# anotacao: Representa a anotação ou tarefa para a data específica.
# Métodos:

# validar_data(): Verifica se a data fornecida (dia, mês, ano) é válida usando o módulo datetime. Se a data for válida, retorna True; caso contrário, retorna False.
# anotar_tarefa(anotacao): Primeiro, valida a data e, se a data for válida, armazena a anotação na agenda.
# mostrar_anotacao(): Exibe a anotação para a data especificada, mas apenas se a data for válida.
# Exemplo de Uso:
# Agenda 1:

# Uma instância da classe Agenda é criada para o dia 25 de dezembro de 2024.
# A tarefa "Comprar presentes de Natal" é anotada e, em seguida, exibida.
# Agenda 2:

# Uma instância da classe Agenda é criada para o dia 31 de fevereiro de 2024 (uma data inválida).
# A tentativa de anotar uma tarefa e exibi-la falha devido à data inválida.