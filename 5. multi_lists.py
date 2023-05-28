# create 3x list
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
print(a)
a[1].append(17)
print(a)

# create a list + dictionary
b = [[1, 2], [5], {'1': 'one'}]
print(b)

# create a dictionary + list
c = {
    '2': 'two',
    '3': 'three',
    'key': [5, 6]
    }
print(c)

# save list from dictionary to new var
d = c['key']
print(d)