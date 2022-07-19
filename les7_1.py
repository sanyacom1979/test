n = int(input())

def factorial(n):

    if  n > 1:
        n *= factorial(n-1)

    return n

print(factorial(n))

