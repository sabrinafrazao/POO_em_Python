from Funcionario import Funcionario

class FuncionarioHora(Funcionario):
    
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora ):

        super().__init__(nome, matricula)
        self.__horas_trabalhadas = horas_trabalhadas
        self.__valor_hora = valor_hora


    @property
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas

    @horas_trabalhadas.setter
    def horas_trabalhadas(self, horas_trabalhadas):
        self.__horas_trabalhadas = horas_trabalhadas

    @property
    def valor_hora(self):
        return self.__valor_hora

    @valor_hora.setter
    def valor_hora(self, valor_hora):
        self.__valor_hora = valor_hora

    def calcular_salario(self):
        return self.__horas_trabalhadas * self.__valor_hora