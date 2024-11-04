
from Biblioteca import Biblioteca
from Livro import Livro


biblioteca = Biblioteca()


biblioteca.adicionar_livros(Livro("Dom Quixote", "Miguel de Cervantes", 1605, "Ficção"))
biblioteca.adicionar_livros(Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Infantil"))
biblioteca.adicionar_livros(Livro("1984", "George Orwell", 1949, "Ficção Científica"))
biblioteca.adicionar_livros(Livro("O Hobbit", "J.R.R. Tolkien", 1937, "Fantasia"))
biblioteca.adicionar_livros(Livro("A Revolução dos Bichos", "George Orwell", 1945, "Ficção"))


print("Livros por George Orwell:", biblioteca.listar_por_autor("George Orwell"))


print("Número de livros de Ficção:", biblioteca.total_por_genero("Ficção"))


biblioteca.exportar_texto("biblioteca.txt")
biblioteca.exportar_json("biblioteca.json")
biblioteca.exportar_csv("biblioteca.csv")
biblioteca.exportar_pickle("biblioteca.pkl")


biblioteca.backup("backup_biblioteca.json")


nova_biblioteca = Biblioteca()
nova_biblioteca.importar_json("biblioteca.json")
print("Livros importados do JSON:", nova_biblioteca.livros)


print("Livros de 1949 e do gênero Ficção Científica:", biblioteca.filtrar_livros(ano=1949, genero="Ficção Científica"))
