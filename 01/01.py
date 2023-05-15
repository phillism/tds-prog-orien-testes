"""Lista1_q1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele
 for par e falso se for ímpar."""

def par_impar(n):
    if n % 2 == 0:
        return True
    return False

while True:
    try:
        num = int(input("\nDigite um número: "))
        if par_impar(num) == True:
            print(f"\nO número {num} é par.")
        else:
            print(f"\nO número {num} é ímpar.")
    except:
        print("\nNúmero inválido. Tente novamente!")
