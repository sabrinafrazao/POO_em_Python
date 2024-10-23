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