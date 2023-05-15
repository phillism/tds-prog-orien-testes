"""
Lista1_q10 - Escreva um programa composto de uma função Max e o programa principal como segue:
  a) a função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um deles;
  b) o programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função Max.
"""


def Max(n1, n2):
    return n1 if n1 > n2 else n2


def ler_numero(msg: str):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Número inválido. Tente novamente!")


def main():
    serie_atual = 0

    while serie_atual != 4:
        numeros = []
        for i in range(4):
            numeros.append(ler_numero("Digite um número: "))

        a = numeros[0:2]
        b = numeros[2:4]

        maior1 = Max(a[0], a[1])
        maior2 = Max(b[0], b[1])

        print(f"Maior: {Max(maior1, maior2)}")

        serie_atual += 1


if __name__ == "__main__":
    main()
