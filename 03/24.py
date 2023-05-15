"""
Lista3_q24: Escreva uma função que recebe, por parâmetro, dois valores X e Z e calcula
e retorna Xz. (sem utilizar funções ou operadores de potência prontos)
"""

def calcular_potencia(x, z):
    if any(type(n) not in [int, float] or n < 0 for n in [x, z]):
        return Exception
    
    if type(z) == float:
        return Exception

    acumulador = 1
    for y in range(z):
        acumulador *= x
    
    return acumulador


assert calcular_potencia(None, 3) == Exception
assert calcular_potencia(3, None) == Exception
assert calcular_potencia(3, '3') == Exception
assert calcular_potencia('3', 1) == Exception
assert calcular_potencia(3, -1) == Exception
assert calcular_potencia(-1, 3) == Exception
assert calcular_potencia(1, 3.1) == Exception
assert calcular_potencia(1, 3.0) == Exception
assert calcular_potencia(0.0, 1) == 0
assert calcular_potencia(0, 1) == 0
assert calcular_potencia(1, 0) == 1
assert calcular_potencia(0, 20) == 0
assert calcular_potencia(1.0, 1) == 1
assert calcular_potencia(1, 19) == 1
assert calcular_potencia(1, 239) == 1
assert calcular_potencia(3, 2) == 9
assert calcular_potencia(3.0, 3) == 27
assert calcular_potencia(7, 2) == 49
assert calcular_potencia(20, 4) == 160000
assert calcular_potencia(20.5, 4) == 176610.0625

print("Todos os testes passaram.")