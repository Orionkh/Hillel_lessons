int1 = 32
int2 = 30

# 1st variant
ternary1 = True if int1 >= 33 else False
print('Object {} is vegetable: {}'.format(int1, ternary1))

# 2nd variant
if int2 <= 35:
    ternary2 = True
else:
    ternary2 = False
print('Object {} is vegetable: {}'.format(int2, ternary2))