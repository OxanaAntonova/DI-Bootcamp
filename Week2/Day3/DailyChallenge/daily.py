#Ask a user for a word
#Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

#Make sure the letters are the keys.
#Make sure the letters are strings.
#Make sure the indexes are stored in a list and those lists are values.

#word = "froggy"
#letters_dict = {}
#for index, letter in enumerate(word) :
#    if letter in letters_dict: 
#        letters_dict[letter].appened(index)
#    else :
#        letters_dict[letter] = [index]
#        print(letters_dict)  
        
#Challenge 2
#Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
#Sort the list in alphabetical order.
#Return “Nothing” if you can’t afford anything from the store.
wallet = "$300"
total_amount = 0
items_bought = []
convert_wallet = int(wallet.replace("$", ""))

for key, value in items_bought.items():
    convert_value = int(value.replace("$", "").replace(",", ""))
    if convert_value < convert_wallet :
        total_amount += convert_value
        items_bought.append(key)