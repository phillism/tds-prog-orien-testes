"""
Lista4_q4: Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma de qualquer seguimento da lista. Ex: Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9,
-6, 4, 1] = 34
"""

def maior_soma(lista: list):

    if type(lista) != list or len(lista) <= 1:
        return Exception

    if any(type(v) != int for v in lista):
        return Exception

    maior = 0
    for i, n in enumerate(lista):
        if type(n) != int:
            return Exception

        for c in range(1, len(lista) + 1):
            if (i + c) > len(lista):
                break

            next = lista[i:i + c]

            if sum(next) > maior:
                maior = sum(next)
    
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
assert maior_soma([-1, -2, -3, 1, 2, 3]) == 6
assert maior_soma([1, 2, 3, 4, 5, 6, -50, 9, 9, 9, 9, 9]) == 45
assert maior_soma([1, 2, 3, 4, 5, 6, -50, 9, 9, 9, 9]) == 36
assert maior_soma([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 34
assert maior_soma([5, -2, -2, -7, 3, 15, 10, -3, 9, 6, -6, 1]) == 40

print("Todos os testes passaram.")
