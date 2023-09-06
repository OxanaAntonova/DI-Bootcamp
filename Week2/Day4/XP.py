#Exercise 1 : What Are You Learning ?

#Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
#Call the function, and make sure the message displays correctly.
#def display_message() :
#    print(f"I'm learning in developers course")
    
#display_message()    

# Exercise 2: What’s Your Favorite Book ?

#Write a function called favorite_book() that accepts one parameter called title.
#The function should print a message, such as "One of my favorite books is <title>".
#For example: “One of my favorite books is Alice in Wonderland”
#Call the function, make sure to include a book title as an argument when calling the function.

#def favorite_book(title) :
#    print(f"One of my favorite books is {title}")
    
#favorite_book("Alice in Wonderland")

#Exercise 3 : Some Geography

#Write a function called describe_city() that accepts the name of a city and its country as parameters.
#The function should print a simple sentence, such as "<city> is in <country>".
#For example “Reykjavik is in Iceland”
#Give the country parameter a default value.
#Call your function.

#def describe_city(city, country) :
#    print(f"{city} is in {country}")
    
#describe_city("NY", "USA")    

#Exercise 4 : Random

#Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
#Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
#def numbers() :
#    random_number = .randint(1,100)
#print()

#def numbers()  

#Exercise 5 : Let’s Create Some Personalized Shirts !

#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
#The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
#Call the function make_shirt().


#def make_shirt(size, message):
#    print(f"\nThe size of the shirt is {size} and the message is {message}")

#make_shirt('small', 'I like it!')

#Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
#Make a large shirt with the default message
#Make medium shirt with the default message
#Make a shirt of any size with a different message.
#Bonus: Call the function make_shirt() using keyword arguments.


#def make_shirt(size='large', message='I love Python!'):
    #print(f"\nThe size of the shirt is {size} and {message}")
    #print(f"\nThe size of the shirt is medium and {message}")
    #print(f"the size of the shirt is {size} and {message}")
#make_shirt()
#make_shirt('large')
#make_shirt()
#make_shirt("small", "this is good")
#make_shirt(size="small", message='OK')


#Exercise 6 : Magicians …

#Create a function called show_magicians(), which prints the name of each magician in the list.
#Write a function called  make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
#Call the function make_great().
#Call the function show_magicians() to see that the list has actually been modified.
#magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

#def show_magicians(magicians):
#    for magician in magicians:
#        print(magician.title())
#show_magicians(magician_names)

#def make_great(magicians) :
#    for i in range(len(magicians)):
#        magicians[i] = magicians[i] + " The Great"
    
#make_great(magician_names)
#show_magicians(magician_names)

#Exercise 7 : Temperature Advice

#Create a function called get_random_temp().
#This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
#Test your function to make sure it generates expected results.

#Create a function called main().
#Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
