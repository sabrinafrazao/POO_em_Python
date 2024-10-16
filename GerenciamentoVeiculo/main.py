from Moto import Moto

def main():

    moto1 = Moto("Moto A", 2023, 100, 250)  
    moto2 = Moto("Moto B", 2023, 100, 150) 

    dias = 5

    custo_moto1 = moto1.custo_cilindrada(dias)
    custo_moto2 = moto2.custo_cilindrada(dias)

    print(f"Custo do aluguel da {moto1._nome} por {dias} dias (cilindrada {moto1.cilindrada}cc): R$ {custo_moto1:.2f}")
    print(f"Custo do aluguel da {moto2._nome} por {dias} dias (cilindrada {moto2.cilindrada}cc): R$ {custo_moto2:.2f}")
    

if __name__ == "__main__":
    main()