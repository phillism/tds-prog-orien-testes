"""
Lista3_q9: Faça uma função que recebe um valor inteiro e verifica se o valor é par ou
ímpar. A função deve retornar um valor booleano.
"""

def classificar_numero(n):
    if type(n) != int:
        return Exception
    
    return 'Par' if n % 2 == 0 else 'Ímpar'

assert classificar_numero('1') == Exception
assert classificar_numero(None) == Exception
assert classificar_numero([]) == Exception
assert classificar_numero(12.5) == Exception
assert classificar_numero(2.52) == Exception
assert classificar_numero(0) == 'Par'
assert classificar_numero(10) == 'Par'
assert classificar_numero(12) == 'Par'
assert classificar_numero(26) == 'Par'
assert classificar_numero(33) == 'Ímpar'
assert classificar_numero(493) == 'Ímpar'
assert classificar_numero(1999) == 'Ímpar'
assert classificar_numero(-13) == 'Ímpar'
assert classificar_numero(-33) == 'Ímpar'
assert classificar_numero(-1111) == 'Ímpar'

print("Todos os testes passaram.")