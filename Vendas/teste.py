from functools import reduce

# Classe Venda
class Venda:
    def __init__(self, nome_produto, quantidade, preco_unitario):
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def total_venda(self):
        return self.quantidade * self.preco_unitario

# Classe HistoricoVendas
class HistoricoVendas:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        self.vendas.append(venda)

    def total_por_produto(self):
        totais = {}
        for venda in self.vendas:
            totais[venda.nome_produto] = reduce(
                lambda total, v: total + v.total_venda(),
                filter(lambda x: x.nome_produto == venda.nome_produto, self.vendas),
                0
            )
        return totais

    def listar_vendas_acima_de(self, valor):
        for venda in self.vendas:
            if venda.total_venda() > valor:
                yield venda

# Classe Funcionario
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

# Decorator para autenticação de acesso
def autenticar_acesso(func):
    def wrapper(self, *args, **kwargs):
        if self.usuario_atual.cargo == "Gerente":
            return func(self, *args, **kwargs)
        else:
            print("Acesso negado: Apenas gerentes podem aumentar o salário.")
    return wrapper

# Classe SistemaRH
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

# Classe Conta
class Conta:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, tipo, valor):
        self.transacoes.append({"tipo": tipo, "valor": valor})

    def filtrar_transacoes_por_tipo(self, tipo):
        return list(filter(lambda t: t["tipo"] == tipo, self.transacoes))

    def aplicar_taxa(self, taxa):
        self.transacoes = list(map(lambda t: {"tipo": t["tipo"], "valor": t["valor"] * (1 - taxa) if t["tipo"] == "Saque" else t["valor"]}, self.transacoes))


# Teste do código
# Histórico de Vendas
venda1 = Venda("Produto A", 3, 10.0)
venda2 = Venda("Produto B", 5, 20.0)
venda3 = Venda("Produto A", 2, 10.0)
historico = HistoricoVendas()
historico.adicionar_venda(venda1)
historico.adicionar_venda(venda2)
historico.adicionar_venda(venda3)

print("Total por produto:", historico.total_por_produto())
print("Vendas acima de 30:")
for venda in historico.listar_vendas_acima_de(30):
    print(f"Produto: {venda.nome_produto}, Total: {venda.total_venda()}")

# Sistema RH
gerente = Funcionario("João", "Gerente", 5000)
funcionario = Funcionario("Maria", "Analista", 3000)
sistema_rh = SistemaRH(usuario_atual=gerente)
sistema_rh.adicionar_funcionario(funcionario)
sistema_rh.aumentar_salario(10)
print("Salário após aumento:", funcionario.salario)

# Conta e transações
conta = Conta()
conta.adicionar_transacao("Depósito", 1000)
conta.adicionar_transacao("Saque", 200)
conta.adicionar_transacao("Saque", 150)
print("Transações de Saque:", conta.filtrar_transacoes_por_tipo("Saque"))
conta.aplicar_taxa(0.05)
print("Transações após aplicar taxa:", conta.transacoes)
