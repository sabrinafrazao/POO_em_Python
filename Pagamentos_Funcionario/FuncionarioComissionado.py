from Funcionario import Funcionario

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        self.validacao_salario(salario_base)
        self.validacao_taxa_comissao(taxa_comissao)
        self.validacao_vendas(vendas)

        super().__init__(nome, matricula)
        self._salario_base = salario_base
        self._vendas = vendas
        self._taxa_comissao = taxa_comissao

    @property
    def salario_base(self):
        return self._salario_base


    def validacao_salario(self, salario_base):
        if salario_base < 0:
            raise ValueError("O salário base deve ser positivo!")
        
    @salario_base.setter
    def set_salario_base(self, salario_base):
        self.validacao_salario(salario_base)
        self._salario_base = salario_base

    @property
    def vendas(self):
        return self._vendas

    def validacao_vendas(self, vendas):
         if vendas < 0:
            raise ValueError("O valor das vendas deve ser positivo!")
         
    @vendas.setter
    def set_vendas(self, vendas):
        self.validacao_vendas(vendas)
        self._vendas = vendas

    @property
    def taxa_comissao(self):
        return self._taxa_comissao

    def validacao_taxa_comissao(self, taxa_comissao):
        if taxa_comissao < 0:
            raise ValueError("A taxa de comissão deve ser positiva!")
    
    @taxa_comissao.setter
    def set_taxa_comissao(self, taxa_comissao):
        self.validacao_taxa_comissao(taxa_comissao)
        self._taxa_comissao = taxa_comissao

    def calcular_salario(self):
        return self._salario_base + (self._vendas * self._taxa_comissao)