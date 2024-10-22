from Pagamento import Pagamento
from PagamentoCartaoCredito import PagamentoCartaoCredito
from PagamentoPix import PagamentoPix
from PagamentoBoleto import PagamentoBoleto

def processar(pagamento: Pagamento):
    pagamento.detalhes_pagamentos()
    pagamento.processar_pagamentos()

def main():
   
    pagamento_cartao = PagamentoCartaoCredito("1234 5678 9012 3456")
    pagamento_boleto = PagamentoBoleto("000111222333")
    pagamento_pix = PagamentoPix("email@example.com")
    

    processar(pagamento_cartao)

    print()


    processar(pagamento_boleto)
    
    print()
    

    processar(pagamento_pix)

if __name__ == "__main__":
    main()