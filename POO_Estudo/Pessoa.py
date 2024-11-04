class Pessoa:
    numero_de_pessoas = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        Pessoa.numero_de_pessoas +=1 

    @classmethod
    def total_pessoas(cls):
        print(f"Total de pessoas:  {cls.numero_de_pessoas}")


pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("bob", 25)

Pessoa.total_pessoas()

