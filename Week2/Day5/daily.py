#Challenge1

#items=[x for x in input("Enter Words :").split(',')]
#items.sort()
#print(','.join(items))

#Challemge2
sentence = input("Enter sentence: ")
longest = max(sentence.split(), key=len)
print("Longest word is: ", longest)
