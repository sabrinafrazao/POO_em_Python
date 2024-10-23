from Funcionario import Funcionario

class FuncionarioHora(Funcionario):
    
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        self.validacao_horas(horas_trabalhadas)
        self.validacao_valor_horas(valor_hora)
        super().__init__(nome, matricula)
        self._horas_trabalhadas = horas_trabalhadas
        self._valor_hora = valor_hora


    @property
    def horas_trabalhadas(self):
        return self._horas_trabalhadas
    
    def validacao_horas(self, horas_trabalhadas):
        if horas_trabalhadas < 0:
            raise ValueError("As horas trabalhadas devem ser positivas!")

    @horas_trabalhadas.setter
    def set_horas_trabalhadas(self, horas_trabalhadas: int):
        self.validacao_horas(horas_trabalhadas)
        self._horas_trabalhadas = horas_trabalhadas

    @property
    def valor_hora(self):
        return self._valor_hora

    def validacao_valor_horas(self, valor_hora):
         if valor_hora < 0:
            raise ValueError("O valor por hora deve ser positivo!")
         
    @valor_hora.setter
    def set_valor_hora(self, valor_hora):
        self.validacao_valor_horas(valor_hora)
        self._valor_hora = valor_hora


    def calcular_salario(self):
        return self._horas_trabalhadas * self._valor_hora