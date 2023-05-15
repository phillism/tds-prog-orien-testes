"""
Lista3_q21: Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.

S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.
"""

def calcular_formula(n):
    if type(n) != int or n <= 0:
        return Exception

    somatorio = 0
    for i in range(1, n + 1):
        somatorio += 1 / (i)
    
    return round(somatorio, 2)


assert calcular_formula(None) == Exception
assert calcular_formula([]) == Exception
assert calcular_formula({}) == Exception
assert calcular_formula('3') == Exception
assert calcular_formula(-1) == Exception
assert calcular_formula(0) == Exception
assert calcular_formula(1) == 1
assert calcular_formula(9) == 2.83
assert calcular_formula(15) == 3.32
assert calcular_formula(29) == 3.96
assert calcular_formula(51) == 4.52
assert calcular_formula(92) == 5.1
assert calcular_formula(182) == 5.78

print("Todos os testes passaram.")