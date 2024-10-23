from Funcionario import Funcionario

class FuncionarioMensal(Funcionario):
    def __init__(self, nome, matricula, salario_mensal):
        self.validacao_salario_mensal(salario_mensal)
        super().__init__(nome, matricula)
        self._salario_mensal = salario_mensal

    @property
    def salario_mensal(self):
        return self._salario_mensal

    def validacao_salario_mensal(self, salario_mensal):
        if salario_mensal < 0:
            raise ValueError("O salário mensal deve ser positivo!")
        
    @salario_mensal.setter
    def set_salario_mensal(self, salario_mensal):
        self.validacao_salario_mensal(salario_mensal)
        self._salario_mensal = salario_mensal

    def calcular_salario(self):
        return self._salario_mensal