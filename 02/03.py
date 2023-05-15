"""
Lista2_q3 - Faça um programa que dada a sequência de n números, imprima-la na ordem inversa à da leitura.
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
    quantidade = receber_numero(
        "Digite a quantidade de números a serem lidos: ")
    numeros = receber_numeros(quantidade)

    print(f"Lista com posição original: {numeros}")
    numeros.reverse()
    print("-=" * 17)
    print(f"Lista com posição reversa: {numeros}")


if __name__ == "__main__":
    main()
