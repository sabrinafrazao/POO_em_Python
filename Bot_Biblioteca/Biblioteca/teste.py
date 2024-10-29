class Biblioteca:
    total_livros = 0

    def __init__(self, nome):
        self.nome = nome
        self.__livros = []
        self.__emprestimos = {}

    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        Biblioteca.total_livros += 1
        print(f"Livro '{livro.titulo}' adicionado à biblioteca '{self.nome}'.")

    def registrar_emprestimo(self, codigo_livro, cliente):
        for livro in self.__livros:
            if livro.codigo == codigo_livro:
                if livro.disponivel:
                    livro.emprestar()
                    self.__emprestimos[codigo_livro] = cliente
                else:
                    print("Este livro já foi emprestado.")
                return
        print("Livro não encontrado.")

    def registrar_devolucao(self, codigo_livro):
        if codigo_livro in self.__emprestimos:
            for livro in self.__livros:
                if livro.codigo == codigo_livro:
                    livro.devolver()
                    del self.__emprestimos[codigo_livro]
                    return
        print("O livro não está registrado como emprestado.")

    def mostrar_livros_disponiveis(self):
        print("Livros disponíveis para empréstimo:")
        for livro in self.__livros:
            if livro.disponivel:
                print(f"- {livro.titulo}")

    @classmethod
    def mostrar_total_livros(cls):
        print(f"Total de livros na biblioteca: {cls.total_livros}")

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


class Livro:

    def __init__(self, titulo, autor, codigo):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo = codigo
        self.__disponivel = True
        self.__autor.adicionar_livros(self)

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def disponivel(self):
        return self.__disponivel

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"O livro '{self.__titulo}' foi emprestado.")

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f"O livro '{self.__titulo}' foi devolvido.")
