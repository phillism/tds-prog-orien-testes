""" Lista1_q4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que 
receba as duas notas por parâmetro e calcule e escreva a média semestral e a mensagem "PARABÉNS! Você foi aprovado!" 
somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação)."""

def media (nota1: float, nota2:float):
    return (nota1 + nota2) / 2


def main():
    while True:
        try:
            aluno = input("Digite o nome do aluno: ")
            nota1 = float(input(f"Digite a 1ª nota de {aluno}: "))
            nota2 = float(input(f"Digite a 2ª nota de {aluno}: "))

            print(f"A média de {aluno} é igual a {media(nota1, nota2):.2f}")
            break
        except ValueError:
            print("Nota informada inválida. Tente novamente!")


if __name__ == "__main__":
    main()
