"""
Lista4_q8: Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor
mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5
"""

def mais_proximo_media(lista: list):
    if type(lista) != list:
        return Exception
    
    if any(type(v) not in [int, float] for v in lista):
        return Exception
    
    if not lista:
        return Exception
    
    media = sum(lista) / len(lista)
    lista = list(set(lista))
    
    difs = []
    for n in lista:
        difs.append(abs(n - media))
    
    return lista[difs.index(min(difs))]


assert mais_proximo_media(None) == Exception
assert mais_proximo_media('1, 2, 3') == Exception
assert mais_proximo_media((1, 2, 3, 4, 5)) == Exception
assert mais_proximo_media({ "1", "2" }) == Exception
assert mais_proximo_media(['1', '2', '3']) == Exception
assert mais_proximo_media([None, 2, 3]) == Exception
assert mais_proximo_media(['1', 2, 3]) == Exception
assert mais_proximo_media([1, [2], 3]) == Exception
assert mais_proximo_media([1, 2, str]) == Exception
assert mais_proximo_media([]) == Exception
assert mais_proximo_media([3.5, 4.5, 2.5, 5.5, 1.5]) == 3.5
assert mais_proximo_media([-10, -5, 0, 5, 10]) == 0
assert mais_proximo_media([7, 8, 9, 10, 8.3]) == 8.3
assert mais_proximo_media([1, 1, 2, 3, 4]) == 2
assert mais_proximo_media([1, 3, 3, 3, 6]) == 3
assert mais_proximo_media([1.1, 2.2, 3.3, 4.4, 5.5, 6.6]) == 3.3
assert mais_proximo_media([1, 2, 3, 5, 6]) == 3
assert mais_proximo_media([2, 2, 3, 3, 3, 4, 4, 4, 12, 10, 5.0, 4, 8, 9, 3, 3]) == 5.0

print("Todos os testes passaram.")
