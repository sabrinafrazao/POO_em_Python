from Funcionario import Funcionario
from FuncionarioHora import FuncionarioHora
from FuncionarioMensal import FuncionarioMensal
from FuncionarioComissionado import FuncionarioComissionado
from FuncionarioProjeto import FuncionarioProjeto
import datetime


def processar_pagamento(funcionario:Funcionario):
    print(f"Nome: {funcionario.nome}")
    print(f"Salário: {funcionario.calcular_salario()}\n")
    print("---------------------------------")


def main():
    
    funcionario_horista = FuncionarioHora("Antônio", 123456, 80, 25)
    Funcionario_Mesalista = FuncionarioMensal("Diego", 432335, 4560)
    Funcionario_Comissionado = FuncionarioComissionado("Jonas", 567786, 3000, 5000, 0.05)
    Funcionario_Projeto =  FuncionarioProjeto("Sabrina", 5679, 1000000)

    funcionarios = [funcionario_horista,Funcionario_Mesalista,Funcionario_Comissionado, Funcionario_Projeto]

    for funcionario in funcionarios:
        processar_pagamento(funcionario)
        

if __name__ =="__main__":
    main()

