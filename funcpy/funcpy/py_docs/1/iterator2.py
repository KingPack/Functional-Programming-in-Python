
# ---------------------------------------------------------------------------------------------------------------------
dates = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

# Documention for the iterator object: https://docs.python.org/pt-br/3/howto/functional.html#data-types-that-support-iterators
for key in dates:
    key, dates[key]


for key, value in dates.items():
    key, value


for key in dates.keys():
    key


for key in dates.values():
    key

# ----------------------------------------------------------------------------------------------------------------------

list_random = [('Italy', 'Rome'), ('France', 'Paris'), ('US', ['Washington DC', 'New York', 'Miami'])]

dict_random = dict(iter(list_random))


# ----------------------------------------------------------------------------------------------------------------------

# with open('/home/hendrek/Documents/GitHub/KingPack/Functional-Programming-in-Python/funcpy/funcpy/py_docs/1/file_values.txt', 'r') as file:
    
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)

    # for line in iter(file):
        # print(line, 12)
    # itere = iter(file)
    # print(next(itere))
    # print(next(itere))
    # print(next(itere))
    # print(next(itere))
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())