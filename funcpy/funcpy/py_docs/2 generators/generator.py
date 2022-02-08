
#-----------------------------------------------------------------------------------------------------------------

# A simple function returning a generator object

def generate_ints(N):
    for i in range(N):
        yield i

#-----------------------------------------------------------------------------------------------------------------

gen = generate_ints(2)

gen  # <generator object generate_ints at 0x7fc175b01e40>

next(gen)    # 0

next(gen)   # 1

# next(gen))  # File "generator.py", line 22, in <module> | StopIteration

#-----------------------------------------------------------------------------------------------------------------

gen2 = generate_ints(3) 

a, b, c = iter(gen2)  # a = 0, b = 1, c = 2

a, b, c # 1 2 3

#-----------------------------------------------------------------------------------------------------------------

gen3 = generate_ints(2)

for i in gen3:
    i

#-----------------------------------------------------------------------------------------------------------------

def counter(maximum):
    incrementer_number = 0      # incrementer_number is a local variable

    while incrementer_number < maximum:         # 
        value = (yield incrementer_number)

        if value is not None:
            incrementer_number = value

        else:
            incrementer_number += 1


counter_mod = counter(50)

counter_mod.__next__()   # 0

counter_mod.send(49)     # 48

# counter_mod.__next__()   # File ./generator.py:62, in <module> | StopIteration: 