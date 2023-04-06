'''
Topic : Patterns
'''
n = 5

# Pattern 1
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()

# pattern 2
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()

# Pattern 3
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print()

# Pattern 4
for i in range(n): 
    for j in range(i):
        print(" ",end="")
    for k in range(n-i,0,-1):
        print("* ",end="")
    print()
