"""
Lista4_q9: Escreva uma função que recebe uma lista com n números inteiros, retornar uma
lista eliminando todas as ocorrências de valores repetidos. Ex: [5, 4, 5, 7, 3, 4] =
[7, 3]
"""


def remover_repetidos(lista):
    if type(lista) != list:
        return Exception

    if any(type(v) != int for v in lista):
        return Exception

    for n in lista:
        if lista.count(n) != 1:
            while n in lista:
                lista.remove(n)
    
    return lista

assert remover_repetidos(None) == Exception
assert remover_repetidos('1') == Exception
assert remover_repetidos({}) == Exception
assert remover_repetidos((1, 2, 3)) == Exception
assert remover_repetidos([1, 2, 3, '4']) == Exception
assert remover_repetidos(['1', 2, 3, 4]) == Exception
assert remover_repetidos([1, 2, 3, 4.0]) == Exception
assert remover_repetidos([1, 2.5, 3, 4]) == Exception
assert remover_repetidos([]) == []
assert remover_repetidos([1]) == [1]
assert remover_repetidos([1, 2, 3]) == [1, 2, 3]
assert remover_repetidos([1, 2, 3, 3]) == [1, 2]
assert remover_repetidos([1, 1, 2, 3, 2, 4, 5]) == [3, 4, 5]
assert remover_repetidos([5, 4, 5, 7, 3, 4]) == [7, 3]
assert remover_repetidos([5, 4, 5, 7, 3, 4, 10, 12, 5, 4, 3, 2, 1]) == [7, 10, 12, 2, 1]

print("Todos os testes passaram.")
