import copy

# create 1st dictionary
dictionary1 = {}

# create 2nd dictionary
dictionary2 = {'1': 'one',
               '2': 'two',
               '3': 'three'
               }

# add to 1st dictionary new pair key-value
dictionary1['4'] = 'four'

# add 2nd dictionary to 1st
dictionary1.update(dictionary2)

# delete one key-value from 1st dictionary via .pop
dictionary1.pop('3')
print(dictionary1)

# delete one key-value from 1st dictionary via .popitem
dictionary1.popitem()
print(dictionary1)

# deepcopy to new var
new_var = copy.deepcopy(dictionary1)
print(new_var)

# add a new key and (value = dictionary1)
new_var[5] = dictionary1
print(new_var)
print(dictionary1)

# list of keys
list_of_keys = dictionary1.keys()
print(list_of_keys)

# list of values
list_of_values = dictionary1.values()
print(list_of_values)
