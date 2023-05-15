"""
Lista3_q22: Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.

S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!
"""

def fatorial(n: int):
    fatorial = 1
    counter = 2
    while counter <= n:
        fatorial *= counter
        counter += 1

    return fatorial

def calcular_formula(n):
    if type(n) != int or n <= 0:
        return Exception

    somatorio = 1
    for i in range(1, n + 1):
        somatorio += 1 / fatorial(n)
    
    return round(somatorio, 9)


assert calcular_formula(None) == Exception
assert calcular_formula([]) == Exception
assert calcular_formula({}) == Exception
assert calcular_formula('3') == Exception
assert calcular_formula(-1) == Exception
assert calcular_formula(0) == Exception
assert calcular_formula(1) == 2.0
assert calcular_formula(5) == 1.041666667
assert calcular_formula(7) == 1.001388889
assert calcular_formula(9) == 1.000024802
assert calcular_formula(10) == 1.000002756

print("Todos os testes passaram.")