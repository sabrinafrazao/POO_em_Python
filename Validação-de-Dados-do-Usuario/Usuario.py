class Usuario:
    def __init__(self, nome, idade, email):
        if not nome:
            raise ValueError("Erro: O nome não pode ser vazio.")
        if not isinstance(idade, int):
            raise TypeError("Erro: A idade deve ser um número inteiro.")
        if "@" not in email:
            raise ValueError("Erro: O email deve conter um '@'.")

        self.nome = nome
        self.idade = idade
        self.email = email