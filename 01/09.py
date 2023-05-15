"""
Lista1_q9 - Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros
contidos no intervalo [n1, n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.
"""


def ler_numero(msg: str):
    while True:
        try:
            n = int(input(msg))
            return n
        except:
            print("Número inválido. Tente novamente!")


def somar_intervalo(n1, n2):
    maior = max(n1, n2)
    menor = min(n1, n2) + 1
    
    acumulador = 0

    for i in range(menor, maior):
        acumulador += i

    return acumulador


def main():
    n1 = ler_numero("Digite o primeiro número: ")
    n2 = ler_numero("Digite o segundo número: ")

    print(f"Soma do intervalo: {somar_intervalo(n1, n2)}")
    pass


if __name__ == "__main__":
    main()
