# WAP to illustrate various functions of math module & statistics module
import math
import statistics as stat

while(True):
    print("\nChoose statistics function :")
    print("1. Statistics function\n2. Math function\n3. Exit(any key)")
    choice = input("Enter your choice : ")
    if(choice=='1'):
        # function call
        numbers = [2, 5, 6, 4, 8, 9, 12, 5, 2]
        print(f"List of  numbers : {numbers}")
        i = 1
        while(i<10):
            print("\nChoose statitics function :")
            print("1. mean()\n2. mode()\n3. median()\n4. Exit(any key)")
            choice = input("Enter your choice : ")
            if(choice=='1'):
                print(f"Mean of list is : {stat.mean(numbers)}")
            elif(choice=='2'):
                print(f"Mode of list is : {stat.mode(numbers)}")
            elif(choice=='3'):
                print(f"Median of list is : {stat.median(numbers)}")
            else:
                print("Exit")
                i = 10
    elif(choice=='2'):
        # function call
        j =1
        while(j<20):
            print("\nChoose math function :")
            print("1. sqrt()\n2. log10()\n3. pow()\n4. Exit(any key)")
            choice = input("Enter your choice : ")
            if(choice=='1'):
                num = int(input("Enter number : "))
                print("Square root of",num,"is",math.sqrt(num))
            elif(choice=='2'):
                num = int(input("Enter number : "))
                print("log of",num,"with base 10",math.log10(num))
            elif(choice=='3'):
                base = int(input("Enter base : "))
                power = int(input("Enter power : "))
                print(base,"to power",power,"is",math.pow(base,power))
            else:
                print("Exit")
                j=20
    else:
        print("Exit")
        exit()