class Aluno:
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def mostrar_info(self):
        print(f"Nome do Aluno: {self.nome}")
        print(f"Número de Matrícula: {self.matricula}")
