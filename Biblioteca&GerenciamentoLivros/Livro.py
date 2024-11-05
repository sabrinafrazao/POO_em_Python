class Livro:

    def __init__(self, titulo, autor, ano_publicacao, genero):  # corrigido 'ano_publicacao'
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero

   
    
    def __repr__(self):  
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', ano_publicacao={self.ano_publicacao}, genero='{self.genero}')"
