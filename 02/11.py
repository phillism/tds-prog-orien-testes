""""
Lista2_q11: Faça um programa que alimente uma lista com um número de posições definidas pelo usuário.
Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.

  ==== =MENU========
    0) Sair do programa
    1)Cadastar nome
    2)Pesquisar nome
    3)Listar todos os nome
"""


def receber_opcao():
    while True:
        try:
            numero = int(input("Digite uma das opções acima: "))

            if numero < 0 or numero > 3:
                print("Opção inválida!")
                continue

            return numero
        except ValueError:
            print("Digite um valor válido!")
            continue


def main():
    nomes = []
    print("""
  ==== =MENU========
      1)Cadastar nome
      2)Pesquisar nome
      3)Listar todos os nome
      0) Sair do programa
  ——————–:""")

    while True:
        opcao = receber_opcao()

        if opcao == 0:
            break

        if opcao == 1:
            while True:
                nome = input("Digite o nome a ser cadastrado: ")
                if nome in nomes:
                    print("Este nome já foi cadastrado.")
                elif nome == '':
                    print("Digite um nome válido!")
                else:
                    nomes.append(nome)
                    print(f"Nome '{nome}' adicionado.")
                    break

        if opcao == 2:
            nome = input("Digite o nome a ser pesquisado: ")
            if nome in nomes:
                print(f"Nome encontrado na {nomes.index(nome) + 1}° posição.")
            else:
                print("Nome não encontrado.")

        if opcao == 3:
            print("Lista de nomes:")
            for i in nomes:
                print(f"  - {nomes.index(i) + 1}°: {i}")

    print("Programa fechado.")


if __name__ == "__main__":
    main()
