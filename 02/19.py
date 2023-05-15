""""
Lista2_q19: Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
de S. Escrever a lista X.
"""


def receber_numero(msg=" - Digite um número: "):
    while True:
        try:
            numero = int(input(msg))

            return numero
        except ValueError:
            print("Digite um valor válido!")
            continue


def receber_numeros(quantidade: int):
    numeros = []
    for i in range(0, quantidade):
        numeros.append(receber_numero())

    return numeros


def main():
    r = receber_numeros(5)
    s = receber_numeros(10)
    x = r + s

    print(f"Lista R: {r}")
    print(f"Lista S: {s}")
    print(f"Lista X: {x}")


if __name__ == "__main__":
    main()
