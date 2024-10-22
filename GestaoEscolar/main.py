from Aluno import Aluno
from Curso import Curso
from Escola import Escola

from Curso import Curso


def main():
  
    escola = Escola("IFAM")


    escola.add_curso("Python para Iniciantes", "PY001")
    escola.add_curso("Introdução à Ciência de Dados", "CD101")

 
    escola.mostrar_cursos()

 
    curso_python = escola.lista_cursos

    for curso in escola.lista_cursos:
        if curso.nome_curso == "Python para Iniciantes":
            curso_python = curso
            break

    curso_python.add_alunos("Maria Silva", "2023001")
    curso_python.add_alunos("João Santos", "2023002")


    curso_python.mostrar_alunos()

if __name__ == "__main__":
    main()