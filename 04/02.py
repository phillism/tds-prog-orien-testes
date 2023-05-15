"""
Lista4_q2: Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
o número de vezes que cada número ocorre na sequência.
"""

def contar_elementos(lista: list):
    if type(lista) != list:
        return Exception

    contagem = {}
    for n in lista:
        if type(n) != int:
            return Exception

        n_str = str(n)
        if n_str in contagem.keys():
            contagem[n_str] += 1
        else:
            contagem[n_str] = 1
    
    return contagem


assert contar_elementos(None) == Exception
assert contar_elementos('1, 2, 3') == Exception
assert contar_elementos((1, 2, 3, 4, 5)) == Exception
assert contar_elementos({ "1", "2" }) == Exception
assert contar_elementos(['1', '2', '3']) == Exception
assert contar_elementos([None, 2, 3]) == Exception
assert contar_elementos(['1', 2, 3]) == Exception
assert contar_elementos([1, [2], 3]) == Exception
assert contar_elementos([1, 2, str]) == Exception
assert contar_elementos([1, 2, 3.0]) == Exception
assert contar_elementos([1.3, 2, 3]) == Exception
assert contar_elementos([1, 1.0, 3]) == Exception
assert contar_elementos([1, 2, 3]) == { "1": 1, "2": 1, "3": 1 }
assert contar_elementos([1, 3, 2]) == { "1": 1, "3": 1, "2": 1 }
assert contar_elementos([1, 1, 2, 3, 2]) == { "1": 2, "2": 2, "3": 1 }
assert contar_elementos([1, 1, 2, 3, 2, 1]) == { "1": 3, "2": 2, "3": 1 }
assert contar_elementos([3, 1, 1, 2, 3, 2, 1]) == { "3": 2, "1": 3, "2": 2 }
assert contar_elementos([9, 3, 1, 1, 2, 3, 2, 1, 6]) == { "9": 1, "3": 2, "1": 3, "2": 2, "6": 1 }

print("Todos os testes passaram.")
