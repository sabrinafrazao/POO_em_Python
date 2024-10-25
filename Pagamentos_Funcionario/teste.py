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
    

from Funcionario import Funcionario

class FuncionarioHora(Funcionario):
    
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        self.validacao_horas(horas_trabalhadas)
        self.validacao_valor_horas(valor_hora)
        super().__init__(nome, matricula)
        self._horas_trabalhadas = horas_trabalhadas
        self._valor_hora = valor_hora


    @property
    def set_horas_trabalhadas(self):
        return self._horas_trabalhadas
    
    def validacao_horas(self, horas_trabalhadas):
        if horas_trabalhadas < 0:
            raise ValueError("As horas trabalhadas devem ser positivas!")

    @set_horas_trabalhadas.setter
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
    
from Funcionario import Funcionario

class FuncionarioProjeto(Funcionario):

    def __init__(self, nome, matricula, valor_por_projeto):
        self.validacao_valor_projeto(valor_por_projeto)
        super().__init__(nome, matricula)
        self._valor_por_projeto = valor_por_projeto

    @property
    def valor_por_projeto(self):
       
        return self._valor_por_projeto


    def validacao_valor_projeto(self, valor_por_projeto):
        if valor_por_projeto < 0:
            raise ValueError("O valor por projeto deve ser positivo!")
        
    @valor_por_projeto.setter
    def set_valor_por_projeto(self, valor_por_projeto):
        self.validacao_valor_projeto(valor_por_projeto)
        self._valor_por_projeto = valor_por_projeto
        

    def calcular_salario(self):
      
        return self._valor_por_projeto

        
from Funcionario import Funcionario
from FuncionarioHora import FuncionarioHora
from FuncionarioMensal import FuncionarioMensal
from FuncionarioComissionado import FuncionarioComissionado
from FuncionarioProjeto import FuncionarioProjeto
import calendar
from datetime import date


def processar_pagamento(funcionario: Funcionario):
    print(f"Nome: {funcionario.nome}")
    print(f"Salário: {funcionario.calcular_salario()}\n")
    print("---------------------------------")

def simular_pagamento_mensal(funcionario: FuncionarioHora, mes: int, ano: int, feriados: list):
    dias_uteis = 0
    total_horas = 0


    num_dias = calendar.monthrange(ano, mes)[1]

    for dia in range(1, num_dias + 1):
        data_atual = date(ano, mes, dia)
        

        if data_atual.weekday() < 5 and data_atual not in feriados:  
            dias_uteis += 1
            total_horas += 8 

    funcionario.set_horas_trabalhadas = total_horas 
    salario = funcionario.calcular_salario()  


    print(f"Pagamento para {funcionario.nome} em {calendar.month_name[mes]}:")
    print(f"  Salário: R${salario:.2f}")
    print(f"  Horas Trabalhadas: {total_horas} horas")
    print(f"  Feriados: {', '.join([f'{f.day}/{f.month}' for f in feriados])}")
    print("---------------------------------")


def main():
    funcionarios = []

    feriados = [date(2024, 12, 25), date(2024, 1, 1)] 

    try:
        funcionarios.append(FuncionarioHora("Antônio", 123456, 160, 25)) 
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
    for funcionario in funcionarios:
        if isinstance(funcionario, FuncionarioHora):
            simular_pagamento_mensal(funcionario, 10, 2024, feriados)
        
  

if __name__ == "__main__":
    main()


  

        