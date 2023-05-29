# create a tuple
tuple1 = (1, 2, 3, 4, 5, 6, 7)
print(tuple1)
print('\n\n')

# create a set
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {5, 6, 7, 8, 9, 10, 11}

# add to set1 0
set1.add(0)

# .intersection() set1
a = set1.intersection(set2)

# .difference() set1
b = set1.difference(set2)

# symmetric_difference() set1
c = set1.symmetric_difference(set2)

# print a b c
print(set1)
print(a)
print(b)
print(c)
