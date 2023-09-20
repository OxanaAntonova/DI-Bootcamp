from collections import Counter, defaultdict 
import math
import random


class AnagramChecker:
    words_list = []
    def __init__(self, file_name):
        with open(file_name, "r") as english_words_file :
            for line in english_words_file:
                for word in line.split():
                    self.words_list.append(word)

    def is_valid_word(self, user_word):
        return user_word in self.words_list
    
    def get_anagrams(self, word):
        anagram_list =[]
        created_anagrams_num = 0
        combinations_num = math.factorial(len(word))
        while created_anagrams_num < combinations_num:
            cur_anagram = random.sample(word, len(word))
            if (cur_anagram in anagram_list):
                continue
            created_anagrams_num += 1
            anagram_list.append(cur_anagram)
        return anagram_list

"""
anagram = AnagramChecker("english_words.txt")
user_word = input("tell me a word:")
if (anagram.is_valid_word(user_word)):
    created_anagrams = anagram.get_anagrams(user_word)
"""
