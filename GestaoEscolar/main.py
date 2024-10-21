from Aluno import Aluno
from Curso import Curso
from Escola import Escola

def main():
    # Criando alunos
    aluno1 = Aluno("Ana", "2024001")
    aluno2 = Aluno("Bruno", "2024002")
    aluno3 = Aluno("Carlos", "2024003")

    # Criando cursos
    curso1 = Curso("Engenharia de Software", "ESW101")
    curso2 = Curso("Ciência da Computação", "CSC102")

    # Adicionando alunos aos cursos
    curso1.add_alunos(aluno1)
    curso1.add_alunos(aluno2)
    curso2.add_alunos(aluno3)

    # Criando uma escola
    escola = Escola("Escola de Tecnologia IFAM")

    # Adicionando cursos à escola
    escola.add_curso(curso1)
    escola.add_curso(curso2)

    # Mostrando informações da escola, cursos e alunos
    escola.mostrar_cursos()

if __name__ == "__main__":
    main()
