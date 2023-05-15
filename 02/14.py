""""
Lista2_q14: Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
Escrever a lista C modificada.
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
    c = receber_numeros(10)

    print(f"Lista original: {c}")

    for i, v in enumerate(c):
        if v < 0:
            c[i] = 0

    print(f"Lista modificada: {c}")


if __name__ == "__main__":
    main()
