list_number = [1, 2, 3, 4]

iterator = iter(list_number)

next(iterator)
iterator.__next__()


for x in iter(list_number):
    print(x)


tuple_iterator = iter(list_number)
tuple_number = tuple(tuple_iterator)
print(tuple_number)


interator_var = iter(list_number)

one, two, three, four = interator_var
print(one)
print(two)
print(three)
print(four)