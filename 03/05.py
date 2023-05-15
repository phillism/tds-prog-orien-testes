"""
Lista3_q5: Faça uma função que recebe a idade de uma pessoa em anos, meses e dias
e retorna essa idade expressa em dias.
"""

def calcular_dias(anos, meses, dias):
    if any(type(p) != int or p < 0 for p in [anos, meses, dias]):
        return Exception

    if meses > 12 or dias > 30:
        return Exception    

    return (anos * 365) + (meses * 30) + dias


assert calcular_dias(None, 11, 3) == Exception
assert calcular_dias(15, [], 3) == Exception
assert calcular_dias(15, 11, '3') == Exception
assert calcular_dias(17, 11, 0.5) == Exception
assert calcular_dias(17, 3.2, 0) == Exception
assert calcular_dias(17.8, 11, 0) == Exception
assert calcular_dias(17, 11, -1) == Exception
assert calcular_dias(17, -11, 1) == Exception
assert calcular_dias(-6, 4, 1) == Exception
assert calcular_dias(18, 13, 3) == Exception
assert calcular_dias(18, 11, 31) == Exception
assert calcular_dias(0, 2, 0) == 60
assert calcular_dias(0, 2, 2) == 62
assert calcular_dias(0, 0, 30) == 30
assert calcular_dias(1, 0, 0) == 365
assert calcular_dias(12, 11, 30) == 4740
assert calcular_dias(38, 0, 2) == 13872
assert calcular_dias(57, 12, 9) == 21174

print("Todos os testes passaram.")