string = 'python'

lista = []

for letra in string:
    lista.append(letra)

print(lista)


string2 = lambda x: x

lista2 = list(map(str, string2('python')))

print(lista2)