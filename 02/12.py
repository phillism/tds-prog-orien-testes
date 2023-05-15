""""
Lista2_q12: Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
Para isso são dados:
o cartão gabarito;
o número de alunos da turma;
o cartão de respostas para cada aluno, contendo o seu número e suas respostas.
"""


def receber_gabarito():
    while True:
        gabarito = input("Digite o gabarito (exemplo: ABEDAEDA): ").upper()
        if gabarito is None or gabarito == '':
            print("Gabarito inválido. Tente novamente!")
        else:
            letras = ['A', 'B', 'C', 'D', 'E']
            valido = True
            for w in gabarito:
                if not w in letras:
                    print("Gabairto inválido: digite apenas as letras de A à E.")
                    valido = False
                    break

            if len(gabarito) != 30:
                print(
                    f"O gabarito deve conter 30 questões! Você só colocou {len(gabarito)}.")
                continue

            if valido:
                return gabarito


def receber_numero(msg=" - Digite um número: "):
    while True:
        try:
            numero = int(input(msg))

            if numero < 0:
                print("Digite um valor maior do que zero!")
                continue

            return numero
        except ValueError:
            print("Digite um valor válido!")
            continue


def main():
    gabarito = receber_gabarito()
    quantidade_alunos = receber_numero("Digite a quantidade de alunos: ")

    gabaritos = []

    for i in range(quantidade_alunos):
        while True:
            print(f"\n[Gabarito {i+1}° aluno(a):]")
            gabarito_aluno = receber_gabarito()
            print("Gabarito salvo com sucesso!\n")
            gabaritos.append((i, gabarito_aluno))
            break

    print("-=-=-=-=-=-=-=-=-=-")
    print("Número de acertos de cada aluno (pela chamada):")
    for i in gabaritos:
        n = i[0]
        g = i[1]

        acertos = 0
        contador = 0
        for j in gabarito:
            gabarito_correto = gabarito[contador]
            gabarito_aluno = g[contador]
            if gabarito_correto == gabarito_aluno:
                acertos += 1

            contador += 1

        print(f" - {n + 1}: {acertos} acerto(s) | {abs(acertos - 30)} erros(s)")


if __name__ == "__main__":
    main()
