""" Lista1_q3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada Celsius para calcular
e retornar o valor correspondente em graus Celsius:

Fórmula: C = ((F - 32)/9) * 5"""

def celsius(fah: float):
    return ((fah - 32) / 9) * 5


def main():
    while True:
        try:
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius_transformado = celsius(fahrenheit)
            print(f"A temperatura em Celsius é: {celsius_transformado}°C")
            break

        except ValueError:
            print("Digite um valor válido. Tente novamente!")

if __name__ == "__main__":
    main()
