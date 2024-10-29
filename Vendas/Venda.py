class Venda:
    def __init__(self, nome, qtd, preco_unitario):
        self.nome = nome
        self.qtd = qtd
        self.preco_unitario = preco_unitario

    def total_vendas(self):
        return self.qtd * self.preco_unitario