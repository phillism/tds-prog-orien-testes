"""
Lista1_q6 - Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:

  - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor de seu perímetro;
  - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área;
  - Se o número de lados for igual a 5, escrever PENTÁGONO.
"""


def receber_lados():
    while True:
        try:
            lados = int(input("Digite a quantidade de lados de seu polígono: "))

            if lados < 3 or lados > 5:
                print("O intervalo deve estar entre 3 e 5. Tente novamente!")
            else:
                return lados
        except ValueError:
            print("Digite um valor válido! Tente novamente!")


def receber_medida():
    while True:
        try:
            medida = float(input("Digite a medida de cada lado de seu polígono: "))

            if medida <= 0:
                print("Sua medida deve ser maior do que 0!")
            else:
                return medida
        except ValueError:
            print("Digite um valor válido! Tente novamente!")


def imprimir_valores(lados: int, medida: float):
    if lados == 3:
        print("TRIÂNGULO")
        print(f"Perímetro: {medida * 3:.02f}cm")

    elif lados == 4:
        print("QUADRADO")
        print(f"Área: {medida ** 2:.02f}cm²")

    elif lados == 5:
        print("PENTÁGONO")


def main():
    lados = receber_lados()
    medida = receber_medida()

    imprimir_valores(lados, medida)


if __name__ == "__main__":
    main()
