class VeiculoAlugar:

    def __init__(self, nome, ano, valor_diario ):
        self.__nome = nome
        self.__ano = ano
        self.__valor_diario = valor_diario

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, valor):
        self.nome = valor
    
    @property
    def ano(self):
        return self.ano
    
    @ano.setter
    def ano(self, valor):
        self.ano = valor

    @property
    def valor_diario(self):
        return self.valor_diario
    
    @valor_diario.setter
    def valor_diario(self, valor):
        self.valor_diario = valor

    def calculo_total_aluguel(self, dias, desconto=0):
        valor_total = self.valor_diario * dias

        if desconto > 0:
            valor_total -= (valor_total * (desconto/100))

        return valor_total
    

    @classmethod
    def total_veiculo(cls):

        return cls.total_veiculo
    
    @classmethod
    def aumento_porcentual(cls, veiculos, aumento_porcentual):
        for veiculo in veiculos:
            VeiculoAlugar.valor_diario += VeiculoAlugar.valor_diario * (aumento_porcentual/100)

            


 



