class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro {self.titulo} foi emprestado.")
        else:
            print(f"O livro {self.titulo} já está emprestado.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro {self.titulo} foi devolvido.")
        else:
            print(f"O livro {self.titulo} já está disponível.")

    def mostrar_info(self):
        disponibilidade = "Disponível" if self.disponivel else "Emprestado"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Status: {disponibilidade}")

class Livraria:
    def __init__(self):
        self.__colecao = []
    
    def incluir_livro(self, obra: Livro):
        self.__colecao.append(obra)
        print(f"{obra.titulo} foi adicionado à biblioteca.")
        
    def retirar_livro(self, titulo: str):
        for obra in self.__colecao:
            if obra.titulo == titulo:
                obra.emprestar() 
                return
        print(f"Obra '{titulo}' não encontrada na biblioteca.")
    
    def retornar_livro(self, titulo: str):
        for obra in self.__colecao:
            if obra.titulo == titulo:
                obra.devolver()  
        print(f"Obra '{titulo}' não encontrada na biblioteca.")
    
    def listar_estoque(self):
        print("\nEstoque da Biblioteca:")
        for obra in self.__colecao:
            obra.mostrar_info()  

if __name__ == '__main__':
    biblioteca = Livraria()

    livro1 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien")
    livro2 = Livro("1984", "George Orwell")
    livro3 = Livro("Dom Casmurro", "Machado de Assis")

    biblioteca.incluir_livro(livro1)
    biblioteca.incluir_livro(livro2)
    biblioteca.incluir_livro(livro3)

    print("\n")

    biblioteca.listar_estoque()

    print("\n")

    biblioteca.retirar_livro("1984")

    print("\n")

    biblioteca.listar_estoque()

    print("\n")

    biblioteca.retornar_livro("1984")

    print("\n")
    
    biblioteca.listar_estoque()
