from VeiculoAlugar import VeiculoAlugar

class Moto(VeiculoAlugar):
    
    def __init__(self, nome, ano, valor_diario, cilindrada):
        super().__init__(nome, ano, valor_diario)
        self.cilindrada = cilindrada


    def custo_cilindrada(self, cilidrada=0):
        valor_total_apos_cilindrada = self.calculo_total_aluguel()

        if cilidrada > 200:
            valor_total_apos_cilindrada += (valor_total_apos_cilindrada * 0.10)
