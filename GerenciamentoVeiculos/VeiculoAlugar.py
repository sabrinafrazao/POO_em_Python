class VeiculoAlugar:
    
    total_veiculos = 0 

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

            


 



