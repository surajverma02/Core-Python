# WAP to print fibonacci series of a number of term
n = int(input("Enter number of term : "))

# fabonacci series function
def fabo(n):
    n1,n2 = 0,1
    print("\nFibonacci series : ",end="")
    if n==1:
        print("0")
    elif n>=2:
        print("0",end=" ")
        for i in range (2,n+1):
            print(n2,end=" ")
            n1,n2 = n2,n1+n2   
                
    else:
        print("Enter a valid number of term.")

fabo(n)