#The goal of the exercise is to create a class that will help you analyze a specific text.
# A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.

#Part I
#First, we will analyze a simple string,
# like 

#Create a class called Text that takes a string as an argument and store the text in a attribute.
#Hint: You need to manually copy-paste the text, straight into the code
import collections
from collections import Counter

class Text:
    def __init__(self, sentence):
        self.sentence = sentence
        print("attr str:", str)

    def word_freq(self):
        word_list = self.sentence.split()
        word_frequency = Counter(word_list)
        print(word_frequency)

    def word_common(self):
        word_list = self.sentence.split()    
        most_common = Counter(word_list)
        return most_common


str = "A good book would sometimes cost as much as a good house."
t = Text(str)
#t.word_freq()
t.word_common()




#Implement the following methods:
#a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
#a method that returns the most common word in the text.
#a method that returns a list of all the unique words in the text.


