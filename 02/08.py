""""
Lista2_q8: Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
ocorreu a letra ‘A’.
"""


def receber_mensagem(msg=" - Digite um texto: ") -> str:
    while True:
        mensagem = input(msg)

        if mensagem == '':
            print("Digite uma mensagme válida!")
            continue

        return mensagem


def is_alpha(letter: str) -> bool:
    code = ord(letter.lower())
    return code >= 97 and code <= 122


def main():
    while True:
        msg = receber_mensagem().lower()
        a_counter = 0
        invalido = False
        for c in msg:
            if not is_alpha(c):
                a_counter += 1
                invalido = True

            if c == 'a':
                a_counter += 1

        if not invalido:
            print(f"A letra 'a' foi contabilizada {a_counter} vez(es).")
            break
        else:
            print(
                "Digite apenas mensagens contendo letras do alfabeto (e sem acentuações).")


if __name__ == "__main__":
    main()
