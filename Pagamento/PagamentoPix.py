from Pagamento import Pagamento
class PagamentoPix(Pagamento):

    def __init__(self,  chave_pix):
        self. chave_pix =  chave_pix


    def  processar_pagamento(self):

        print("O pagamento via Pix foi processado.")