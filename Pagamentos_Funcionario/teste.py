from abc import ABC, abstractmethod


class Funcionario(ABC):
   
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @abstractmethod
    def calcular_salario(self):
        ...


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
    

from Funcionario import Funcionario

class FuncionarioHora(Funcionario):
    
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora ):

        super().__init__(nome, matricula)
        self._horas_trabalhadas = horas_trabalhadas
        self._valor_hora = valor_hora


    @property
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas

    @horas_trabalhadas.setter
    def horas_trabalhadas(self, horas_trabalhadas):
        if horas_trabalhadas < 0:
            raise ValueError("As horas trabalhadas devem ser positivas!")
        self._horas_trabalhadas = horas_trabalhadas

    @property
    def valor_hora(self):
        return self._valor_hora

    @valor_hora.setter
    def valor_hora(self, valor_hora):
        if valor_hora < 0:
            raise ValueError("O valor por hora deve ser positivo!")
        self._valor_hora = valor_hora


    def calcular_salario(self):
        return self._horas_trabalhadas * self._valor_hora
    
from Funcionario import Funcionario

class FuncionarioMensal(Funcionario):
    def __init__(self, nome, matricula, salario_mensal):
        super().__init__(nome, matricula)
        self._salario_mensal = salario_mensal

    @property
    def salario_mensal(self):
        return self._salario_mensal

    @salario_mensal.setter
    def salario_mensal(self, salario_mensal):
        if salario_mensal < 0:
            raise ValueError("O salário mensal deve ser positivo!")
        self.__salario_mensal = salario_mensal

    def calcular_salario(self):
        return self._salario_mensal

from Funcionario import Funcionario

class FuncionarioProjeto(Funcionario):

    def __init__(self, nome, matricula, valor_por_projeto):
        super().__init__(nome, matricula)
        self._valor_por_projeto = valor_por_projeto

    @property
    def valor_por_projeto(self):
       
        return self._valor_por_projeto

    @valor_por_projeto.setter
    def valor_por_projeto(self, valor_por_projeto):
        if valor_por_projeto < 0:
            raise ValueError("O valor por projeto deve ser positivo!")
        self.__valor_por_projeto = valor_por_projeto
        

    def calcular_salario(self):
      
        return self._valor_por_projeto

        
   

from Funcionario import Funcionario
from FuncionarioHora import FuncionarioHora
from FuncionarioMensal import FuncionarioMensal
from FuncionarioComissionado import FuncionarioComissionado
from FuncionarioProjeto import FuncionarioProjeto
import datetime


def processar_pagamento(funcionario: Funcionario):
    print(f"Nome: {funcionario.nome}")
    print(f"Salário: {funcionario.calcular_salario()}\n")
    print("---------------------------------")


def simular_pagamento_mensal(funcionario, mes, ano, feriados):
    # Verifica se o mês é dezembro (12) para calcular o próximo mês corretamente
    if mes == 12:
        dias_no_mes = (datetime.date(ano + 1, 1, 1) - datetime.date(ano, mes, 1)).days
    else:
        dias_no_mes = (datetime.date(ano, mes + 1, 1) - datetime.date(ano, mes, 1)).days

    horas_totais = 0

    for dia in range(1, dias_no_mes + 1):
        data_atual = datetime.date(ano, mes, dia)
        if data_atual.weekday() < 5 and data_atual not in feriados:  # Dias úteis e sem feriados
            horas_totais += 8  # Assumindo 8 horas de trabalho por dia

    return funcionario.valor_hora * horas_totais


# Função principal
def main():
    funcionarios = []

    feriados = [datetime.date(2024, 12, 25), datetime.date(2024, 1, 1)]  # Exemplo de feriados.

    try:
        funcionarios.append(FuncionarioHora("Antônio", 123456, 80, -25))
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    try:
        funcionarios.append(FuncionarioMensal("Diego", 432335, 4560))
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    try:
        funcionarios.append(FuncionarioComissionado("Jonas", 567786, 3000, 5000, 0.05))
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    try:
        funcionarios.append(FuncionarioProjeto("Sabrina", 5679, 1000000))
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    for funcionario in funcionarios:
        processar_pagamento(funcionario)

    # Simulação do pagamento do funcionário horista no mês de dezembro
    try:
        print("Simulação de pagamento para um funcionário horista no mês de dezembro:")
        salario_mes = simular_pagamento_mensal(funcionarios[0], 12, 2024, feriados)
        print(f"Nome: {funcionarios[0].nome}, Salário para dezembro: {salario_mes:.2f}")
    except IndexError:
        print("Erro: Não há funcionário horista para simulação.")

if __name__ == "__main__":
    main()