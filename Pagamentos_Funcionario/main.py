from Funcionario import Funcionario
from FuncionarioHora import FuncionarioHora
from FuncionarioMensal import FuncionarioMensal
from FuncionarioComissionado import FuncionarioComissionado
from FuncionarioProjeto import FuncionarioProjeto
import calendar
from datetime import date, timedelta


def processar_pagamento(funcionario: Funcionario):
    print(f"Nome: {funcionario.nome}")
    print(f"Salário: {funcionario.calcular_salario()}\n")
    print("---------------------------------")


def calcular_horas_uteis_mes(ano, mes, feriados):
  
    horas_por_dia = 8 

    
    dias_uteis = 0

   
    for dia in range(1, calendar.monthrange(ano, mes)[1] + 1):  
        data_atual = date(ano, mes, dia)
        
        # Verificar se é um fim de semana (sábado ou domingo)
        if data_atual.weekday() >= 5:  # Sábado (5) ou Domingo (6)
            continue
        
        # Verificar se é um feriado
        if data_atual in feriados:
            continue
        
        # Se não for nem fim de semana nem feriado, é um dia útil
        dias_uteis += 1

    # Retornar o total de horas úteis no mês
    return dias_uteis * horas_por_dia

def simular_pagamento_mensal(funcionario: FuncionarioHora, mes, ano, feriados):

    horas_trabalhadas_no_mes = calcular_horas_uteis_mes(ano, mes, feriados)
    return funcionario.valor_hora * horas_trabalhadas_no_mes



def main():
    funcionarios = []

    feriados = [date(2024, 12, 25), date(2024, 1, 1)]  # Lista de feriados

    try:
        funcionarios.append(FuncionarioHora("Antônio", 123456, 160, 25))  # Exemplo de funcionário horista
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    try:
        funcionarios.append(FuncionarioMensal("Diego", 432335, 4560))  # Funcionário mensal
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    try:
        funcionarios.append(FuncionarioComissionado("Jonas", 567786, 3000, 5000, 0.05))  # Comissionado
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    try:
        funcionarios.append(FuncionarioProjeto("Sabrina", 5679, 1000000))  # Funcionário por projeto
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    # Processar pagamento de funcionários horistas com cálculo de horas úteis no mês de dezembro de 2024
    for funcionario in funcionarios:
        if isinstance(funcionario, FuncionarioHora):
            salario_mes = simular_pagamento_mensal(funcionario, 12, 2024, feriados)
            print(f"Nome: {funcionario.nome}, Salário em dezembro de 2024: {salario_mes}\n")
        else:
            processar_pagamento(funcionario)


if __name__ == "__main__":
    main()


