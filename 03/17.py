"""
Lista3_q17: Faça uma função que lê 50 valores inteiros e retorna o maior e o menor deles.
"""

def maior_menor(*numeros):
    if type(numeros) not in [tuple, list] or len(numeros) != 50:
        return Exception
    
    if any(type(n) not in [int, float] for n in numeros):
        return Exception
    
    menor = None
    maior = None
    for n in numeros:
        if menor is None or n < menor:
            menor = n
        
        if maior is None or n > maior:
            maior = n
    
    return (menor, maior)



assert maior_menor() == Exception
assert maior_menor(None) == Exception
assert maior_menor([]) == Exception
assert maior_menor([None]) == Exception
assert maior_menor(0, {}) == Exception
assert maior_menor(1, 2, '3') == Exception
assert maior_menor(1, 2, 3) == Exception
assert maior_menor(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49) == Exception
assert maior_menor(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51) == Exception
assert maior_menor(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50) == (1, 50)
assert maior_menor(1, 2, 3, 4, 5, 62, 73, 48, -23, 19, 310, 151, 182, 213, 914, 715, 616, 147.3, 18, 19, 20, 21, 32.22, 12.23, 2.4, 0.33, 291.2, 1999.2, 392, 1992, 3921, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 49, 50) == (-23, 3921)
assert maior_menor(1, 2, 3, 5, 62, 73, 48, -23, 19, 31029.9123, 151, 182, 213, 914, 715, 616, 147.3, 18, 19, 20, 21, 32.22, 12.23, 2.4, 0.33, 291.2, 1999.2, 392, 1992, 3921, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50) == (-23, 31029.9123)

print("Todos os testes passaram.")