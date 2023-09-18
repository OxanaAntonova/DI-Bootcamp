#class Cat:
#    def __init__(self, cat_name, cat_age):
#        self.name = cat_name
#        self.age = cat_age      
#def oldest_cat(*args):
#    oldest_cat = args[0]
#    for cat in args :
#        if cat.age > oldest_cat.age:
#            oldest_cat = cat
#    return oldest_cat

#cat1 = Cat("Marusya", 8)        
#cat2 = Cat("Ginger", 5)        
#cat3 = Cat("Murzik", 12)  

#x = oldest_cat(cat1, cat2, cat3)

#print(f"The oldest cat is {x.name}, and is {x.age} years old.")


#Create a class called Dog.
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")   
    def jump(self):
        self.height = self.height * 2
        print(f"{self.name} jumps {self.height} cm high!") 

    
davids_dog = Dog("Rex", 50)  
davids_dog.bark()
davids_dog.jump()
sarahs_dog = Dog("Teacup", 20)
sarahs_dog.bark()
sarahs_dog.jump()

if  davids_dog.height > sarahs_dog.height :
            print({davids_dog.name})
else :
            print({sarahs_dog.name})


#Exercise 3 : Who’s The Song Producer?

#class Song:   
#    def __init__(self, lyrics):
#        self.lyrics = lyrics
#    def sing_me_a_song(self):
#            [print(line) for line in self.lyrics]
#stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
#stairway.sing_me_a_song()

#Exercise 4 : Afternoon At The Zoo
#It instantiates two attributes: animals (an empty list) and name (name of the zoo).
class Zoo:
    def __init__ (self, zoo_name):
        self.animals = []
        self.name = zoo_name
#Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.        
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(new_animal, "Already in",  self.name, "Zoo")
            return

#Create a method called get_animals that prints all the animals of the zoo.
    def get_animal(self):
        print(f"{self.animals}")
#Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(animal_sold, "Not in",  self.name, "Zoo")
            return
    
    def sort_animal(self):

        from itertools import groupby
        from operator import itemgetter

        for letters, words in groupby(sorted(self.animals), key=itemgetter(0)):
            for word in words:
                print([word]) 

#Create a method called get_groups that prints the animal/animals inside each group.
        
zoo1 = Zoo("ramat_gan_safari")
zoo1.add_animal("Bear")
zoo1.add_animal("Cat")
zoo1.add_animal("Ape")
zoo1.add_animal("Car")
zoo1.add_animal("Giraph")
zoo1.add_animal("Ape")
zoo1.add_animal("Eal")
zoo1.add_animal("Puma")
zoo1.add_animal("Cougar")
zoo1.add_animal("Baboon")
zoo1.sell_animal("Cat")
zoo1.get_animal()
zoo1.sort_animal()

#{ 
#   1: "Ape",
#    2: ["Baboon", "Bear"],
#    3: ['Cat', 'Cougar'],
#    4: ['Eel', 'Emu']
#}

#Create an object called ramat_gan_safari and call all the methods.
#Tip: The zookeeper is the one who will use this class.
#Example
#Which animal should we add to the zoo --> Giraffe
#x.add_animal(Giraffe)

