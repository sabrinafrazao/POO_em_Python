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
        self._valor_por_projeto = valor_por_projeto
        

    def calcular_salario(self):
      
        return self._valor_por_projeto

        
   

        