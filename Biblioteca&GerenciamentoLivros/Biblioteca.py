

import csv
from functools import reduce
import json
import pickle
from Livro import Livro


class Biblioteca:
    
    def __init__(self):
        self.livros = []


    def adicionar_livros(self, livro):
        self.livros.append(livro)

    def listar_por_autor(self, autor):

        filtro_autor = list(filter(lambda livro: livro.autor == autor, self.livros))

        return filtro_autor
    
    def total_por_genero(self, genero):

        contar_por_genero = reduce(lambda count, livro: count + 1 if livro.genero == genero else count, self.livros, 0)

        return contar_por_genero
    
    def listar_titulos(self):
        return list(map(lambda livro: livro.titulo, self.livros))

    def filtrar_livros(self, ano=None, genero=None):
        return list(filter(lambda livro: (ano is None or livro.ano_publicacao == ano) and
                                       (genero is None or livro.genero == genero), self.livros))
    

    def exportar_texto(self, arquivo = "Arquivo_texto.txt"):
        with open(arquivo, 'w') as arquivo_texto:
            for livro in self.livros:
                arquivo_texto.write(f"{livro.titulo}, {livro.autor}, {livro.ano_publicacao}, {livro.genero}")

        print(f"Dados salvos em {arquivo}.")

    def importar_texto(self,  arquivo = "Arquivo_texto.txt"):
        with open(arquivo, 'r') as arquivo_texto:
            for livro in arquivo_texto:
                titulo, autor, ano_publicacao, genero = livro.strip().split(', ')
                self.adicionar_livros(Livro(titulo, autor, int(ano_publicacao), genero))

        print(f"Dados carregados em {arquivo}.")
   

    def exportar_json(self, arquivo="Arquivo_json.json"):
        dados = [{"titulo": livro.titulo, "autor": livro.autor, "ano_publicacao": livro.ano_publicacao, "genero": livro.genero} for livro in self.livros]
        with open(arquivo, "w") as arquivo_json:
            json.dump(dados, arquivo_json)
        print(f"Dados salvos em {arquivo}.")


    def importar_json(self, arquivo = "Arquivo_json.json"):
        with open(arquivo, "r") as arquivo_json:
            dados = json.load(arquivo_json)
            self.livros = [Livro(**livro) for livro in dados]
        print(f"Dados carregados de {arquivo}.")


    def exportar_csv(self, arquivo = "Arquivo_csv.csv"):
        with open(arquivo, "w", newline="") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(["Livro", "Autor", "Ano Publicação", "Genero"])
            for livro in self.livros:
                escritor.writerow([livro.titulo, livro.autor, livro.ano_publicacao, livro.genero])
        print(f"Dados salvos em {arquivo}.")

    def importar_csv(self, arquivo="Arquivo_csv.csv"):
        with open(arquivo, "r") as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            next(leitor) 
            self.livros = [Livro(linha[0], linha[1], int(linha[2]), linha[3]) for linha in leitor]  # corrigido self.alunos para self.livros
        print(f"Dados carregados de {arquivo}.")

    def exportar_pickle(self, arquivo="Arquivo_pkl.pkl"):
        with open(arquivo, "wb") as arquivo_pkl:
            pickle.dump(self.livros, arquivo_pkl)
        print(f"Dados salvos em {arquivo}.")

    def importar_pickle(self, arquivo="Arquivo_pkl.pkl"):
        with open(arquivo, "rb") as arquivo_pkl:
            self.livros = pickle.load(arquivo_pkl)
        print(f"Dados carregados de {arquivo}.")


    def backup(self, arquivo):
        
        if arquivo.endswith('.json'):
            self.exportar_json(arquivo)
        else:
            self.exportar_pickle(arquivo)
