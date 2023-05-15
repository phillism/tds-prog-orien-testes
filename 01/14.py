"""
Lista1_q14 - Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo N e retorna o valor de S.

  S = 1 + S + 1/1! + 1/2! + 1/3! + 1 / N!
"""


def get_fatorial(n: int):
    fatorial = 1
    counter = 2
    while counter <= n:
        fatorial *= counter
        counter += 1

    return fatorial


def calcular_formula(n: int):
    acumulador = 0
    for i in range(1, n + 1):
        acumulador += 1 / get_fatorial(i)
      
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
    valor = calcular_formula(n)
    print(f"{valor}")


if __name__ == "__main__":
    main()
