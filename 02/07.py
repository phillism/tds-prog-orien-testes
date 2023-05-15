""""
Lista2_q7: Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
outro valor dado pertence ou não à lista.
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
    quantidades = receber_numeros(10)
    numero = receber_numero(
        "Digite um número, para verificar sua presença na lista de números digitados anteriormente: ")

    if numero in quantidades:
        print("Este número foi digitado anteriormente!")
    else:
        print("Este número não foi digitado anteriormente!")


if __name__ == "__main__":
    main()
