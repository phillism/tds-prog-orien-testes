""""
Lista2_q13: Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
cada face.
"""

import random


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


def main():
    quant_lancamentos = receber_numero(
        "Digite a quantidade de lançamentos do dado: ")
    ocorrencias = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]

    for i in range(quant_lancamentos):
        n_random = random.randint(1, 7)

        for index, o in enumerate(ocorrencias):
            n = o[0]
            quant = o[1]
            if n == n_random:
                quant += 1
                ocorrencias[index] = (n, quant)

    print("Número de ocorrencias de cada face:")
    for o in ocorrencias:
        print(f" - {o[0]}: {o[1]} vez(es)")


if __name__ == "__main__":
    main()
