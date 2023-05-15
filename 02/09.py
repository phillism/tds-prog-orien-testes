""""
Lista2_q9: Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.
"""


def receber_numero(msg=" - Digite um número: "):
    while True:
        try:
            numero = int(input(msg))

            if numero <= 0:
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
    numeros = receber_numeros(5)

    print(f"Lista com posição original: {numeros}")
    numeros.reverse()
    print("-=" * 17)
    print(f"Lista com posição reversa: {numeros}")


if __name__ == "__main__":
    main()
