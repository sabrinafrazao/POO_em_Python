class ContaBancaria:

    taxa_juros = 0.02

    def __init__(self, titular, saldo):

        self.__titular = titular
        self.__saldo = saldo


    def depositar(self, valor, titular):
            
            if valor > 0:
    
                self.__saldo += valor

                print(f" Deposito de R${valor:.2f} realizado com sucesso")

            else:
                  
                  print("O valor do depósito deve ser positivo")
                  

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
                self.__saldo -= valor
                
                print("O valor do deposito de R${valor:.2f} realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def mostar_saldo(self):
            return self.__saldo
        
    @classmethod
    def conta_com_juros(cls, titular, saldo_incial):
          
          saldo_com_juros = saldo_incial * (1 + cls.taxa_juros)

          return cls(titular, saldo_com_juros)
    

    
conta1 = ContaBancaria("Alice", 1000)


print(conta1._ContaBancaria__saldo)

    


        