"""
Lista4_q3: Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
4, 1] = 25
"""

def maior_soma(lista: list):
    if type(lista) != list or len(lista) <= 1:
        return Exception

    maior = 0
    for i, valor in enumerate(lista, 1):
        if len(lista) <= i:
            break

        proximo_valor = lista[i]
        if any(type(v) != int for v in [valor, proximo_valor]):
            return Exception

        soma_valores = valor + proximo_valor
        if soma_valores > maior:
            maior = soma_valores

    
    return maior


assert maior_soma(None) == Exception
assert maior_soma('1, 2, 3') == Exception
assert maior_soma((1, 2, 3, 4, 5)) == Exception
assert maior_soma({ "1", "2" }) == Exception
assert maior_soma(['1', '2', '3']) == Exception
assert maior_soma([None, 2, 3]) == Exception
assert maior_soma(['1', 2, 3]) == Exception
assert maior_soma([1, [2], 3]) == Exception
assert maior_soma([1, 2, str]) == Exception
assert maior_soma([1, 2, 3.0]) == Exception
assert maior_soma([1.3, 2, 3]) == Exception
assert maior_soma([]) == Exception
assert maior_soma([1]) == Exception
assert maior_soma([1, 2]) == 3
assert maior_soma([1, 2, 3]) == 5
assert maior_soma([3, 1, 2]) == 4
assert maior_soma([1, 2, 3, 4, 5]) == 9
assert maior_soma([1, 4, 5, 2, 3]) == 9
assert maior_soma([4, 5, 1, 2, 3]) == 9
assert maior_soma([1, 2, 8, 1, 9, 0, 2, 3]) == 10
assert maior_soma([1, 2, 8, 1, 9, 0, 2, 3]) == 10

print("Todos os testes passaram.")
