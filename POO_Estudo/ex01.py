dobrar = lambda x: x * 2 

print(dobrar(5))


produto = [
    {"nome": "Camisa", "preco":50},
    {"nome": "Calça", "preco": 100},
    {"nome": "Sapato", "preco": 200}
]

produto_ordenadas =sorted(produto, key=lambda produto: produto["preco"])
print(produto_ordenadas)

numeros = [ 1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)

temperaturas_celsius = [0, 20, 37, 100]


temperatura_fahrennheit = list(map(lambda c: c * 9/2 + 32, temperaturas_celsius))
print(temperatura_fahrennheit)
numeros = [ 1, 2, 3, 4, 5]

numeros_quadrados = list(map(lambda x : x **2, numeros))
print(numeros_quadrados)


numeros = [ 1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

palavras = ["Python", "é", "incrivel", "para", "data", "science"]
palavras_longas = list(filter(lambda palavra: len(palavra)> 5, palavras))
print(palavras_longas)


numeros = [1, 2, 3, 4]
quadrados = [x ** 2 for x in numeros]
print(quadrados)

numeros = [1, 2, 3, 4]
quadrado_dict = {x:x ** 2 for x in numeros}
print(quadrado_dict)

numeros = [1, 2, 3, 4]
quadrado_set = {x ** 2 for x in numeros}
print(quadrado_set)



def saudacao_decorator(func):
    def wrapper(nome):
        print("Olá")
        func(nome)
        print("Tenha um bom dia! ")
    return wrapper

@saudacao_decorator
def saudacao(nome):
    print(f"Prazer em conhece - lo {nome}")

saudacao("Alice")


def gerar_pares(limite):
    n = 0

    while n < limite:
        yield n

        n+= 2

for n in gerar_pares(10):
    print(n)