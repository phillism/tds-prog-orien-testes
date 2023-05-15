"""
Lista3_q12: Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os
ordenados em ordem crescente.
"""

def ordenar_crescente(n1, n2):
    if type(n1) != int or type(n2) != int:
        return Exception

    return sorted([n1, n2])    

assert ordenar_crescente([], 3) == Exception
assert ordenar_crescente(9, None) == Exception
assert ordenar_crescente(18, '2') == Exception
assert ordenar_crescente(9, 9.5) == Exception
assert ordenar_crescente(3.3, 1) == Exception
assert ordenar_crescente(9, 0) == [0, 9]
assert ordenar_crescente(2, 1) == [1, 2]
assert ordenar_crescente(1, 2) == [1, 2]
assert ordenar_crescente(0, -35) == [-35, 0]
assert ordenar_crescente(-100, -101) == [-101, -100]
assert ordenar_crescente(-101, -100) == [-101, -100]

print("Todos os testes passaram.")