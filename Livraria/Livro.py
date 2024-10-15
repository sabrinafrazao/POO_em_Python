class Livro:

    def __init__(self, titulo, autor):

        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False

            print(f"O livro {self.titulo} foi emprestado")
        
        else:
            print(f"O livro {self.titulo} já está emprestado ")


    def devolver(self):

        if not self.disponivel:
            self.disponivel = True

            print(f"O livro {self.titulo} já foi devolvido")


    def mostrar_info(self):
        if self.disponivel:
            disponibilidade = "Disponivel"

        else: 

            disponibilidade = "Emprestado"

            print(f"Titulo: {self.titulo}, autor: {self.autor}, status: {disponibilidade}")

    




class Livraria: 

    def __init__(self):
        
        self.inventario= []

    def adicionar_livros(self, inventario):
        self.livros.append()
        print(f"Livro {Livro.titulo}adicionado na livraria")

    def emprestar_livro(self, livros):

        for livro in livros:
            ...


