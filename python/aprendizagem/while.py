# > Laços de Repetição (While)

numero_sorteado = 15

numero_escolhido = int( input('Informe um número entre 1 e 20: ') )

# Esta utilização com o 'IF' não permite que o usuário continue interagindo, sem ter uma nova chance
""" 
    if numero_sorteado == numero_escolhido:
        print('Você acertou!')
    else:
        print('Você errou!')
"""

# Desta forma com o 'While' já permite que o usuário continue tentando até acertar

while numero_escolhido != numero_sorteado:
    print('Você errou o número, tente novamente...')

    numero_escolhido = int( input('Informe um número entre 1 e 20: ') )

print('Parabéns! Você acertou!')

# Exemplo 02: Estrutura com Contador

contador = 0

while contador < 5:
    print(contador)

    contador = contador + 1
