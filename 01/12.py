"""
Lista1_q12 - Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.
"""


def ler_numero(msg: str):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Número inválido. Tente novamente!")


def get_somatorio(n: int):
    acumulador = 0
    for i in range(1, n + 1):
        acumulador += i

    return acumulador


def main():
    while True:
        n = ler_numero("Digite um número: ")
        if n <= 0:
            print("Digite um número maior que 0. Tente novamente!")
        else:
            print(f"Somatório: {get_somatorio(n)}")
            break


if __name__ == "__main__":
    main()
