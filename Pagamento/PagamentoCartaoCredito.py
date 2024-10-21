from Pagamento import Pagamento

class PagamentoCartaoCredito(Pagamento):
    
    def __init__(self, numero_cartao):

        self.numero_cartao = numero_cartao

    def processar_pagamento(self):

        print("O Pagamento com cartão de crédito foi processado com sucesso")