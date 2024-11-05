from Conta import Conta
from excecoes import LimiteExcedidoError, SaldoInsuficienteError, ContaDestinoInvalidaError


def main():
    try:
        conta1 = Conta("João", 500, 1000)
        conta2 = Conta("Maria", 1000, 1500)

        conta1.depositar(200)
        conta1.sacar(100)
        conta1.transferir(700, conta2)
        conta1.transferir(300, None)  
    except SaldoInsuficienteError as e:
        print(e)
    except LimiteExcedidoError as e:
        print(e)
    except ContaDestinoInvalidaError as e:
        print(e)


if __name__ == '__main__':
    main()