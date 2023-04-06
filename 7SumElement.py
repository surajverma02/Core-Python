# WAP to calculate Sum of elements of a list
list = [2, 5, 6, 9, 4, 8, 9, 5, 7]
sum = 0

for i in range(len(list)):
    sum += list[i]

print("Sum of elemens is",sum)