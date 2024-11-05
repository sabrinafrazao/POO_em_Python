from excecoes import SaldoInsuficienteError, LimiteExcedidoError, ContaDestinoInvalidaError
class Conta:

    def __init__(self, titulo, saldo, limite):

        self.titutlo = titulo
        self.saldo = saldo
        self.limite = limite

    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Erro: Saldo insuficiente.")
        self.saldo -= valor
        print(f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")

    def transferir(self, valor, conta_destino):
        if valor > self.limite:
            raise LimiteExcedidoError("Erro: O valor da transferência excede o limite da conta.")
        if conta_destino is None:
            raise ContaDestinoInvalidaError("Erro: Conta de destino inválida.")
        if valor > self.saldo:
            raise SaldoInsuficienteError("Erro: Saldo insuficiente para realizar a transferência.")
        
        self.saldo -= valor
        conta_destino.depositar(valor)
        print(f"Transferência de R${valor} para {conta_destino.titular} realizada com sucesso.")