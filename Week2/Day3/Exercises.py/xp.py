#Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]
#test_dict = {key: value for key, value in zip(keys, values)}
#print(test_dict)



# Exercise 2 : Cinemax

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
#Bonus: Ask the user to input the names and ages instead of using the provided family variable 
# (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8} 
#UserWarning = input("What is you name and How old are you?")

#while True: 
    #age = input("Enter your age or 'q' to quit: ") 
    #if age == 'q': 
    #   break 
    #age = int(age) 
    #if age < 3: ticket_cost = 0 
    #elif age <= 12: ticket_cost = 10 
    #else: ticket_cost = 15 
    #print(f"The cost of your movie ticket is ${ticket_cost}.") 

#brand = {
#    'name': 'Zara',
#    'creation_date': 1975,
#    'creator_name': 'Amancio Ortega Gaona',
#    'type_of_clothes': ['men', 'women', 'children', 'home'],
#    'international_competitors': ['Gap', 'H&M', 'Benetton'],
#    'number_stores': 7000,
#    'major_color': {
#        'France': 'blue',
#        'Spain': 'red',
#        'US': ('pink', 'green')}
#}  
#brand['number_store'] = 2
#print(brand['number_store'])
#print(f"Zara's clients are {brand['type_of_clothes']}")
#brand['country_creation'] = 'Spain'
#print(brand)


# Exercise 4 : Disney Characters
#users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
#1/
# print(disney_users_A)
#{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#users_a = {}
#for i, value in enumerate(users):
#    users_a.update({i: value})
#    print(users_a)

#2/
#print(disney_users_B)
#{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#users_b = {}
#for i, key in enumerate(users):
#    users_b.update({i: key})
#    print(users_b)

#3/ 
#print(disney_users_C)
#{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
#users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
#users_c = {}
#for i, value in enumerate(users):
#        users_c.update({i: value})
#print(sorted(users_c.items()))


#users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
#for i in users:
#    res=i.isalpha()
#    print(i, res )

#users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
#res = []
#check = "M" 
#for i in users:
#    if (i.find(check) == 0):
#        res.append(i)
#        print(res)
        
    
# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

