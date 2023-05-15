"""
Lista1_q15 - Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo N e retorna o valor de S.

  S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... + (t ^ 2 + 1) / (t + 3)
"""


def ler_numero(msg: str):
    while True:
        try:
            n = int(input(msg))

            if n <= 0:
              print("Digite um número maior que zero!")
              continue

            return n
        except ValueError:
            print("Número inválido. Tente novamente!")


def main():
    n = ler_numero("Digite um valor: ")
    acumulador = 0

    for i in range(1, n + 1):
        acumulador += (i ** 2 + 1) / (i + 3)

    print(acumulador)


if __name__ == "__main__":
    main()
