
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

numbers = {2, 3 ,5, 7, 11, 13}

for value in numbers:
    value

# ----------------------------------------------------------------------------------------------------------------------