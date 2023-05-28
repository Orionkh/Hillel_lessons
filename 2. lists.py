import copy

# simple list with nested list
a = [1, 2, [3, 4, 5], 6, 7]

# create a var = simple list with nested list
b = a

# shallow copy
c = copy.copy(a)

# deep copy
d = copy.deepcopy(a)

# print all lists
print(a)
print(b)
print(c)
print(d)
print('\n\n')

# append to simple list with nested list
a[2].append(8)

# print all lists again
print(a)
print(b)
print(c)
print(d)
