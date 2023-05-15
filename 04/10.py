"""
Lista4_q10: Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma dos números que se repetem da lista. Ex: [5, -2, -2, 5, 3, 5, 10, -2, 3,
10, 3, 1] = 20
"""


def maior_soma(lista):
    if type(lista) != list or not lista:
        return Exception

    if any(type(v) != int for v in lista):
        return Exception

    somas = []
    for n in set(lista):
        c = lista.count(n)
        if c > 1:
            somas.append(n * c)
    
    return max(somas) if len(somas) != 0 else 0

assert maior_soma(None) == Exception
assert maior_soma('1') == Exception
assert maior_soma({}) == Exception
assert maior_soma((1, 2, 3)) == Exception
assert maior_soma([1, 2, 3, '4']) == Exception
assert maior_soma(['1', 2, 3, 4]) == Exception
assert maior_soma([1, 2, 3, 4.0]) == Exception
assert maior_soma([1, 2.5, 3, 4]) == Exception
assert maior_soma([]) == Exception
assert maior_soma([1]) == 0
assert maior_soma([1, 2, 3]) == 0
assert maior_soma([1, 2, 3, 3]) == 6
assert maior_soma([1, 2, 3, 3, 2, 2, 2]) == 8
assert maior_soma([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]) == 20
assert maior_soma([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1, 5, 5]) == 25
assert maior_soma([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1, 5, 5, 5]) == 30

print("Todos os testes passaram.")
