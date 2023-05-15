"""
Lista3_q7: Faça uma função que recebe a idade de um nadador por parâmetro e retorna
a categoria desse nadador de acordo com a tabela abaixo:

-----------------------+-------------
| Faixa Etária         | Categoria  |
-------------------------------------
| 5 a 7 anos           | Infantil A |
-------------------------------------
| 8 a 10 anos          | Infantil B |
-------------------------------------
| 11 a 13 anos         | Juvenil A  |
-------------------------------------
| 14 a 17 anos         | Juvenil B  |
-------------------------------------
| Maiores de 18 anos   | Adulto     |
-------------------------------------
"""

def categoria(idade):
    if type(idade) != int:
        return Exception
    
    if idade < 5 or idade > 80:
        return Exception
    
    if idade >= 5 and idade <= 7:
        return 'Infantil A'
    
    if idade >= 8 and idade <= 10:
        return 'Infantil B'
    
    if idade >= 11 and idade <= 13:
        return 'Juvenil A'
    
    if idade >= 14 and idade <= 17:
        return 'Juvenil B'
    
    return 'Adulto'


assert categoria('1') == Exception
assert categoria([]) == Exception
assert categoria(-1) == Exception
assert categoria(-2) == Exception
assert categoria(-7.3) == Exception
assert categoria(0) == Exception
assert categoria(1) == Exception
assert categoria(4) == Exception
assert categoria(81) == Exception
assert categoria(5) == 'Infantil A'
assert categoria(6) == 'Infantil A'
assert categoria(7) == 'Infantil A'
assert categoria(8) == 'Infantil B'
assert categoria(9) == 'Infantil B'
assert categoria(10) == 'Infantil B'
assert categoria(11) == 'Juvenil A'
assert categoria(12) == 'Juvenil A'
assert categoria(13) == 'Juvenil A'
assert categoria(14) == 'Juvenil B'
assert categoria(16) == 'Juvenil B'
assert categoria(17) == 'Juvenil B'
assert categoria(18) == 'Adulto'
assert categoria(21) == 'Adulto'
assert categoria(36) == 'Adulto'
assert categoria(76) == 'Adulto'
assert categoria(80) == 'Adulto'

print("Todos os testes passaram.")