# > Listas

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9, 9.7, 8.2]

# Criando Listas
lista = []
lista = list()
lista = [26, 'Matheus', 3.14159, True]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (Fatiamento)
lista = [26, 'Matheus', 3.14159, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
# print(lista[4]) - Esta fora do range da lista

print(lista[-1])

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])

# Interação com o FOR

# 1. Utilizando os própios elementos de uma lista
for elemento in lista:
    print(elemento)

# 2. Utilizando os índices
print( 'Comprimento da lista:', len(lista) )

for i in range(len(lista)):
    print(lista[i]) # Acessa a cada índece a cada iteração



# > Metódos de Listas

lista = [1, 3, 12, 8, 2]

# Append - Adiciona ao final de uma lista

print('Antes do append:', lista)

lista.append(3)

print('Depois do append:', lista)

# Insert - Adiciona na posição escolhida na lista

lista.insert(2, 10)

print('Depois do insert:', lista)

# Extend - Adiciona elementos de uma nova lista e joga ao final da outra

lista2 = [1, 2, 3]

lista.extend(lista2)

print('Depois do extend:', lista)

# Pop - Remove o elemento especificado ou se não especificado remove o último elemento

lista.pop()

print('Lista após o pop:', lista)

lista.pop(0)

print('Lista após o pop:', lista)

# Remove - Remove o valor mencionado dentro de uma lista (removendo o primeiro valor encontrado)

lista.remove(3)

print('Depois do remove:', lista)

# Count - Contar quantos o mesmo valor aparecem na lista

print( 'Quantidade de 2 na lista:', lista.count(2) )

# Index - Diz o índice de um determinado elemento

print( 'Índice do elemento 12:', lista.index(12) )

# Sort - Realiza a ordenação da lista de forma crescente

lista.sort()

print('Depois do sort:', lista)

lista.sort(reverse=True)

print('Lista decrescente:', lista)

# > Funções para Lista

# Len

print( 'A quantidade de elementos da lista é:', len(lista) )

# Sum

print( 'A soma total dos elementos da lista é:', sum(lista) )

# Max

print( 'Maior elemento da lista é:', max(lista) )

# Min

print( 'Menor elemento da lista é:', min(lista) )
