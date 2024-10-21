class Aluno:

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


    def mostrar_info(self):

        print(f"{self.nome} - {self.matricula}")