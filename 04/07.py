"""
Lista4_q7: Escreva uma função que recebe uma lista com n números inteiros, e retorna True
caso algum elemento apareça mais de uma vez ou False caso nenhum elemento
apareça mais de uma vez. Ex [1, 2, 3, 1] = True. Ex. [3, 7, 2, 4] = False
"""

def numero_repete(lista: list):
    if type(lista) != list:
        return Exception
    
    if any(type(v) != int for v in lista):
        return Exception
    
    for i, v in enumerate(lista):
        if v in lista[:i]:
            return True

    return False 


assert numero_repete(None) == Exception
assert numero_repete('1, 2, 3') == Exception
assert numero_repete((1, 2, 3, 4, 5)) == Exception
assert numero_repete({ "1", "2" }) == Exception
assert numero_repete(['1', '2', '3']) == Exception
assert numero_repete([None, 2, 3]) == Exception
assert numero_repete(['1', 2, 3]) == Exception
assert numero_repete([1, [2], 3]) == Exception
assert numero_repete([1, 2, str]) == Exception
assert numero_repete([1, 2, 3.0]) == Exception
assert numero_repete([1.3, 2, 3]) == Exception
assert numero_repete([]) == False
assert numero_repete([1, 2, 3, 4, 5]) == False
assert numero_repete([5, 4, 3, 2, 1]) == False
assert numero_repete([1, 3, 2, 5, 4]) == False
assert numero_repete([1, 3, 2, 5, 4, 4]) == True
assert numero_repete([1, 3, 2, 5, 4, 1]) == True
assert numero_repete([-3, -2, -1, 0, 1, 2, 3, -3]) == True

print("Todos os testes passaram.")
