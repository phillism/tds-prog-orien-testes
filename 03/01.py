"""
Lista3_q1: Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o
seu volume (v = 4/3 * PI * R ** 3).
"""

def volume(raio):
    if type(raio) not in [int, float] or raio <= 0:
        return Exception
    
    return round(4 / 3 * 3.14 * raio ** 3, 2)

assert volume('.') == Exception
assert volume([]) == Exception
assert volume(None) == Exception
assert volume(0) == Exception
assert volume(-1) == Exception
assert volume(1.0) == 4.19
assert volume(1) == 4.19
assert volume(5.85) == 838.18

print("Todos os testes passaram.")