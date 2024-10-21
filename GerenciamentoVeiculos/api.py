from flask import Flask, request, jsonify
from Carro import Carro
from Moto import Moto

api = Flask(__name__)

@api.route('/calcular_aluguel', methods=['POST'])
def calcular_aluguel():
    data = request.get_json()
    
    nome_veiculo = data['nomeVeiculo']
    ano_veiculo = data['anoVeiculo']
    tipo_veiculo = data['tipoVeiculo']
    valor_diario = float(data['valorDiario'])
    dias_aluguel = int(data['diasAluguel'])
    
    # Verifica o tipo de veículo e cria a instância apropriada
    if tipo_veiculo == 'carro':
        tipo_combustivel = data['campoExtra']
        veiculo = Carro(nome_veiculo, ano_veiculo, valor_diario, tipo_combustivel)
    else:
        cilindrada = float(data['campoExtra'])
        veiculo = Moto(nome_veiculo, ano_veiculo, valor_diario, cilindrada)
    
    valor_total = veiculo.calcular_aluguel(dias_aluguel)

    return jsonify({'valorTotal': valor_total})

if __name__ == '__main__':
    api.run(debug=True)

