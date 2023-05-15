"""
Lista3_q8: Faça uma função que recebe um valor inteiro e verifica se o valor é positivo
ou negativo. A função deve retornar um valor booleano.
"""

def classificar_numero(n):
    if type(n) not in [int, float]:
        return Exception
    
    return 'Positivo' if n >= 0 else 'Negativo'


assert classificar_numero('1') == Exception
assert classificar_numero(None) == Exception
assert classificar_numero([]) == Exception
assert classificar_numero(0) == 'Positivo'
assert classificar_numero(2.2) == 'Positivo'
assert classificar_numero(12) == 'Positivo'
assert classificar_numero(33.3) == 'Positivo'
assert classificar_numero(493) == 'Positivo'
assert classificar_numero(1932.7) == 'Positivo'
assert classificar_numero(-1) == 'Negativo'
assert classificar_numero(-10.23) == 'Negativo'
assert classificar_numero(-29) == 'Negativo'
assert classificar_numero(-82.5) == 'Negativo'
assert classificar_numero(-193) == 'Negativo'
assert classificar_numero(-1024.9333) == 'Negativo'

print("Todos os testes passaram.")