"""
Lista3_q25: Escreva uma função que recebe, por parâmetro um valor inteiro e retorna o
seu fatorial.
"""

def fatorial(n: int):
    if type(n) != int or n <= 0:
        return Exception

    fatorial = 1
    counter = 2
    while counter <= n:
        fatorial *= counter
        counter += 1

    return fatorial


assert fatorial([]) == Exception
assert fatorial(None) == Exception
assert fatorial('3') == Exception
assert fatorial(0) == Exception
assert fatorial(-1) == Exception
assert fatorial(3.1) == Exception
assert fatorial(3.0) == Exception
assert fatorial(5) == 120
assert fatorial(8) == 40320
assert fatorial(12) == 479001600
assert fatorial(16) == 20922789888000
assert fatorial(20) == 2432902008176640000
assert fatorial(23) == 25852016738884976640000
assert fatorial(25) == 15511210043330985984000000

print("Todos os testes passaram.")