
from Curso import Curso
class Escola:

    def __init__(self, nome_escola):
        self.nome_escola = nome_escola
        self.lista_cursos = []

    def add_curso(self, nome_curso, codigo):
        curso = Curso(nome_curso, codigo)
        self.lista_cursos.append(curso)

    def mostrar_cursos(self):
   
        if self.lista_cursos:
            print(f"Cursos disponíveis na {self.nome_escola}:")
            for curso in self.lista_cursos:
                print(f"Curso: {curso.nome_curso} (Código: {curso.cod})")
                curso.mostrar_alunos()  
        else:
            print(f"Não há cursos cadastrados na {self.nome_escola}.")
