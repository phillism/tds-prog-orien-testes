"""
Lista2_q1. Faça um programa que grave uma lista de 100 elementos numéricos, inteiros e:
  a) mostra a quantidade de números pares;
  b) grave uma lista somente com os números pares e mostre na lista;
  c) mostre a quantidade de números ímpares;
  d) grave uma lista somente com os números ímpares e mostre a lista
"""


def is_par(n: int):
    return n % 2 == 0


def receber_numero():
    while True:
        try:
            numero = int(input(" - Digite um número: "))
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
    numeros = receber_numeros(100)

    pares = []
    impares = []

    for i in numeros:
        if is_par(i):
            pares.append(i)
        else:
            impares.append(i)

    print("Pares:")
    print(f"  - {pares}")
    print(f"  - Quantidade de numeros pares: {len(pares)}")
    print("-=" * 16)
    print("Ímpares:")
    print(f"  - {impares}")
    print(f"  - Quantidade de numeros ímpares: {len(impares)}")


if __name__ == "__main__":
    main()
