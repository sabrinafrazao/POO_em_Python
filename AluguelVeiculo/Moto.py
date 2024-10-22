from VeiculoAlugar import VeiculoAlugar

class Moto(VeiculoAlugar):
    
    def __init__(self, nome, ano, valor_diario, cilindrada):
        super().__init__(nome, ano, valor_diario)
        self.cilindrada = cilindrada

    def custo_cilindrada(self, dias, desconto=0):
        valor_total = self.calculo_total_aluguel(dias, desconto)  

        if self.cilindrada > 200:
            valor_total += (valor_total * 0.10) 

        return valor_total