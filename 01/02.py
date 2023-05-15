""" Lista1_q2. Escreva um programa que leia o raio de um circulo que faça duas funções: uma função chamada área que calcula e retorna
a área do círculo, e outra função chamada perímetro que calcula e retorna o perímetro do círculo."""
import math

def get_area(r):
    return math.pi * (r ** 2)


def get_perimetro(r):
    return math.pi * 2 * r


def main():
    while True:
        try:
            raio = float(input("Digite o raio do círculo: "))

            print(f"A área do circulo é {get_area(raio)}")
            print(f"O perimetro do circulo é {get_perimetro(raio)}")    
            break
        except ValueError:
            print("Valor do raio inválido. Tente novamente!")


if __name__ == "__main__":
    main()