#Challenge 1
#Ask the user for a number and a length.
#Create a program that prints a list of multiples of the number until the list length reaches length.
#Examples

#number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

#number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

#number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

#user_answer = input("give me a number and a length separated by a comma")
#list_answer = user_answer.split(",")
#number = int(list_answer[0])
#length = int(list_answer[1])
#list_multiples = []
#for x in range (length):
#    multiple = number * (x + 1)
#    list_multiples.append(multiple)
#    print(list_multiples)

#Challenge 2
#Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
#Examples

#user's word : "ppoeemm" ➞ "poem"

#user's word : "wiiiinnnnd" ➞ "wind"

#user's word : "ttiiitllleeee" ➞ "title"

#user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"

word = "ttttitllllleeee"
new_word = word [0]
first_letter = word[0]

for number in range (1, len(word)) :
    if word[number] != new_word[-1] :
        new_word += word[number]
        print(new_word)

