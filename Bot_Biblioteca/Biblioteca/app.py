from flask import Flask, request, jsonify
from flask_cors import CORS
from Autor import Autor
from Livro import Livro
from Biblioteca import Biblioteca


app = Flask(__name__)
CORS(app)

biblioteca = Biblioteca("Minha Biblioteca")

@app.route('/adicionar_livro', methods=['POST'])
def adicionar_livro():
    data = request.json
    autor = Autor(data['autor'])
    livro = Livro(data['titulo'], autor, data['codigo'])
    biblioteca.adicionar_livro(livro)
    return jsonify({"message": "Livro adicionado com sucesso!"})

@app.route('/registrar_emprestimo', methods=['POST'])
def registrar_emprestimo():
    data = request.json
    biblioteca.registrar_emprestimo(data['codigo'], data['cliente'])
    return jsonify({"message": "Empréstimo registrado!"})

@app.route('/registrar_devolucao', methods=['POST'])
def registrar_devolucao():
    data = request.json
    biblioteca.registrar_devolucao(data['codigo'])
    return jsonify({"message": "Devolução registrada!"})

@app.route('/livros_disponiveis', methods=['GET'])
def livros_disponiveis():
    livros = [livro.titulo for livro in biblioteca._Biblioteca__livros if livro.disponivel]
    return jsonify(livros)

if __name__ == '__main__':
    app.run(debug=True)

