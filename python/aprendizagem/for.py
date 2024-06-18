# > Laços de Repetição (For)

"""for variavel in range(10):
    print(variavel)"""

"""for variavel in range(2, 10):
    print(variavel)"""

# 1, 4, 7, 10, (13)...
"""for variavel in range(1, 12, 3):
    print(variavel)"""

"""nota1 = float( input('Informe sua nota 1: ') )
nota2 = float( input('Informe sua nota 2: ') )
nota3 = float( input('Informe sua nota 3: ') )"""

# Estrutura automatizada para obtenção das 3 notas do estudante

soma = 0

for i in range(1, 4):
    nota = float( input(f'Informe sua nota {i}: ') )

    soma = soma + nota

print(soma / 3)
