from flask import Flask, request, jsonify
from flask_cors import CORS
from VeiculoAlugar import VeiculoAlugar
from Carro import Carro
from Moto import Moto

api = Flask(__name__)
CORS(api) 

@api.route('/calcular_aluguel', methods=['POST'])
def calcular_aluguel():
    data = request.json

    # Validação dos dados
    if 'tipoVeiculo' not in data or 'dias' not in data or 'desconto' not in data:
        return jsonify({'error': 'Dados insuficientes'}), 400

    tipo_veiculo = data['tipoVeiculo']
    dias = int(data['dias'])
    desconto = float(data['desconto'])

    if tipo_veiculo == 'carro':
        carro = Carro(data['nomeVeiculo'], data['anoVeiculo'], data['valorDiario'], data['combustivel'])
        valor_total = carro.desconto_extra(dias, desconto, desconto_extra=10)  
    elif tipo_veiculo == 'moto':
        moto = Moto(data['nomeVeiculo'], data['anoVeiculo'], data['valorDiario'], data['cilindrada'])
        valor_total = moto.custo_cilindrada(dias, desconto)  
    else:
        return jsonify({'error': 'Tipo de veículo inválido'}), 400

    return jsonify({'valor_total': valor_total})


if __name__ == '__main__':
    api.run(debug=True)
