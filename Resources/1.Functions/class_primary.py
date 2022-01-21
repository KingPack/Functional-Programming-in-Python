

# Funçoes com objetos de primeira classe

    # Exemplo 1 
lista = [1, 'str', [1,2], (1,2), {1,2}, {1: 'um'}]


func = lambda x: x   # a função foi armazenada em uma variavel

    # exemplo 2
def func_2(x):
    return x + 2

lista2 = [func, func_2]

lista3 = [lambda x: x, lambda x: x+1]

# Exemplo 3

valor = 5 

def mais_cinco(x):
    return x + 5

assert mais_cinco(5) == 10

valor = 7

assert mais_cinco(5) == 10


# Exemplo 4
valor = 5

def teste():
    global valor
    valor = 7

# print(valor)

# Exemplo 5

func = lambda  x: x+2

# print(func(10)) 

def func_mais_2(funcao, valor):
    return funcao(valor) + 2



assert func_mais_2(func, 2)  == 6


def func_quadrada(val):
    return val * val

assert func_mais_2(func_quadrada, 2) == 6
