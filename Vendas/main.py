from Venda import Venda
from HistoricoVendas import HistoricoVendas
from Funcionario import Funcionario
from SistemaRH import SistemaRH
from Conta import Conta

venda1 = Venda("Produto A", 3, 10.0)
venda2 = Venda("Produto B", 5, 20.0)
venda3 = Venda("Produto A", 2, 10.0)
historico = HistoricoVendas()
historico.adicionar_vendas(venda1)
historico.adicionar_vendas(venda2)
historico.adicionar_vendas(venda3)

print("Total por produto:", historico.total_por_produtos())
print("Vendas acima de 30:")
for venda in historico.listar_vendas_acima_de(30):
    print(f"Produto: {venda.nome}, Total: {venda.total_vendas ()}")

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