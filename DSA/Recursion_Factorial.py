"""
Recursion - Factorial

"""
def fact(n):
    if n <= 1:
        return 1
    else:
        sum = n*fact(n-1)
        n = n-1
        return sum

print(fact(10))
