from VeiculoAlugar import VeiculoAlugar

class Carro(VeiculoAlugar):

    def __init__(self, nome, ano, valor_diario, tipo_combustivel ):
        super().__init__(nome, ano, valor_diario)
        self.tipo_combustivel = tipo_combustivel


    def desconto_extra(self, dias, desconto, desconto_extra=0):
        valor_total_pos_extra = super().calculo_total_aluguel(dias, desconto)

        if  dias> 7: 
            valor_total_pos_extra -= (valor_total_pos_extra * (desconto_extra/100))

        return valor_total_pos_extra
    
