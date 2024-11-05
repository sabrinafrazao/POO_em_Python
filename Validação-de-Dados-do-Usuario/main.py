from Usuario import Usuario

def main():
    try:
        usuario1 = Usuario("", 25, "usuario@example.com")  # Nome vazio
    except ValueError as e:
        print(e)

    try:
        usuario2 = Usuario("Ana", "vinte e cinco", "usuario@example.com")  # Idade não é um inteiro
    except TypeError as e:
        print(e)

    try:
        usuario3 = Usuario("Carlos", 30, "usuarioexample.com")  # Email sem "@"
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()