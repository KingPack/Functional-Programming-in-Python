list_number = [1, 2, 3, 4]

iterator = iter(list_number)

next(iterator)
iterator.__next__()


for x in iter(list_number):
    x


tuple_iterator = iter(list_number)
tuple_number = tuple(tuple_iterator)
tuple_number


interator_var = iter(list_number)

one, two, three, four = interator_var


one
two
three
four