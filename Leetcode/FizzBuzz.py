def fizzBuzz(n):
    ans = []
    for i in range(1, n+1):
        temp = ''
        if i%3==0:
            temp = "Fizz"
        if i%5==0:
            temp = temp + "Buzz"
        if i%3 !=0 and i%5!=0:
            temp = temp + str(i)
        ans.append(temp)
    return ans

print(fizzBuzz(11))