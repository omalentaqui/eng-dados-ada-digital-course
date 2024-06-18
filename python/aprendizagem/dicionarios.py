# > Dicionários

# Criando Dicionários

dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Matheus', 'idade': 23, 'altura': 1.80 }

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionário
""" Ao tentar adicionar uma chave onde o não for encontrada no dicionário e atribuir um valor a ela,
automaticamente será adicionado ao dicionário o novo elemento. """
dicionario[ 'programador' ] = True

print(dicionario)


""" Para subscrever um elemento já adicionado a lista anteriormente, basta seguir conforme abaixo: """
dicionario[ 'altura' ] = 1.79

print(dicionario)

# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)