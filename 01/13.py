"""
Lista1_q13 - Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo N e retorna o valor de S.

  S = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/N.
"""


def calcular_formula(n: int):
    acumulador = 0
    for i in range(1, n + 1):
        acumulador += 1 / i
      
    return acumulador  
    


def ler_numero(msg: str):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Número inválido. Tente novamente!")


def main():
    n = ler_numero("Digite um número: ")
    valor = round(calcular_formula(n), 2)

    print(valor)


if __name__ == "__main__":
    main()
