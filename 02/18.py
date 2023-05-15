""""
Lista2_q18: Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.
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
    x = receber_numeros(10)
    r = []

    for i in x:
        if i < 0:
            r.append(i)

    print(f"Lista X: {x}")
    print(f"Lista R: {r}")


if __name__ == "__main__":
    main()
