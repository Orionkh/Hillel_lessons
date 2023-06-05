def sum_range(start, end):
    if start > end:
        start, end = end, start
    x = 0
    for i in range(start, end + 1):
        x += i
    return x
# 1st int > 2nd int
a, b = 5, 2
print(sum_range(a, b))

