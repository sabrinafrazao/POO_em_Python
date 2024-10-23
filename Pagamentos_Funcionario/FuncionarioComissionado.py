from Funcionario import Funcionario

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        super().__init__(nome, matricula)
        self._salario_base = salario_base
        self._vendas = vendas
        self._taxa_comissao = taxa_comissao

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        if salario_base < 0:
            raise ValueError("O salário base deve ser positivo!")
        self._salario_base = salario_base

    @property
    def vendas(self):
        return self._vendas

    @vendas.setter
    def vendas(self, vendas):
        if vendas < 0:
            raise ValueError("O valor das vendas deve ser positivo!")
        self._vendas = vendas

    @property
    def taxa_comissao(self):
        return self._taxa_comissao

    @taxa_comissao.setter
    def taxa_comissao(self, taxa_comissao):
        if taxa_comissao < 0:
            raise ValueError("A taxa de comissão deve ser positiva!")
        self._taxa_comissao = taxa_comissao

    def calcular_salario(self):
        return self._salario_base + (self._vendas * self._taxa_comissao)