class Calculadora:

    def __init__(self, peso, h):
        self.peso = peso
        self.h = h
        self.imc = 0.0

    def calcular_imc(self):
        imc_res = self.peso / (self.h**2)
        return imc_res
    
    def resultado_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Magreza"
        elif imc >= 18.5 and imc < 24.9:
            return "Normal"
        elif imc >= 25 and imc <= 29.9:
            return "Sobrepeso"
        elif imc >= 30 and imc <= 34.9:
            return "Obesidade grau I"
        elif imc >= 35 and imc <= 39.9:
            return "Obesidade grau II"
        else:
            return "Obesidade grau III"

        
def main():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))

    print(f"Peso: {peso}, Altura: {altura}")
    
    resultado = Calculadora(peso, altura)
    imc = resultado.calcular_imc()
    faixa = resultado.resultado_imc()
    
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Você está na faixa: {faixa}")

if __name__ == "__main__":
    main()
