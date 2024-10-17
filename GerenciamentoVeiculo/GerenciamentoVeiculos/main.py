from GerenciamentoVeiculos.VeiculoAlugar import VeiculoAlugar
from GerenciamentoVeiculos.Carro import Carro
from GerenciamentoVeiculos.Moto import Moto

def main():

    carro = Carro(nome="Honda Civic", ano=2020, valor_diario=200, tipo_combustivel="Gasolina")
    
    dias_aluguel = 10
    desconto = 10 
    desconto_extra = 5 
    print(f"Aluguel de {dias_aluguel} dias sem desconto extra do carro: R${carro.calculo_total_aluguel(dias_aluguel, desconto):.2f}")
    print(f"Aluguel de {dias_aluguel} dias com desconto extra do carro: R${carro.desconto_extra(dias_aluguel, desconto, desconto_extra):.2f}")
    
  
    moto = Moto(nome="Yamaha MT-07", ano=2021, valor_diario=150, cilindrada=689)
    

    dias_aluguel_moto = 5
    print(f"Aluguel de {dias_aluguel_moto} dias da moto: R${moto.calculo_total_aluguel(dias_aluguel_moto):.2f}")
    print(f"Custo adicional por cilindrada da moto: R${moto.custo_cilindrada(dias_aluguel_moto):.2f}")
    

if __name__ == "__main__":
    main()
