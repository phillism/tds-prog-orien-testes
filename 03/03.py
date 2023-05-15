"""
Lista3_q3: Faça uma função que recebe por parâmetro um valor inteiro e positivo e
retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso
contrário.
"""

def primo(n):
    if type(n) != int:
        return Exception
    
    if n < 0:
        return Exception
    
    for i in range(2, n) or [1]:
        if n % i == 0:
            return False
    
    return True

assert primo([]) == Exception
assert primo('.') == Exception
assert primo(None) == Exception
assert primo(3.2) == Exception
assert primo(-2.2) == Exception
assert primo(-1) == Exception
assert primo(-6) == Exception
assert primo(0) == False
assert primo(1) == False
assert primo(2) == False
assert primo(7) == True
assert primo(21) == False
assert primo(19) == True
assert primo(1005) == False
assert primo(31) == True
assert primo(3333) == False
assert primo(251) == True
assert primo(1999) == True
assert primo(3427) == False

print("Todos os testes passaram.")