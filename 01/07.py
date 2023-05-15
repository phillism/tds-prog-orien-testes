"""
Lista1_q7 - Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de N(-1)!;
este por sua vez depende de (N-2)!; e assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo.
Utilize uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial
deste número, também do tipo inteiro.
"""


def get_fatorial(n: int):
    fatorial = 1
    counter = 2
    while counter <= n:
        fatorial *= counter
        counter += 1

    return fatorial


def main():
    while True:
        try:
            n = int(input("Digite um número: "))

            if n <= 0:
                print("Este número tem que ser maior do que 0. Tente novamente!")
            else:
                print(f"O fatorial deste número é: {get_fatorial(n)}")
                break
        except ValueError:
            print("Número inválido. Tente novamente!")
    pass


if __name__ == "__main__":
    main()
