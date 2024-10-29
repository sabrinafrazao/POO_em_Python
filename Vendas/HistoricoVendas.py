from functools import reduce
from Venda import Venda

class HistoricoVendas:

    def __init__(self):
        self.vendas = []

    
    def adicionar_vendas(self, venda):
        self.vendas.append(venda)


    def total_por_produtos(self):
        totais = {}

        for venda in self.vendas:
            totais = [venda.nome] = reduce( lambda total, v: total + v.total_venda(),
                filter(lambda x: x.nome_produto == venda.nome_produto, self.vendas),
                0)
            
        return totais

