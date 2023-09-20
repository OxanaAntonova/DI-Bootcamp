#import random

#def get_words_from_file() :
#    list = []
#    with open("sowpods.txt", "r") as sowpods_file :
#        for line in sowpods_file:
#            for word in line.split():
#                list.append(word)
#    return list

#def get_random_sentence(list, len):
#    sentence =[]
#    for i in range(len):
#        random_word = random.choice(list)
#        sentence.append(random_word)
#    return sentence

#def main():

#    print(f"In this program we will create a random sentence generator.")
#    len = int(input("How long you want the sentence to be? You can put the number between 2 and 20: "))

#    if (len < 2 or len > 20):
#        print('You put incorrect len:', len)
#        return

#    word_list = get_words_from_file()
#    random_sentence = get_random_sentence(word_list, len)
#    for word in random_sentence:
#        print(word, " ", end='')
#main()

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
#Access the nested “salary” key from the JSON-string above.

#Save the dictionary as JSON to a file.

import json

json_string = """{
   "age": 35,
   "children": [
      {
            "age": 6,
            "firstName": "Alice",
            "loves_school": true
      },
      {
            "age": 8,
            "firstName": "Bob",
            "loves_school": false
      }
   ],
   "email": "jane-doe@gmail.com",
   "firstName": "Jane",
   "hobbies": [
      "running",
      "sky diving",
      "singing"
   ],
   "lastName": "Doe"
}"""

dict_person = json.loads(json_string)
print(dict_person)

dict_second = {'age': 35, 'lastName': 'Doe'}
json_second = json.dumps(dict_second)
print(json_second)

dict_second = {
   "age": 35,
   "children": [
      {
            "age": 6,
            "firstName": "Alice",
            "loves_school": True
      },
      {
            "age": 8,
            "firstName": "Bob",
            "loves_school": False
      }
   ],
}


with open("person.json", "w") as file:
   json.dump(dict_second, file)


def check():
   with open('person.json', "r") as file:
      parsed_json = json.load(file)

   
   for key in parsed_json.keys():
      print(key)