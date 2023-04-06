# WAP to remove all the duplicate from a string
string = input("Enter your string : ")
newstr = []

for i in range(len(string)):
    if string[i] in newstr :
        continue
    newstr.append(string[i])

newstr = "".join(newstr)
print("New string without duplication is :",newstr)