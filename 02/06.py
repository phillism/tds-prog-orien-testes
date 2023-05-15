""""
Lista2_q6: Dadas duas listas, uma contendo a quantidade e outra contendo o preço de 20 produtos. Elabore um programa que calcule e exiba o faturamento que é igual a
quantidade x preço. Calcule e exiba também o faturamento total que é a somatória de todos os faturamentos, a média dos faturamentos, quantos faturamentos estão abaixo da média.
"""


def receber_numero(msg=" - Digite um número: "):
    while True:
        try:
            numero = float(input(msg))

            if numero < 0:
                print("Digite um valor maior do que zero!")
                continue

            return numero
        except ValueError:
            print("Digite um valor válido!")
            continue


def receber_numeros(quantidade: int, msg):
    numeros = []
    for i in range(0, quantidade):
        numeros.append(receber_numero(msg.format(i + 1)))

    return numeros


def main():
    quantidades = receber_numeros(20, "Digite a quantidade do {}° produto: ")
    precos = receber_numeros(20, "Digite o preço do {}° produto: ")

    faturamento_total = 0
    for i in range(20):
        faturamento = (quantidades[i]) * (precos[i])
        faturamento_total += faturamento

        print(
            f"  - O faturamento do {i + 1}° produto foi de R$ {faturamento:0.2f}.")

    print(f"Seu faturamento total foi de R$ {faturamento_total:.02f}")

    media_faturamento = faturamento_total / 20
    print(f"Faturamentos que estão abaixo da média:")
    for i in range(20):
        faturamento = (quantidades[i]) * (precos[i])
        if faturamento < media_faturamento:
            print(f"  - {i + 1}° produto: R$ {faturamento:0.2f}")


if __name__ == "__main__":
    main()
