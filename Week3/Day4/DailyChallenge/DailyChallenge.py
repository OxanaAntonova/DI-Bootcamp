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

    #def word_freq(self):
    #    word_list = self.sentence.split()
    #    word_frequency = Counter(word_list)
    #    print(word_frequency)

    def word_common(self):
        word_list = self.sentence.split()  
        counts = Counter(word_list)
        top_word = counts.most_common(1)
        print(top_word)

    def word_unique(self):
        word_list = self.sentence.split() 
        count_all = Counter(word_list)
        for key, value in count_all.items():
            if 1 == value:
                return key

    def get_text_from_file(self, file):
        return "the_stranger.txt"

#str = "A good book would sometimes cost as much as a good house."
str = Text.get_text_from_file("the_stranger.txt")

t = Text(str)

#t.word_freq()
t.word_common()
t.word_unique()


#Implement a classmethod that returns a Text instance but with a text file:

#    >>> Text.from_file('the_stranger.txt')
#Hint: You need to open and read the text from the text file.

#Now, use the provided the_stranger.txt file and try using the class you created above.

