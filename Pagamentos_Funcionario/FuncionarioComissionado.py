from Funcionario import Funcionario

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        super().__init__(nome, matricula)
        self.__salario_base = salario_base
        self.__vendas = vendas
        self.__taxa_comissao = taxa_comissao

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        self.__salario_base = salario_base

    @property
    def vendas(self):
        return self.__vendas

    @vendas.setter
    def vendas(self, vendas):
        self.__vendas = vendas

    @property
    def taxa_comissao(self):
        return self.__taxa_comissao

    @taxa_comissao.setter
    def taxa_comissao(self, taxa_comissao):
        self.__taxa_comissao = taxa_comissao

    def calcular_salario(self):
        return self.__salario_base + (self.__vendas * self.__taxa_comissao)