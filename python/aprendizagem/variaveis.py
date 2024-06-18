# > Variáveis e Operadores

# 1. Variáveis

idade = 23 # Criando uma variável

print(idade)

nome = 'Matheus Malentaqui'

print(nome)

"""
  Tipos de variáveis

  1. int: números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000 
  2. float: números reais, ou seja, números com parte decimal: 1.0, -2.7, 3.14
  3. str: cadeias de caracteres, ou seja, dados textuais (string)
  4. bool: valores lógicos (booleanos): True or False
"""

idade = 23
altura = 1.80
nome = 'Matheus Malentaqui'
estudando = True

print(  type(idade) )
print(  type(altura) )
print(  type(nome) )
print(  type(estudando) )

# Obtendo dados do usuário e salvando em variáveis

linguagem = input('Qual é a linguagem de programação que você está estudando? ')

print('A linguagem que você está estudando é:', linguagem)

# Imprimindo variáveis + Mais sobre a função print

print('Suas informações de cadastro ao curso:', nome, idade, altura)