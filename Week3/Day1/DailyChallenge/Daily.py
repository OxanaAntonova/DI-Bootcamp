class Farm :
    def __init__(self, name) :
        self.farm_name = name
        self.all_animals = {}
    
    def add_animal(self, animal, number = 1) :
        if animal in self.all_animals :
            self.all_animals[animal] += number
        else :
            self.all_animals[animal] = number

    def get_info (self) :
        sentence = f"{self.farm_name}'s farm \n\n"
        for animal, amount in self.all_animals.items() :
            sentence += f"{animal} : {amount} \n"
        sentence += " \n E-I-E-I-0!".center(20) 
        return sentence

    def get_animals_type (self) :
        types = sorted(list(self.all_animals.keys()))
        return types # ['cow', 'goat', 'sheep'].
    
    def get_short_info (self) :
        all_types = self.get_animals_type()
        for index, type in enumerate(all_types) :
            if self.all_animals[type] > 1 :
                all_types[index] += "s"
        
        sentence_animals = ', '.join(all_types[0:-1])
        sentence = f"{self.farm_name}'s farm has {sentence_animals} and {all_types[-1]}"
        return sentence

macdonald = Farm("McDonald") #create the object
macdonald.add_animal('cow',5) #call the
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.add_animal('dog')
# print(macdonald.get_info())
print(macdonald.get_short_info())
# print(macdonald.get_animals_type())


# {
#     "cows" : 5,
#     "sheep" : 2
# } 