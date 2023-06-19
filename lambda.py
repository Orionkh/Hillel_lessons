# #1
one = lambda x, y=100: [print(x) for _ in range(y)]

one(511)

# #2
two = lambda x, y: [print(x) if x > y else print(y)]

two(15, 10)

# #3
three = lambda : print(10)

three()