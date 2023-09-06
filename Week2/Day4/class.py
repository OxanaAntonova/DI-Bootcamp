# create a function that takes a number as an argument, and check if this number is even or odd
#2. create a function that takes a list of numbers as an argument, and check if each number is even or odd


#def numbers (num) :
#    if num % 2 == 0:
#        print(f"The numbers are even")
#    else:
#        print(f"The numbers are odd")   
        
#numbers(7)       

#def calculation (list_numbers) :
    #for num in list_numbers :
#       if num % 2 == 0:
#      print(f"The numbers are even")
#       else:
#           print(f"The numbers are odd") 
    
#calculation([2, 5, 120])   


#1st function - get_price_car
#receive the age of the user 
#and if the user is > 40
#    --> 200
#if the user is < 40
#    --> 300
    
def get_price_car(age_user) :
    if age_user > 40 :
        return 200
    else:
        return 300    
    
def get_flight_price(destination) :
    if destination == "Paris" :
        return 400
    else:
        return 600  
    
def inform_user_vacation() :
    price_car = get_price_car(45)
    flight_price = get_flight_price("NY")
    total = price_car + flight_price
    print(f"your vacation ill cost {total}")
    
    inform_user_vacation()

#2nd function - get_price_flight
#receive a destination from the user
#if the destinatation is Paris
#    --> 400
#if the destinatation is Paris
#    --> 600


#3rd function
#is going to use the result from the 2 functions above
#and inform the user of the total price of the vacation
