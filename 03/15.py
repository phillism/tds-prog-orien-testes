"""
Lista3_q15: A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes,
coletando dados sobre o salário e número de filhos. Faça uma função que leia
esses dados para um número não determinado de pessoas e retorne a média de
salário da população, a média do número de filhos, o maior salário e o percentual
de pessoas com salário até R$ 350,00.
"""

def ler_dados(pessoas: list):
    if type(pessoas) != list:
        return Exception
    
    if len(pessoas) == 0 or any(type(p) != tuple or len(p) != 2 for p in pessoas):
        return Exception

    quant_pessoas = len(pessoas)
    total_filhos = 0
    total_salario = 0
    maior_salario = 0
    salarios_acima = 0    

    for p in pessoas:
        salario = p[0]    
        filhos = p[1]


        # Tratando erros com os valores das tuplas.
        if any(type(p_data) not in [int, float] for p_data in p):
            return Exception

        if salario <= 0 or filhos < 0 or type(filhos) == float:
            return Exception


        total_salario += salario
        total_filhos += filhos

        if total_salario > maior_salario:
            maior_salario = salario

        if salario >= 350:
            salarios_acima += 1
    
    return { 
        'media_salario': round(total_salario / quant_pessoas, 2), 
        'media_filhos': int(total_filhos / quant_pessoas),
        'maior_salario': round(maior_salario, 2),
        'percentual': round((salarios_acima / quant_pessoas) * 100, 2)
    }


assert ler_dados(None) == Exception
assert ler_dados(1) == Exception
assert ler_dados('19999;2') == Exception
assert ler_dados([None]) == Exception
assert ler_dados([]) == Exception
assert ler_dados([1]) == Exception
assert ler_dados([()]) == Exception
assert ler_dados([(None, 2), (1000, 3)]) == Exception
assert ler_dados([None, (2000, 2)]) == Exception
assert ler_dados((1000, 3)) == Exception
assert ler_dados([(1000, -1)]) == Exception
assert ler_dados([(0, 3)]) == Exception
assert ler_dados([(1000, 3.0)]) == Exception

assert ler_dados([(1000, 3)]) == { 
    'media_salario': 1000.0, 'media_filhos': 3, 'maior_salario': 1000.0,'percentual': 100.0 
}

assert ler_dados([(1000, 3), (2000, 2)]) == { 
    'media_salario': 1500.0, 'media_filhos': 2, 'maior_salario': 2000, 'percentual': 100 
}

assert ler_dados([(1000, 3), (2000, 1), (954, 6), (323, 3), (340, 0), (2500, 4)]) == {
    'media_salario': 1186.17, 'media_filhos': 2, 'maior_salario': 2500, 'percentual': 66.67
}

assert ler_dados([(1000, 3), (2000, 1), (954, 6), (323, 3), (1900, 0), (1997.90, 4)]) == {
    'media_salario': 1362.48, 'media_filhos': 2, 'maior_salario': 1997.9, 'percentual': 83.33
}

print("Todos os testes passaram.")