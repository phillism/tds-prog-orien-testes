""" Lista1_q5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma: 1: feminino, 2: masculino) 
de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e que calcule e 
retorne seu peso ideal, utilizando as seguintes fórmulas: para homens (72.7 * h) - 58 e para mulheres: (62.1 * h) - 44.7. 
Observação: Altura = h (na fórmula acima)."""

def receber_altura():
    while True:
        try:
            h = float(input("Insira sua altura: "))
            return h
        except ValueError:
            print("A altura informada está incorreta. Tente novamente!")


def receber_genero():
    def_message = "Gênero inválido! Tente novamente."

    while True:
        try:
            while True:
                g = int(input("Digite seu gênero (1 = feminino; 2 = masculino): "))
                if g == 1 or g == 2:
                    return g
                else:
                    print(def_message)
        except:
            print(def_message)


def peso_ideal(height: float, gender: int):
    if gender == 1:
        return (62.1 * height) - 44.7
    
    return (72.7 * height) - 58


def main():
    height = receber_altura()
    gender = receber_genero()

    p_ideal = peso_ideal(height, gender)
    print(f"Seu peso ideal seria {p_ideal:0.2f}.")


if __name__ == "__main__":
    main()
