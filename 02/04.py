""""
Lista2_q4: Faça um programa que grave uma lista com 15 posições, calcule e mostre:
  a) o maior elemento da lista e em que composição este elemento se encontra;
  b) o menor elemento da lista e em que posição este elemento se encontra.
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
    maior_index = numeros.index(maior)

    menor = min(numeros)
    menor_index = numeros.index(menor)

    print(f"O maior número é {maior}, e sua posição é {maior_index}")
    print(f"O menor número é {menor}, e sua posição é {menor_index}")


if __name__ == "__main__":
    main()
