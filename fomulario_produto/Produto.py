class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.qdt = 0

    def exibir(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade em estoque: {self.qtd}")

    def atualizar(self, nova_qtd):
    
        if nova_qtd >= 0:
            self.qtd = nova_qtd
            print(f"A quantidade de {self.nome} foi atualizada para {self.qtd} unidades.")


        
