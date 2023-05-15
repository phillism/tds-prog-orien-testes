"""
Lista3_10: Faça uma função que recebe a média final de um aluno por parâmetro e
retorna o seu conceito, conforme a tabela abaixo:

  Nota      |  Conceito
  de 0,0 a  |  4,9 D
  de 5,0 a  |  6,9 C
  de 7,0 a  |  8,9 B
  de 9,0 a  |  10,0A
"""

def obter_conceito(media_final):
    if type(media_final) not in [int, float]:
        return Exception
    
    if not (0 <= media_final <= 10):
        return Exception
    
    if media_final < 5:
        return 'D'
    
    if media_final < 7:
        return 'C'
    
    if media_final < 9:
        return 'B'

    return 'A'

assert obter_conceito('1') == Exception
assert obter_conceito([]) == Exception
assert obter_conceito(None) == Exception
assert obter_conceito(-0.3) == Exception
assert obter_conceito(-1) == Exception
assert obter_conceito(-6.3) == Exception
assert obter_conceito(11) == Exception
assert obter_conceito(10.1) == Exception
assert obter_conceito(0) == 'D'
assert obter_conceito(2.5) == 'D'
assert obter_conceito(4.9) == 'D'
assert obter_conceito(5) == 'C'
assert obter_conceito(5.3) == 'C'
assert obter_conceito(6.9) == 'C'
assert obter_conceito(7) == 'B'
assert obter_conceito(7.1) == 'B'
assert obter_conceito(8.99) == 'B'
assert obter_conceito(9) == 'A'
assert obter_conceito(9.5) == 'A'
assert obter_conceito(10) == 'A'

print("Todos os testes passaram.")