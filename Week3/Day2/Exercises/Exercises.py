#class Pets():
#    def __init__(self, animals):
#        self.animals = animals

#    def walk(self):
#        for animal in self.animals:
#            print(animal.walk())

#class Cat():
#    is_lazy = True

#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def walk(self):
#        return f'{self.name} is just walking around'

#class Bengal(Cat):
#    def sing(self, sounds):
#        return f'{sounds}'

#class Chartreux(Cat):
#    def sing(self, sounds):
#        return f'{sounds}'

#class Siamese(Cat):    
#    def sing(self, sounds):
#        return f'{sounds}'   
    
#cat1 = Bengal('Myu', 2)
#cat2 = Chartreux('Caramel', 2)
#cat3 = Siamese('Popcorn', 2)

#all_cats = [cat1, cat2, cat3]

#sara_pet = Pets(all_cats)
#sara_pet.walk()

#Exercise 2 : Dogs

#Create a class called Dog with the following attributes name, age, weight.
#Implement the following methods in the Dog class:
#bark: returns a string which states: “<dog_name> is barking”.
#run_speed: returns the dogs running speed (weight/age*10).
#fight :  takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

#Create 3 dogs and run them through your class.
class Dog:
    def __init__(self, name, age, weight): 
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return (f"{self.name}  is barking") 
    
    def run_speed(self):
        speed = self.weight / self.age * 10
        print(speed)
        return speed
        
    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            print("Winner dog: ", self.name)    
        else:
            print("Winner dog: ", other_dog.name)

dog1 = Dog("Rex", 8, 7)
dog2 = Dog("Gav", 4, 8)
dog3 = Dog("Keks", 10, 9) 
other_dog = Dog("other", 4, 8)  
dog1.bark() 
dog2.bark()
dog3.bark()
dog1.run_speed()
dog2.run_speed()
dog3.run_speed()
dog1.fight(dog3)
dog1.fight(dog2)

#Exercise 3 : Dogs Domesticated

#Create a new python file and import your Dog class from the previous exercise.
#In the new python file, create a class named PetDog that inherits from Dog.
#Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
#Add the following methods:
#train: prints the output of bark and switches the trained boolean to True

#play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

#do_a_trick: If the dog is trained the method should print one of the following sentences at random:
#“dog_name does a barrel roll”.
#“dog_name stands on his back legs”.
#“dog_name shakes your hand”.
#“dog_name plays dead”.