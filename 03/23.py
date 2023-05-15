"""
Lista3_q23: Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(n2+1)/(n+3)
"""

def calcular_formula(n):
    if type(n) != int or n <= 0:
        return Exception

    somatorio = 0
    for i in range(1, n + 1):
        somatorio += (n * 2 + 1) / (n + 3)
    
    return somatorio



assert calcular_formula(None) == Exception
assert calcular_formula([]) == Exception
assert calcular_formula({}) == Exception
assert calcular_formula('3') == Exception
assert calcular_formula(-1) == Exception
assert calcular_formula(0) == Exception
assert calcular_formula(1) == 0.75
assert calcular_formula(3) == 3.5
assert calcular_formula(7) == 10.5
assert calcular_formula(9) == 14.250000000000002
assert calcular_formula(13) == 21.9375

print("Todos os testes passaram.")