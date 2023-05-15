"""
Lista4_q1: Escreva uma função que recebe uma lista com n números inteiros, retornar uma
lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]
"""

def remover_repetidos(lista: list):
    if type(lista) != list:
        return Exception

    nova_lista = []
    for n in lista:
        if type(n) != int:
            return Exception
        
        if n not in nova_lista:
            nova_lista.append(n)
        
    return nova_lista


assert remover_repetidos(None) == Exception
assert remover_repetidos('1, 2, 3') == Exception
assert remover_repetidos((1, 2, 3, 4, 5)) == Exception
assert remover_repetidos({ "1", "2" }) == Exception
assert remover_repetidos(['1', '2', '3']) == Exception
assert remover_repetidos([None, 2, 3]) == Exception
assert remover_repetidos(['1', 2, 3]) == Exception
assert remover_repetidos([1, [2], 3]) == Exception
assert remover_repetidos([1, 2, str]) == Exception
assert remover_repetidos([1, 2, 3.0]) == Exception
assert remover_repetidos([1.3, 2, 3]) == Exception
assert remover_repetidos([1, 1.0, 3]) == Exception
assert remover_repetidos([]) == []
assert remover_repetidos([1]) == [1]
assert remover_repetidos([1, 2, 3]) == [1, 2, 3]
assert remover_repetidos([2, 1, 3]) == [2, 1, 3]
assert remover_repetidos([5, 4, 5, 7, 3, 4]) == [5, 4, 7, 3]
assert remover_repetidos([2, 2, 3, 4, 7, 4, 2]) == [2, 3, 4, 7]

print("Todos os testes passaram.")
