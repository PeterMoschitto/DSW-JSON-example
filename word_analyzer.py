import json

#load the data from the JSON file
with open('words.json') as words:
    word_data = json.load(words) 

print(word_data) #word_data is a list of dictionaries

#access the first element in the list and then access the value for the key 'word'
print(word_data[0]['word'])

"""
for data in word_data: #data is each dictionary in the word_data list
    if data['part of speech'] == 'verb':
        print(data['word'])
        
num_nouns = 0
for data in word_data:
    if data['part of speech'] == 'noun':
        num_nouns = num_nouns + 1
print(num_nouns)"""