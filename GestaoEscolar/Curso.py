from Aluno import Aluno

class Curso:

    def __init__(self, nome_curso, cod):
        self.nome_curso = nome_curso
        self.cod = cod
        self.lista_alunos = []



    def add_alunos(self, nome, matricula):

        aluno = Aluno(nome, matricula)

        self.lista_alunos.append(aluno)

    def mostrar_alunos(self):
    
        if self.lista_alunos:
            print(f"Alunos matriculados no curso {self.nome_curso}:")
            for aluno in self.lista_alunos:
                aluno.mostrar_info()
        else:
            print(f"Não há alunos matriculados no curso {self.nome_curso}.")



 
        

        

