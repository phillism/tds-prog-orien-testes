""""
Lista2_q16: Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
Escrever as listas X e Y.
"""


def receber_numero(msg=" - Digite um número: "):
    while True:
        try:
            numero = int(input(msg))

            if numero < 0:
                print("Digite um valor maior do que zero!")
                continue

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
    x = receber_numeros(10)

    y = []

    for i in x:
        y.append(i / 2 if i % 2 == 0 else i * 3)

    print(f"Lista X: {x}")
    print(f"Lista Y: {y}")


if __name__ == "__main__":
    main()
