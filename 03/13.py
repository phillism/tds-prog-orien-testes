"""
Lista3_q13: Faça uma função que recebe, por parâmetro, a hora de inicio e a hora de
término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos.
O procedimento deve retornar, também por parâmetro, a duração do jogo em
horas e minutos, considerando que o tempo máximo de duração de um jogo é
de 24 horas e que o jogo pode começar em um dia e terminar no outro.
"""

def duracao_jogo(inicio_h, inicio_m, termino_h, termino_m):
    if any(type(n) != int or n < 0 for n in [inicio_h, inicio_m, termino_h, termino_m]):
        return Exception
    
    if (inicio_h >= 24 or termino_h >= 24) or (inicio_m >= 60 or termino_m >= 60):
        return Exception
    
    if inicio_h == termino_h and inicio_m == inicio_h:
        return Exception
    
    inicio_minutos = (inicio_h * 60) + inicio_m
    termino_minutos = (termino_h * 60) + termino_m

    if inicio_minutos < termino_minutos:
        total = termino_minutos - inicio_minutos
    else:
        total = (1440 - inicio_minutos) + termino_minutos

    return  { 'minutos': (total % 60), 'horas': total // 60 }


assert duracao_jogo('22', 0, 2, 0) == Exception
assert duracao_jogo(23, [0], 2, 0) == Exception
assert duracao_jogo(23, 0, None, 0) == Exception
assert duracao_jogo(23, 0, 6, 3.4) == Exception
assert duracao_jogo(23, 0, -1, 0) == Exception
assert duracao_jogo(-23, 0, 6, 0) == Exception
assert duracao_jogo(24, 0, 2, 0) == Exception, 'O tempo máximo em horas é 24.'
assert duracao_jogo(0, 0, 24, 0) == Exception, 'O tempo máximo em horas é 24.'
assert duracao_jogo(12, 60, 18, 30) == Exception, 'O tempo máximo em minutos é 59.'
assert duracao_jogo(0, 0, 13, 60) == Exception, 'O tempo máximo em minutos é 59.'
assert duracao_jogo(0, 0, 19, 30) == { 'minutos': 30, 'horas': 19 }
assert duracao_jogo(12, 30, 19, 30) == { 'minutos': 0, 'horas': 7 }
assert duracao_jogo(23, 30, 1, 40) == { 'minutos': 10, 'horas': 2 }
assert duracao_jogo(16, 0, 18, 0) == { 'minutos': 0, 'horas': 2 }
assert duracao_jogo(10, 35, 18, 0) == { 'minutos': 25, 'horas': 7 }
assert duracao_jogo(22, 0, 6, 0) == { 'minutos': 0, 'horas': 8 }
assert duracao_jogo(23, 30, 6, 0) == { 'minutos': 30, 'horas': 6 }
assert duracao_jogo(23, 30, 6, 45) == { 'minutos': 15, 'horas': 7 }

print("Todos os testes passaram.")