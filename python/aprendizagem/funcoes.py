# > Funções

# 1. O que são funções e porque utilizá-las?

# Funções aprendidas anteriormente...
"""
print() # - Imprimi uma mensagem (int, float, str) no console (terminal, cmd)
input() # - Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
len()   # - Recebe uma lista e retorna o tamanho dessa lista
max()   # - Retorna o maior valor de uma lista"""

# 2. Criação de Funções

# Função Inicial

def saudacao():
    print('Seja bem-vinda(o)!')
    print('Olá, é um prazer ter você fazendo parte deste curso!')

saudacao()

# Funções com Parâmetros

def saudacao(nome, curso):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Matheus', 'Python')

# Funções com Parâmetros Default

def saudacao(nome, curso='Python'):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Matheus')

# > Se não informado o valor na 'saudacao', ele segue conforme definido como padrão,
#   Caso contrário, ele utilizará o que for definidado dentro da variável 'saudacao' 
def saudacao(nome, curso='Python'):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Matheus', 'CSS')

# Funções com Retorno
"""
    Utilização do 'return' sempre indicado utilizar ao fim da função, pois a partir
    não é mais considerado linhas de códigos
"""
def soma(num1, num2):
    return num1 + num2  

resultado = soma(5, 7)

print('O resultado da soma é:', resultado)


def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    else:
        return num1 / num2
    
resultado = calculadora(10, 20, '*')

print('O resultado da operação é:', resultado)