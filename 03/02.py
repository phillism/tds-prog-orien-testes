"""
Lista3_q2. Escreva uma função que recebe as 3 notas de um aluno por parâmetro
e uma letra. Se a letra for A o procedimento calcula a média aritmética das
notas do aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2).
A função deve retornar a média calculada.
"""

def calcular_media(n1, n2, n3, letra):
    medias = [n1, n2, n3]

    if letra not in ['A', 'P']:
        return Exception

    if not all(type(n) in [int, float] for n in medias):
        return Exception
    
    if any(n < 0 or n > 10 for n in medias):
        return Exception

    media = 0
    if letra == 'A':
        media = (n1 + n2 + n3) / 3
    else:
        media = (n1 * 5 + n2 * 3 + n3 * 2) / 10
    
    return round(media, 1)


assert calcular_media(4.0, 4.0, 5.0, "X") == Exception
assert calcular_media(".", 4.0, 5.0, "A") == Exception
assert calcular_media(6.0, 4.0, 5.0, "a") == Exception
assert calcular_media(7.0, 2.0, 4.0, "p") == Exception
assert calcular_media(7.0, 2.0, 4.0, []) == Exception
assert calcular_media(7.0, 2.0, 4.0, None) == Exception
assert calcular_media(7.0, [], 4.0, "P") == Exception
assert calcular_media(True, 7.0, 4.0, "A") == Exception
assert calcular_media(6.5, 7.0, "6.0", "P") == Exception
assert calcular_media(-2, 7.0, 10.0, "A") == Exception
assert calcular_media(2, 11.0, 9.0, "P") == Exception
assert calcular_media(2, 10.0, 13.2, "A") == Exception
assert calcular_media(6.0, 6.0, 9.0, "A") == 7.0
assert calcular_media(4, 8, 9.0, "A") == 7.0
assert calcular_media(4.5, 8, 9.0, "A") == 7.2
assert calcular_media(6, 8, 10, "P") == 7.4
assert calcular_media(7.0, 8.5, 10, "P") == 8.1

print("Todos os testes passaram.")