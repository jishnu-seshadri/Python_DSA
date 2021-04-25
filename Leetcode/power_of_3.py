def isPowerOfThree(n):
    if n == 1:
        return True
    elif n<1:
        return False
    else:
        return isPowerOfThree(n/3)
        

        