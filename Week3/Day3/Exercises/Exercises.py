#Exercise 1: Currencies

#class Currency:
#    def __init__(self, currency, amount):
#        self.currency = currency
#        self.amount = amount

#    def __str__(self):
#        return f'{self.amount} {self.currency}'
    
#    def __int__(self):
#        return self.amount
    
#    def __repr__(self):
#        return (repr(self.amount) + ' ' + self.currency)

#    def __add__(self, other):
#        print("ADD Called")
#        if (type(other) is int):
#            return self.amount + other
#        else:
#            if (self.currency != other.currency):
#                print("Can't add between Currency type ",  self.currency, "and", other.currency)
#                return
#            return self.amount + other.amount

#    def __iadd__(self, other):
#        print("IADD Called")
#        if (type(other) is int):
#            self.amount += other
#        else:
#            self.amount += other.amount
#        return self
#Using the code above, implement the relevant methods and dunder methods which will output the results below.
#Hint : When adding 2 currencies which don’t share the same label you should raise an error.
#c1 = Currency('dollar', 5)
#print(str(c1))
#print(int(c1))
#print(repr(c1))
#print(c1 + 5)

#c2 = Currency('dollar', 10)
#print(c1 + c2)

#c1 += 5
#print(int(c1))

#c1 += c2
#print(int(c1))

#c3 = Currency('shekel', 10)
#c4 = Currency('shekel', 10)

#print(c1 + c3)

#Exercise 2: Import

#In a file named func.py create a function that adds 2 number, and prints the result
#In a file namedexercise_one.py import and the function
#Hint: You can use the the following syntaxes:

#import module_name 

#OR 
#from module_name import function_name 
#OR 
#from module_name import function_name as fn 
#OR
#import module_name as mn

#Exercise 3: String Module

#Generate random String of length 5
#Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
#Hint: use the string module
#import random 
#import string 
#def Upper_Lower_string(length): 
#    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length))) 
#    print(" Random string generated in Lowercase: ", result) 

#    result1 = ''.join((random.choice(string.ascii_uppercase) for x in range(length))) 
#    print(" Random string generated in Uppercase: ", result1) 

#Upper_Lower_string(5) # define the length 

#Exercise 4 : Current Date

#Create a function that displays the current date.
#Hint : Use the datetime module.
#from datetime import date

#current_date = date.today()
#print(current_date)
#Exercise 5 : Amount Of Time Left Until January 1st

#Create a function that displays the amount of time left from now until January 1st.
#(Example: the 1st of January is in 10 days and 10:34:01hours).

#from datetime import date

#future_date = date(2024, 1, 1)
#delta = future_date - current_date
#print(delta)

#Exercise 6 : Birthday And Minutes

#Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

#import datetime

#current_date=datetime.datetime.now().date()
#birth_day=datetime.date(1977,5,15)

#delta1 = (current_date - birth_day) * 1440
#print(f"You lived {delta1} min")
