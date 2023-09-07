# Exercise 1 : Set

# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

#my_favorite_numbers = {5, 7, 13, 21}
#my_favorite_numbers.update([15, 25])
#print(my_favorite_numbers)
#my_favorite_numbers.remove(25)
#print(my_favorite_numbers)

#friends_fav_numbers = {2,4,8}
#our_fav_numbers = my_favorite_numbers | friends_fav_numbers
#print(our_fav_numbers)

# Exercise 2: Tuple

# Given a tuple which value is integers, is it possible to add more integers to the tuple?
#my_tuple = (2, 3, 5)
#Tuples are immutable

#Exercise 3: List
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append('Kiwi')
# basket.insert(0, "Apples")
# basket.count("Apples")
# basket.clear()
# print(basket)

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# Exercise 4: Floats

# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# float_list = [float(i) / 2 for i in range(3, 11)]
# print(float_list)


# Exercise 5: For Loop

# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

# for x in range(1, 21):
#     print(x)
# for num in range(1, 21):
#    if num % 2 == 0:
#        print(num)
    
# Exercise 6 : While Loop
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.    
# name = "Oxana"
# while True:
#    guess = (input("Guess the name:"))
#    if guess == name:
#        print("Correct")
#        break
#    else:
#        print("Try again")

# Exercise 7: Favorite Fruits

# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print .
# If the user’s input is NOT in the list, print, “”.

# list_fruits = input("Tell me your favorite fruits")
# user_favorite = list_fruits.split()
# print(user_favorite)
# user = input("Type a name of any fruit")
# if user.strip() in user_favorite:
#     print('You chose one of your favorite fruits! Enjoy!')
# else: 
#     print('You chose a new fruit. I hope you enjoy')


# Exercise 8: Who Ordered A Pizza ?

# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

#finish = "quit"
#list = []
#while True:
#    topping = input("Enter topping or 'quit':\n")
#    list.append(topping)
#    print(list) 
#    if topping == finish:
#        break
#    else:
#        print("  I'll add " + topping + " to your pizza.")
#        list.append(topping)
#        print(list)

#Exercise 9: Cinemax

#A movie theater charges different ticket prices depending on a person’s age.
#if a person is under the age of 3, the ticket is free.
#if they are between 3 and 12, the ticket is $10.
#if they are over the age of 12, the ticket is $15.

#Ask a family the age of each person who wants a ticket.

#Store the total cost of all the family’s tickets and print it out.

#A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
#Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
#At the end, print the final list.

#while True: 
#    age = input("Enter your age or 'q' to quit: ") 
#    if age == 'q': 
#        break 
#    age = int(age) 
#    if age < 3: ticket_cost = 0 
#    elif age <= 12: ticket_cost = 10 
#    else: ticket_cost = 15 
#    print(f"The cost of your movie ticket is ${ticket_cost}.") 
    
#total_price = 0
#while True:
#    age = input("Enter your age or 'q' to quit: ") 
#    if age == 'q': 
#        break 
#    age = int(age) 
#    if age <= 3:
#        ticket_cost = 0 
#    elif age <= 12:
#        ticket_cost = 10 
#    else:
#        ticket_cost = 15 

#    total_price = total_price + ticket_cost
#    print(f"The cost of your movie ticket is ${ticket_cost}.") 
    
#print(f"Total price is ${total_price}.") 

#name_list = ["Dan", "Ron", "Sam"]
#loop_list = name_list.copy()
#for x in loop_list :
#    print("hello '{}' " .format(x), end="")
#    age = int(input("Enter your age: "))
#    if age < 16 or age > 21:
#        name_list.remove(x)

#print(name_list)

#Exercise 10 : Sandwich Orders

#Using the list below :

#sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

#The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
#We need to prepare the orders of the clients:
#Create an empty list called finished_sandwiches.
#One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
#After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
#I made your tuna sandwich
#I made your avocado sandwich
#I made your egg sandwich
#I made your chicken sandwich

#finished_sandwiches = []

#print("I'm sorry, we're all out of pastrami today.")
#while 'pastrami' in sandwich_orders:
#    sandwich_orders.remove('pastrami')

#print("\n")
#while sandwich_orders:
#    current_sandwich = sandwich_orders.pop()
#    print(f"I'm working on your {current_sandwich} sandwich.")
#    finished_sandwiches.append(current_sandwich)

#print("\n")
#for sandwich in finished_sandwiches:
#    print(f"I made a {sandwich} sandwich.")