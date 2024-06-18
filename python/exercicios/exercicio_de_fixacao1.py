# > Exercícios de Fixação 1

"""
  Questão 1
  Muitas vezes é requerido o armazenamento de algum valor ou o resultado de alguma operação, 
  para que os dados possam ser utilizados em outras partes do programa. Para que isso seja possível, 
  o Python permite a criação de variáveis. Sabendo disso, considere o trecho de código a seguir:

  var1 = 12
  var2 = 30
  var3 = var1 XXX var2

  print(var3)

  var3 = var3 YYY 2

  print(var3)

  A instrução print(var3) exibe na tela o valor armazenado na variável var3, 
  em cada uma das duas vezes que a instrução aparece no script acima. Para que os valores exibidos na 
  tela sejam, nessa ordem, 42 e 21.0, quais operadores matemáticos devem substituir 'XXX' e 'YYY' no 
  trecho de código, respectivamente?
""" 

var1 = 12
var2 = 30
var3 = var1 + var2

print(var3)

var3 = var3 / 2

print(var3)

"""
  Questão 2
  Algumas situações requerem que os dados sejam recebidos diretamente pelo usuário como parte da execução 
  do programa. Isso pode ser feito com a função input(). No entanto, esta função sempre retorna os valores 
  em string. Assim, se os dados esperados do usuário forem numéricos, é importante realizar a conversão dos 
  tipos de dados para que eles possam ser processados. Considere o trecho abaixo:

  num1 = XXX
  dobro = 2*num1
  print("O dobro do número digitado é:", dobro)

  Levando em consideração que o usuário pode entregar qualquer número como input, o 'XXX' no código acima deve 
  ser substituído por qual elemento?
"""

num1 = float( input("Digite um número a seguir: ") )
dobro = 2 * num1

print('O dobro do número digitado é:', dobro)

"""
  Questão 3
  Para a construção de programas flexíveis e mais complexos, é necessário que haja a realização de comparações. 
  Isso é possível com o uso de operadores lógicos de comparação (em python: ==, !=, <, <=, >, >=), como mostra 
  o código:

  x = 10
  y = 4.2
  num = float(input("Digite um número a seguir: "))

  print(num > x*y, num <= x + y, num*y != x*y)

  Suponha que na execução do script acima, o usuário digitou o valor 10, quando solicitado pelo input. 
  Qual das alternativas a seguir produz o mesmo output que o script acima?
"""

x = 10
y = 4.2
num = float(input("Digite um número a seguir: "))

print(
        num > x*y,      # false
        num <= x + y,   # true
        num*y != x*y    # false
    ) 

print(
        num == x*y,     # false
        num*y == x*y,   # true
        y > x + num     # false
    )


"""
Questão 4
Em muitos programas é necessário que mais de uma expressão lógica seja avaliada, de maneira composta. 
É possível realizar a composição lógica através dos operadores and e or do Python. Além disso, o operador 
not é utilizado para inverter o valor lógico de um booleano ou expressão lógica como um todo.

x = 4.2

y = 10

z = "42"

not (((x * y == z) and not (x < y)) or y % 2 == 0)

Qual das seguintes alternativas contém uma expressão que resulta no mesmo valor lógico (True ou False) 
que a última linha do código acima?
"""

x = 4.2

y = 10

z = "42"

print( not (((x * y == z) and not (x < y)) or y % 2 == 0) )

print( not (((not True) or int(z) % 7 == 0) and ((str(int(x*y)) == z) and (type(x) != type(z)))) )


"""
    Questão 5
    Um dos principais usos destinados aos operadores lógicos é a construção de expressões condicionais, 
    que são utilizadas para (re)direcionar o fluxo de um programa. Isso é possível com as expressões if, 
    elif e else em Python.

    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))
    c = int(input("Digite o terceiro número inteiro: "))

    if a > b and a > c:

    resposta = a % 2 == 0

    elif b > a and b > c:

    resposta = b % 2 == 0

    else:

    resposta = c % 2 == 0

    print(XXX, resposta)

    Pelo que o "XXX" deve ser substituído no código acima (ou seja, o que este código efetivamente faz?)
"""

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a > b and a > c:
    resposta = a % 2 == 0
elif b > a and b > c:
    resposta = b % 2 == 0
else:
    resposta = c % 2 == 0

print("O maior número entre os três informados é par?", resposta)