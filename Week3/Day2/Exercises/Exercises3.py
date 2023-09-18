from Exercises import Dog
import random
class PetDog(Dog):
#Create a new python file and import your Dog class from the previous exercise.
#In the new python file, create a class named PetDog that inherits from Dog.
    def __init__(self, name, age, weight, trained = False):
        Dog.__init__(self, name, age, weight)
        self.trained = trained

#Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
#Add the following methods:
#train: prints the output of bark and switches the trained boolean to True
    def train(self):
        print(self.bark())
        self.trained = True

#play: takes a psarameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.
    def play(self, *args):
        print(self.name, end='')
        for arg in args:
            print(",", arg, end='')
        print(" are playing together")

#do_a_trick: If the dog is trained the method should print one of the following sentences at random:
#“dog_name does a barrel roll”.
#“dog_name stands on his back legs”.
#“dog_name shakes your hand”.
#“dog_name plays dead”.

    def do_a_trick(self):
        list = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead']
        if (self.trained):
            print(self.name, random.choice(list))
        else:
            print(self.name, "not trained")

print("Exercise3:")
PetDog1 = PetDog("Rex", 5, 7)
PetDog2 = PetDog("Gav", 4, 8)
PetDog3 = PetDog("Keks", 10, 9) 
PetDog1.train()
PetDog1.play(PetDog2.name, PetDog3.name)
PetDog1.do_a_trick()
PetDog2.train()
PetDog2.do_a_trick()

