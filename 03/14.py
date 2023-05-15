"""
Lista3_q14: Escreva uma função que recebes 3 valores reais X, Y e Z e que verifique se
esses valores podem ser os comprimentos dos lados de um triângulo e, neste
caso, retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um
triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento
de cada lado de um triângulo é menor do que a soma do comprimento dos outros
dois lados. O procedimento deve identificar o tipo de triângulo formado
observando as seguintes definições:

o Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
o Triângulo Isósceles: os comprimentos de 2 lados são iguais.
o Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.
"""

def identficar_triangulo(x, y, z):
    lados = [x, y, z]
    
    if any(type(n) != int or n <= 0 for n in lados):
        return Exception

    if any(sum(lados) - n <= n for n in lados):
        return Exception

    if all(x == n for n in lados):
        return 'Equilátero'
    
    if (x == y) or (y == z) or (z == x):
        return 'Isósceles'
    
    return 'Escaleno'


assert identficar_triangulo('5', 5, 5) == Exception
assert identficar_triangulo(5, [5], 5) == Exception
assert identficar_triangulo(5, 5, {5}) == Exception
assert identficar_triangulo(5.0, 5, 5) == Exception
assert identficar_triangulo(5, 5.3, 5) == Exception
assert identficar_triangulo(5, 5, 5.5) == Exception
assert identficar_triangulo(-5, 5, 5) == Exception
assert identficar_triangulo(2, -1, 2) == Exception
assert identficar_triangulo(2, 0, 2) == Exception
assert identficar_triangulo(5, 5, 10) == Exception
assert identficar_triangulo(5, 10, 5) == Exception
assert identficar_triangulo(10, 5, 5) == Exception
assert identficar_triangulo(12, 12, 25) == Exception
assert identficar_triangulo(6, 8, 14) == Exception
assert identficar_triangulo(5, 5, 5) == 'Equilátero'
assert identficar_triangulo(13, 13, 13) == 'Equilátero'
assert identficar_triangulo(1, 1, 1) == 'Equilátero'
assert identficar_triangulo(5, 5, 8) == 'Isósceles'
assert identficar_triangulo(8, 5, 8) == 'Isósceles'
assert identficar_triangulo(8, 9, 9) == 'Isósceles'
assert identficar_triangulo(6, 8, 13) == 'Escaleno'
assert identficar_triangulo(9, 6, 8) == 'Escaleno'
assert identficar_triangulo(3, 4, 6) == 'Escaleno'

print("Todos os testes passaram.")