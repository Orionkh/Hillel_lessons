try:
    print(10 / 0)
except ArithmeticError as ex:
    print(f'Error {ex}')

finally:
    print('1st block')

a = (1, 2, 3)
try:
    a.append(4)
except Exception as ec:
    print(f'Error {ec}')

finally:
    print(a)
    print('2nd block')
