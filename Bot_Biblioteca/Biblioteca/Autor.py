class Autor:
    
    def __init__(self, nome):
        self.__nome = nome
        self.__livros = []

    @property
    def nome(self):
        return self.__nome
    
    def adicionar_livros(self, livro):
        self.__livros.append(livro)

    def mostrar_livros(self):
        print(f"Livros de {self.__nome}: ")
        for livro in self.__livros:
            print(f"- {livro.titulo}")
