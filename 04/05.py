"""
Lista4_q5: Escreva uma função que recebe uma lista com n números inteiros, e retorna uma
lista com a soma cumulativa dos elementos da lista original onde o i-ésimo
elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] =
[1,3,6]
"""

def soma_cumulativa(lista: list):
    if type(lista) != list:
        return Exception
    
    if any(type(v) != int for v in lista):
        return Exception

    lista_cumulativa = [lista[0]] if lista else []

    for i in range(1, len(lista)):
        lista_cumulativa.append(sum(lista[:i + 1]))

    return lista_cumulativa


assert soma_cumulativa(None) == Exception
assert soma_cumulativa('1, 2, 3') == Exception
assert soma_cumulativa((1, 2, 3, 4, 5)) == Exception
assert soma_cumulativa({ "1", "2" }) == Exception
assert soma_cumulativa(['1', '2', '3']) == Exception
assert soma_cumulativa([None, 2, 3]) == Exception, f"Valor retornado: {soma_cumulativa([None, 2, 3])}"
assert soma_cumulativa(['1', 2, 3]) == Exception
assert soma_cumulativa([1, [2], 3]) == Exception
assert soma_cumulativa([1, 2, str]) == Exception
assert soma_cumulativa([1, 2, 3.0]) == Exception
assert soma_cumulativa([1.3, 2, 3]) == Exception
assert soma_cumulativa([]) == []
assert soma_cumulativa([1]) == [1], f"Valor retornado: {soma_cumulativa([1])}"
assert soma_cumulativa([1, 2]) == [1, 3]
assert soma_cumulativa([1, 2, 3]) == [1, 3, 6]
assert soma_cumulativa([1, 2, 3, 5]) == [1, 3, 6, 11]
assert soma_cumulativa([1, 2, 3, 5, 10]) == [1, 3, 6, 11, 21]

print("Todos os testes passaram.")
