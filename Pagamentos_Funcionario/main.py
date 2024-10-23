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


