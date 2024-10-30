from Venda import Venda
from HistoricoVendas import HistoricoVendas
from Funcionario import Funcionario, autenticar_acesso

class SistemaRH:
    def __init__(self, usuario_atual):
        self.funcionarios = []
        self.usuario_atual = usuario_atual

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    @autenticar_acesso
    def aumentar_salario(self, percentual):
        for funcionario in self.funcionarios:
            funcionario.salario += funcionario.salario * (percentual / 100)