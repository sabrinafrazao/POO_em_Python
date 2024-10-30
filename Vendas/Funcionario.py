class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario


def autenticar_acesso(func):
    def wrapper(self, *args, **kwargs):
        if self.usuario_atual.cargo == "Gerente":
            return func(self, *args, **kwargs)
        else:
            print("Acesso negado: Apenas gerentes podem aumentar o salário.")
    return wrapper