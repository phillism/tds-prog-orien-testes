"""
Lista3_q19: Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o número de divisores desse valor.
"""

def quant_divisores(n):
    if type(n) != int or n <= 0:
        return Exception

    quant = 0
    for i in range(1, n + 1):
        if n % i == 0:
            quant += 1
    
    return quant


assert quant_divisores(None) == Exception
assert quant_divisores([]) == Exception
assert quant_divisores({}) == Exception
assert quant_divisores('3') == Exception
assert quant_divisores(-1) == Exception
assert quant_divisores(0) == Exception
assert quant_divisores(6) == 4
assert quant_divisores(10) == 4
assert quant_divisores(20) == 6
assert quant_divisores(50) == 6
assert quant_divisores(105) == 8
assert quant_divisores(190) == 8
assert quant_divisores(288) == 18
assert quant_divisores(1928) == 8

print("Todos os testes passaram.")