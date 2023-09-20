from anagram_checkert import AnagramChecker 

anagram = AnagramChecker("english_words.txt")
user_word = ""
while user_word != "Exit":
    user_word = input("tell me a word:")
    if (1 < len(user_word.split())):
        print("Please enter only one word !!!")
        continue
    if (not user_word.isalpha()):
        print("Please enter only Alphabetic characters !!!")
        continue
    user_word = user_word.lstrip()
    if (anagram.is_valid_word(user_word)):
        print("YOUR WORD :", user_word, "\nthis is a valid English word.")
        created_anagrams = anagram.get_anagrams(user_word)
        print("Anagrams for your word: ", end='')
        for cur_anagram in created_anagrams:
            print(''.join(cur_anagram), "", end='')
        print("\n")

