"""
Lista3_q18: Faça uma função que recebe, por parâmetro, um valor N e calcula e escreve
a tabuada de 1 até N. Mostre a tabuada na forma:
1 x N = N
2 x N = 2N
...
N x N = N2
"""

def tabuada(n):
    if type(n) != int or n <= 0:
        return Exception
    
    t = []
    for i in range(1, n + 1):
        t.append(i * n)

    return t


assert tabuada(None) == Exception
assert tabuada([]) == Exception
assert tabuada({}) == Exception
assert tabuada('3') == Exception
assert tabuada(-1) == Exception
assert tabuada(0) == Exception
assert tabuada(1.0) == Exception
assert tabuada(1.5) == Exception
assert tabuada(1) == [1]
assert tabuada(2) == [2, 4]
assert tabuada(5) == [5, 10, 15, 20, 25]
assert tabuada(10) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
assert tabuada(25) == [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625]

print("Todos os testes passaram.")