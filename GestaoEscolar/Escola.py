
from Curso import Curso
class Escola:

    def __init__(self, nome_escola):
        self.nome_escola = nome_escola
        self.lista_cursos = []


    def add_curso(self, nome_curso, cod):

        curso = Curso(nome_curso, cod)

        self.lista_cursos.append(curso)

    def mostrar_cursos(self):

        if self.add_curso:

            print(f"Os cursos da {self.nome_escola}: ")

            for curso in self.lista_cursos:

                print(curso)


            



