# ----------------------------------------------------------------------------------------------------------------------

line_list = ['  line 1\n', 'line 2  \n', 'line 3\n', 'line 4\n']

# returns iterator object
stripped_iter = (line.strip() for line in line_list)

# returns list
stripped_list = [line.strip() for line in line_list]

# conditional if in list comprehension
stripped_list2 = [line.strip() for line in line_list if line != ""]

# ----------------------------------------------------------------------------------------------------------------------

# combinations in list comprehension

sequence1 = 'abcd'

sequence2 = (1, 2, 3, 4)

list_sequence = [(x, y) for x in sequence1 for y in sequence2]

# ----------------------------------------------------------------------------------------------------------------------