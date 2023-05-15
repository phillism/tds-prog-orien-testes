"""
Lista1_q11 - Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.
"""


def ler_numero(msg: str):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Número inválido. Tente novamente!")


# n = 10
def get_divisores(n: int):
    acumulador = 0
    for i in range(1, n + 1):
        if n % i == 0:
            acumulador += 1

    return acumulador


def main():
    while True:
        n = ler_numero("Digite um número: ")
        if n <= 0:
            print("Digite um número maior que 0. Tente novamente!")
        else:
            print(f"Número de divisores: {get_divisores(n)}")
            break


if __name__ == "__main__":
    main()
