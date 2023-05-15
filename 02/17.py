""""
Lista2_q17: Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
aparece.

Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.
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
    w = receber_numeros(10)
    v = receber_numero("Digite o valor de V: ")

    if not v in w:
        print("Não ocorreu nenhuma vez.")
        return

    print("Quantidade de vezes que ocorreu o valor V na lista W:")
    quantidade = 0
    for i, value in enumerate(w):
        if v == value:
            print(f" - {i}° posição")
            quantidade += 1

    print(f"Total: {quantidade} vez(es)")


if __name__ == "__main__":
    main()
