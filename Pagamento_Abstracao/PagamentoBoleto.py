from Pagamento import Pagamento
class PagamentoBoleto(Pagamento):

    def __init__(self, codigo_boleto):
        
        self.codigo_boleto = codigo_boleto

    def processar_pagamentos(self):

        print("O Pagamento com boleto foi processado")