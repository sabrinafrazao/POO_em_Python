class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info_veiculo(self):
        print(f"Veiculo: {self.marca} {self.modelo}")

    

class Carro(Veiculo):
    
    def __init__(self, marca, modelo, n_portas):
        Veiculo.__init__(self, marca, modelo)
        self.n_portas = n_portas

    def infor_portas(self):
        print(f"O veiculo tem {self.n_portas} rodas")

    
    def infor_completa(self):
        self.info_veiculo()
        self.infor_portas()


veiculo = Carro("Honda", "HB20", 4)

veiculo.infor_completa()
