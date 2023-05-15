"""
Lista3_q20: Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o somatório desse valor.
"""

def somatorio(n):
    if type(n) != int or n <= 0:
        return Exception

    somatorio = 0
    for i in range(1, n + 1):
        somatorio += i
    
    return somatorio


assert somatorio(None) == Exception
assert somatorio([]) == Exception
assert somatorio({}) == Exception
assert somatorio('3') == Exception
assert somatorio(-1) == Exception
assert somatorio(0) == Exception
assert somatorio(6) == 21
assert somatorio(10) == 55
assert somatorio(15) == 120
assert somatorio(30) == 465
assert somatorio(105) == 5565
assert somatorio(293) == 43071
assert somatorio(3992) == 7970028

print("Todos os testes passaram.")