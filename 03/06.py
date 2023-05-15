"""
Lista3_q6: Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito
perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio.
(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar
um valor booleano.
"""

def perfeito(n):
    if type(n) != int or n < 0:
        return Exception

    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i

    return n != 0 and soma == n


assert perfeito('1') == Exception
assert perfeito([]) == Exception
assert perfeito(-1) == Exception
assert perfeito(-2) == Exception
assert perfeito(-7.3) == Exception
assert perfeito(3.25) == Exception
assert perfeito(0) == False
assert perfeito(1) == False
assert perfeito(3) == False
assert perfeito(6) == True
assert perfeito(7) == False
assert perfeito(10) == False
assert perfeito(15) == False
assert perfeito(28) == True
assert perfeito(496) == True
assert perfeito(8128) == True

print("Todos os testes passaram.")