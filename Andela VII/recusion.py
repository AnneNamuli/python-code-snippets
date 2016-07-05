# find the factorial of a number
def recur_fact(x):
    if x == 1:
        return 1
    else:
        return (x * recur_fact(x-1))

num = int(input("Enter a number: "))
if num >= 1:
    print("The factorial of", num, "is", recur_fact(num))
