"""
Lista3_q4: Faça uma função que recebe por parâmetro o tempo de duração de um
processo em uma fábrica expressa em segundos e retorna também por
parâmetro esse tempo em horas, minutos e segundos.
"""

def formatar_tempo(segundos):
    if type(segundos) != int or segundos < 0:
        return Exception
    
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60

    return segundos, minutos, horas


assert formatar_tempo('.') == Exception
assert formatar_tempo([]) == Exception
assert formatar_tempo(None) == Exception
assert formatar_tempo(3.6) == Exception
assert formatar_tempo(-12) == Exception
assert formatar_tempo(0) == (0, 0, 0)
assert formatar_tempo(5) == (5, 0, 0)
assert formatar_tempo(32) == (32, 0, 0)
assert formatar_tempo(60) == (0, 1, 0)
assert formatar_tempo(61) == (1, 1, 0)
assert formatar_tempo(140) == (20, 2, 0)
assert formatar_tempo(653) == (53, 10, 0)
assert formatar_tempo(9123) == (3, 32, 2)
assert formatar_tempo(19212) == (12, 20, 5)

print("Todos os testes passaram.")