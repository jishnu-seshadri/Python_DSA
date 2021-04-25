"""
Recursion - Fibonacci

"""
def fib(n):
    if n <= 1:
        return 1
    else:
        return n + fib(n-1)


