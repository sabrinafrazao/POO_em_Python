from Pagamento import Pagamento
from PagamentoCartaoCredito import PagamentoCartaoCredito
from PagamentoPix import PagamentoPix
from PagamentoBoleto import PagamentoBoleto

def processar(pagamento: Pagamento):
    pagamento.processar_pagamento()

def main():
    
    pagamento_cartao = PagamentoCartaoCredito("1234-5678-9101-1121")
    pagamento_boleto = PagamentoBoleto("BOLETO123456789")
    pagamento_pix = PagamentoPix("chavepix@email.com")

   
    processar(pagamento_cartao)
    processar(pagamento_boleto)
    processar(pagamento_pix)

if __name__ == "__main__":
    main()