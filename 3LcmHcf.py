# WAP to calculate HCF and LCM of two numbers
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

# LCM function
def lcm(num1,num2):
    for i in range(1,num1*num2):
        if(i%num1==0 and i%num2==0):
            return i
    return num1*num2
    
# HCF function
def hcf(num1,num2):
    for i in range(num1,1,-1):
        if(num1%i==0 and num2%i==0):
            return i
    return 1
    
# function call
lcm = lcm(num1,num2)
hcf = hcf(num1,num2)
print("\nLCM of numbers is",lcm,"and HCF of numbers is",hcf)