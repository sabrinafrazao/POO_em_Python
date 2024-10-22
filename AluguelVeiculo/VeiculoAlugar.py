class VeiculoAlugar:

    def __init__(self, nome, ano, valor_diario):
        self.__nome = nome
        self.__ano = ano
        self.__valor_diario = valor_diario
        self.dias = 0

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, valor):
        self.__ano = valor

    @property
    def valor_diario(self):
        return self.__valor_diario
    
    @valor_diario.setter
    def valor_diario(self, valor):
        self.__valor_diario = valor

    def calculo_total_aluguel(self, dias, desconto=0):
        valor_total = self.__valor_diario * dias
        if desconto > 0:
            valor_total -= (valor_total * (desconto / 100))
        return valor_total


class Moto(VeiculoAlugar):
    
    def __init__(self, nome, ano, valor_diario, cilindrada):
        super().__init__(nome, ano, valor_diario)
        self.cilindrada = cilindrada

    def custo_cilindrada(self, dias, desconto=0):
        valor_total = self.calculo_total_aluguel(dias, desconto)
        if self.cilindrada > 200:
            valor_total += (valor_total * 0.10)
        return valor_total


class Carro(VeiculoAlugar):

    def __init__(self, nome, ano, valor_diario, tipo_combustivel):
        super().__init__(nome, ano, valor_diario)
        self.tipo_combustivel = tipo_combustivel

    def desconto_extra(self, dias, desconto=0, desconto_extra=0):
        valor_total = self.calculo_total_aluguel(dias, desconto)
        if dias > 7:
            valor_total -= (valor_total * (desconto_extra / 100))
        return valor_total
