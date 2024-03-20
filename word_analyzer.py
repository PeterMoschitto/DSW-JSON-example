import json

#load the data from the JSON file
with open('foods.json') as food:
    food_data = json.load(food) 

print(food_data) #word_data is a list of dictionaries

print()

#access the first element in the list and then access the value for the key 'word'
print(food_data[0]['food'])

# for data in word_data: #data is each dictionary in the word_data list
#     print(data)
#     print()#print a blank line

# """
# for data in word_data: 
#     if data['part of speech'] == 'verb':
#         print(data['word'])
        
# num_nouns = 0
# for data in word_data:
#     if data['part of speech'] == 'noun':
#         num_nouns = num_nouns + 1
# print(num_nouns)"""
