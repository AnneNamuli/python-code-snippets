def recursive_factorial(n):
   if n <= 1:
       return 1
   else:
       return n * recursive_factorial(n-1)


def iterative_factorial(n):
    product = 1
    for i in range(n):
        product *= i + 1
    return product