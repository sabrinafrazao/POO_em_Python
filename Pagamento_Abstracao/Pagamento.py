from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def processar_pagamentos():
        ...


    def detalhes_pagamentos(self):

          print(f"Processando pagamento via {self.__class__.__name__}.")
        



    