""""
Lista2_q15: Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
por diante. Escrever todo a lista D e todo a lista E.
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

    d = c[:]
    c.reverse()
    e = c

    print(f"Lista D: {d}")
    print(f"Lista E: {e}")


if __name__ == "__main__":
    main()
