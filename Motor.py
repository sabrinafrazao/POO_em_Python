class Motor:
    def ligar(self):
        print("Motor ligado!")


class Carro:

    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor()

    def dirigir(self):
        print(f"Dirigindo o carro {self.modelo}")
        self.motor.ligar()



carro = Carro("fusca")
carro.dirigir()