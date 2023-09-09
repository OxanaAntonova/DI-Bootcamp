#Exercise 1 : What Are You Learning ?

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

#import random
#def random_number(user_num) :
#    rand_num = random.randint(1, 100)
#    if user_num == rand_num :
#        print("Good: ", rand_num)
#    else :
#        print("Bad ", user_num, rand_num)

#i = 1
#while i < 101:
#    random_number(i)
#    i += 1

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
#import random
#def get_random_temp(season) :
#    temp = 0
#    if season == "winter":
#        temp = random.randint(-10, 16)
#    elif season == "spring" or season == "autom":
#        temp = random.randint(15, 25)
#    elif season == "summer" :
#        temp = random.randint(26, 40)
#    else :
#        print("Wrong season", season)
#        return

#    print("Current temperature is: ", temp)
    #if season (parameter) is winter get random from -10 to 16. If spring or autom get rand between 15-25, 
    #if summer get rand between 26 to 40.
#    return

#def main():
#    season = input("Tell me the season: ")
#    get_random_temp(season)

    #ask the user for the season and call get_random_temp with the seaso.
    #cur_temp = get_random_temp()
    #print ("The temperature right now is", cur_temp, "degrees Celsius")

    #if cur_temp < 16:
        #print("Don't forget your coat")    
#main()   


#Create a function called main().
#Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

#Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
#below zero (eg. “”)
#between zero and 16 (eg. )
#between 16 and 23
#between 24 and 32
#between 32 and 40

#Change the get_random_temp() function:
#Add a parameter to the function, named ‘season’.
#Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
#Now that we’ve changed get_random_temp(), let’s change the main() function:
#Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
#Use the season as an argument when calling get_random_temp().

#Bonus: Give the temperature as a floating-point number instead of an integer.
#Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

# exercise Star war
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def check_answers () :
    number_correct_answers = 0 
    number_incorrect_answers = 0 
    list_wrong_answers = [] 

    print("\n ---- The quizz starts ----")
    for quizz in data : # loop 
        user_answer = input(quizz["question"]) 
        if user_answer.lower() == quizz["answer"].lower(): 
            number_correct_answers += 1 
        else :
            number_incorrect_answers += 1 
            new_quizz = quizz.copy() 
            new_quizz["user_answer"] = user_answer 
            list_wrong_answers.append(new_quizz) 
    
    inform_user(number_correct_answers, number_incorrect_answers, list_wrong_answers) 

def inform_user (correct, incorrect, wrong_answers) : 
    print("\n ----------------------------")
    print(f"You have {correct} correct answers")
    print(f"You have {incorrect} incorrect answers")
    for global_answer in wrong_answers : 
        print(f'The question was {global_answer["question"]}')
        print(f'Your answer was {global_answer["user_answer"]}')
        print(f'Your got it wrong, the correct answer is {global_answer["answer"]}')
    
    print("\n --------------------")
    if incorrect > 3 :
        print(" YOU GOT MORE 3 ANSWERS WRONG Play Again")
        check_answers()
    else :
        print("Good Job - YOU DONT NEED TO REDO THE GAME")

check_answers() 

