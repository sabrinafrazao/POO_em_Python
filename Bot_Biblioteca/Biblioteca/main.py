from Biblioteca import Biblioteca
from Autor import Autor
from Livro import Livro


# Criação de autores
autor1 = Autor("Machado de Assis")
autor2 = Autor("Clarice Lispector")

# Criação de livros com os autores associados
livro1 = Livro("Dom Casmurro", autor1, 101)
livro2 = Livro("Memórias Póstumas de Brás Cubas", autor1, 102)
livro3 = Livro("A Hora da Estrela", autor2, 201)

# Criação da biblioteca
biblioteca = Biblioteca("Biblioteca Central")

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Mostrando o total de livros
Biblioteca.mostrar_total_livros()

# Realizando um empréstimo e depois devolvendo
biblioteca.registrar_emprestimo(101, "Cliente 1")
biblioteca.registrar_emprestimo(102, "Cliente 2")
biblioteca.mostrar_livros_disponiveis()

# Devolvendo um livro
biblioteca.registrar_devolucao(101)
biblioteca.mostrar_livros_disponiveis()

