"""
Lista2_q2 - Faça um programa que grave uma lista com 10 números reais, calcule e motre a quantidade de números negativos e a soma dos números positivos desta lista.
"""


def receber_numero():
    while True:
        try:
            numero = float(input(" - Digite um número: "))
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
    numeros = receber_numeros(10)

    negativos = []
    positivos = []

    for n in numeros:
        if n < 0:
            negativos.append(n)
        else:
            positivos.append(n)

    print("Números negativos:")
    print(f"  - Quantidade: {len(negativos)}")
    print(f"  {negativos}")

    print("-=" * 17)

    print("Números positivos:")
    print(f"  - Quantidade: {len(positivos)}")
    print(f"  - {positivos}")


if __name__ == "__main__":
    main()
