""""
Lista2_q5: Faça um programa que leia duas listas de 10 elementos numéricos cada um, e intercale os elementos desde em uma outra lista de 20 elementos.
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
    lista1 = receber_numeros(10)
    lista2 = receber_numeros(10)
    nova_lista = []

    nova_lista.extend(lista1)
    nova_lista.extend(lista2)
    print(f"Primeira lista: {lista1}")
    print(f"Segunda lista: {lista2}")

    print("-=" * 60)

    nova_lista.sort()
    print(f"Lista intercalada: {nova_lista}")


if __name__ == "__main__":
    main()
