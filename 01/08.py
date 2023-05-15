"""
Lista1_q8 - Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se
o caractere não for nem 'S' nem 'N', a função imprime a mensagem: 'Caractere inválido. Tente novamente!'. Use esta função em um
programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.
"""


def receber_numero():
    while True:
        try:
            n = int(input("Digite um número: "))
            return n
        except ValueError:
            print("Valor inválido. Tente novamente!")


def main():
    while True:
        continuar = input("(S/N): ").upper()[0]

        if continuar == "S":
            n = receber_numero()
            print(n ** 3)
        elif continuar == "N":
            break

        else:
            print("Caractere inválido. Digite novamente!")


if __name__ == "__main__":
    main()
