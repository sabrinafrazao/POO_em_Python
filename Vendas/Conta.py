class Conta:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, tipo, valor):
        self.transacoes.append({"tipo": tipo, "valor": valor})

    def filtrar_transacoes_por_tipo(self, tipo):
        return list(filter(lambda t: t["tipo"] == tipo, self.transacoes))

    def aplicar_taxa(self, taxa):
        self.transacoes = list(map(lambda t: {"tipo": t["tipo"], "valor": t["valor"] * (1 - taxa) if t["tipo"] == "Saque" else t["valor"]}, self.transacoes))
