"""
Lista3_q11: FFaça uma função que recebe, por parâmetro, a altura e o sexo de uma
pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a
fórmula peso ideal = 72.7 * altura - 58 e, para mulheres, peso ideal = 62.1 * altura
- 44.7.
"""

def peso_ideal(altura, sexo):
    if type(altura) != float or sexo not in ['M', 'F']:
        return Exception
    
    if altura <= 1 or altura >= 2.2:
        return Exception
    
    peso = 0
    if sexo == 'M':
        peso = 72.7 * altura - 58
    elif sexo == 'F':
        peso = 62.1 * altura - 44.7
    
    return round(peso, 1)


assert peso_ideal('1.73', 'F') == Exception
assert peso_ideal(None, 'M') == Exception
assert peso_ideal(1.74, 'X') == Exception
assert peso_ideal(1.52, 'm') == Exception
assert peso_ideal(1.69, 'f') == Exception
assert peso_ideal(-1.23, 'M') == Exception
assert peso_ideal(0, 'M') == Exception
assert peso_ideal(1, 'M') == Exception
assert peso_ideal(2.2, 'F') == Exception
assert peso_ideal(1.78, 'M') == 71.4
assert peso_ideal(1.65, 'M') == 62.0
assert peso_ideal(2.1, 'M') == 94.7
assert peso_ideal(1.53, 'F') == 50.3
assert peso_ideal(1.53, 'F') == 50.3
assert peso_ideal(1.1, 'F') == 23.6

print("Todos os testes passaram.")