
class Livro:

    def __init__(self, titulo, autor, ano_puplicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_puplicacao
        self.genero = genero


    def mostrar_infor(self):

        return f"Livro: Titulo: {self.titulo}, Autor: {self.autor}, Ano de publicação: {self.ano_publicacao}, Genêro: {self.genero}"
    
    