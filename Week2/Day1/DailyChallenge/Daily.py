#Using the input function, ask the user for a string. The string must be 10 characters long.
#If it’s less than 10 characters, print a message which states “string not long enough”.
#If it’s more than 10 characters, print a message which states “string too long”.
#If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

user = input("tell me a word with at least 10 letters:\n")
if len(user) < 10:
    print(f"String is not enought")
elif len(user) > 10:
    print(f"string too long") 
else: 
    print(f"perfect string ")  

# Then, print the first and last characters of the given text.   
print("first:", user[0], "last:", user[len(user)-1])

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
#The user enters "HelloWorld"
#Then, you have to construct the string character by character
#H
#He
#Hel
#... etc
#HelloWorld

#for x in range(0):
#    print(x)

# value loop
for x in range(len(user)):
    for y in range(x+1):
        print(user[y], end="")
    print("")

#string characters loop
#for x in user:
#    print(x)
