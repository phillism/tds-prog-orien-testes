""""
Lista2_q12: Faça um programa que grave uma lista com 15 posições, calcule e mostre:
  a) O maior elemento da lista e em que posição esse elemento se encontra;
  b) O menor elemento da lista e em que posição esse elemento se encontra.
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
    numeros = receber_numeros(15)

    maior = max(numeros)
    menor = min(numeros)

    print(f"Posição do maior elemento da lista: {numeros.index(maior) + 1}°")
    print(f"Posição do menor elemento da lista: {numeros.index(menor) + 1}°")


if __name__ == "__main__":
    main()
