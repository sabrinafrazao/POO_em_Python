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
