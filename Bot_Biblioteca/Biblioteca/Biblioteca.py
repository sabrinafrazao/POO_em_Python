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
