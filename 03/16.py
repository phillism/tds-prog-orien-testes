"""
Lista3_q16: Faça uma função que leia um número não determinado de valores positivos
e retorna a média aritmética dos mesmos.
"""

def calcular_media(*numeros):
    if type(numeros) not in [tuple, list] or len(numeros) == 0:
        return Exception
    
    if any(type(n) not in [float, int] for n in numeros):
        return Exception

    total = 0
    for n in numeros:
        total += n
        
    return round(total / len(numeros), 2)


assert calcular_media() == Exception
assert calcular_media(None) == Exception
assert calcular_media([]) == Exception
assert calcular_media([None]) == Exception
assert calcular_media(0, {}) == Exception
assert calcular_media(1, 2, '3') == Exception
assert calcular_media(6, 6, 6) == 6.0
assert calcular_media(2, 2, 2) == 2.0
assert calcular_media(10, 10, 8) == 9.33
assert calcular_media(10, 2, 3) == 5.0
assert calcular_media(100, 250, 175, 50, 25) == 120.0
assert calcular_media(1, 2, 3, 4, 5, 6, 7, 8, 10) == 5.11
assert calcular_media(19.3, 293.9, 992.15, 676) == 495.34

print("Todos os testes passaram.")