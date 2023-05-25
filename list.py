new_list = [1, 2, 3, 4, 5, 6, 7, 'lol']

print(new_list)
# copy list
new_list2 = new_list.copy()
# add new element to the list via append
new_list2.append('cheburek')

print(new_list2)
# add new element to the list via insert
new_list2.insert(8, 'kek')

print(new_list2)
# add one list to another via extend
new_list3 = [ 'a1', 'a2']
print(new_list3)

new_list3.extend(new_list)

print(new_list3)
# add one list to another via append
new_list3.append(new_list)

print(new_list3)
# show character from new_list3 via pop
pop_character = new_list3.pop(9)
print(pop_character)
# remove element by value
new_list3.remove(2)

print(new_list3)
#delete item by index
del new_list3[0]

print(new_list3)
# value of element by index
print(new_list3[0])

# slices

list1 = (8, 'kek', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
name = 'one', 'two', 'three', 'four'

rev_name = name[::-1]
print(name)
print(rev_name)

rev_list = list1[::-1]
print(list1)
print(rev_list)

sliced_list = list1[2:7:3]
print(sliced_list)

rev2_name = name[2:4]
print(rev2_name)