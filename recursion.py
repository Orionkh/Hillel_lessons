def recursion_fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return recursion_fib(n-1) + recursion_fib(n-2)
print(recursion_fib(7))
