"""
Lista4_q6: Escreva uma função que recebe uma lista com n números inteiros, e retorna True
caso a lista esteja ordenada em ordem ascendente ou False caso não esteja
ordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = False
"""

def esta_ordenada(lista: list):
    if type(lista) != list:
        return Exception
    
    if any(type(v) != int for v in lista):
        return Exception
    
    if not lista:
        return Exception

    return list(range(min(lista), max(lista) + 1)) == lista


assert esta_ordenada(None) == Exception
assert esta_ordenada('1, 2, 3') == Exception
assert esta_ordenada((1, 2, 3, 4, 5)) == Exception
assert esta_ordenada({ "1", "2" }) == Exception
assert esta_ordenada(['1', '2', '3']) == Exception
assert esta_ordenada([None, 2, 3]) == Exception
assert esta_ordenada(['1', 2, 3]) == Exception
assert esta_ordenada([1, [2], 3]) == Exception
assert esta_ordenada([1, 2, str]) == Exception
assert esta_ordenada([1, 2, 3.0]) == Exception
assert esta_ordenada([1.3, 2, 3]) == Exception
assert esta_ordenada([]) == Exception
assert esta_ordenada([1, 2, 3, 4, 5]) == True
assert esta_ordenada([5, 4, 3, 2, 1]) == False
assert esta_ordenada([1, 3, 2, 5, 4]) == False
assert esta_ordenada([1]) == True
assert esta_ordenada([-3, -2, -1, 0, 1, 2, 3]) == True

print("Todos os testes passaram.")
