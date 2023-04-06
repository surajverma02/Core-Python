# WAP to calculate factorial of a number
n = int(input("Enter number : "))

# factorial function
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
# function call
factorial = fact(n)
print(factorial)