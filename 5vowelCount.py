# WAP to count number of vowel in a string
string = input("Enter your string : ")
vowel = ('a','e','i','o','u')
count = 0

for i in range(len(string)):
    if(string[i] in vowel):
        count +=1
print("Number of vowel in string is",count)